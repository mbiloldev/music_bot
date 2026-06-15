import os

from aiogram import Router, types, F
from aiogram.types import FSInputFile

from services.music_search import search_music
from services.downloader import download_audio
from keyboards.inline import results_keyboard

router = Router()

# Foydalanuvchi qidirgan natijalarni vaqtincha saqlash uchun (xotirada)
search_cache: dict[int, dict[str, dict]] = {}


@router.message(F.text)
async def handle_search(message: types.Message):
    query = message.text.strip()
    if not query:
        return

    status = await message.answer("🔍 Qidirilmoqda...")

    try:
        results = search_music(query)
    except Exception:
        await status.edit_text("Qidirishda xatolik yuz berdi 😕")
        return

    if not results:
        await status.edit_text("Hech narsa topilmadi 😕")
        return

    search_cache[message.from_user.id] = {r["id"]: r for r in results}

    await status.edit_text(
        f"🎵 \"{query}\" bo'yicha natijalar:",
        reply_markup=results_keyboard(results),
    )


@router.callback_query(F.data.startswith("dl:"))
async def handle_download(callback: types.CallbackQuery):
    video_id = callback.data.split(":", 1)[1]

    await callback.message.edit_text("⬇️ Yuklab olinmoqda, biroz kuting...")

    try:
        file_path = download_audio(video_id)

        cache = search_cache.get(callback.from_user.id, {})
        title = cache.get(video_id, {}).get("title", "Musiqa")

        audio = FSInputFile(file_path, filename=f"{title}.mp3")
        await callback.message.answer_audio(audio, title=title)
        await callback.message.delete()

        os.remove(file_path)
    except Exception as e:
        await callback.message.edit_text(f"Xatolik yuz berdi: {e}")

    await callback.answer()

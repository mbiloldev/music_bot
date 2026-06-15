from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Salom! 🎵\n\n"
        "Men musiqa qidiruvchi botman.\n"
        "Menga qo'shiq nomini yoki ijrochi + qo'shiq nomini yozing, "
        "men topib, audio fayl sifatida yuboraman."
    )

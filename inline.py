from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def results_keyboard(results: list[dict]) -> InlineKeyboardMarkup:
    """Topilgan qo'shiqlar uchun tugmalar yaratadi."""
    builder = InlineKeyboardBuilder()

    for item in results:
        title = item["title"]
        text = title if len(title) <= 45 else title[:42] + "..."
        builder.button(text=text, callback_data=f"dl:{item['id']}")

    builder.adjust(1)
    return builder.as_markup()

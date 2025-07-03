from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

about_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="GitHub", url="https://github.com/Potismain")],
        [InlineKeyboardButton(text="Aiogram", url="https://docs.aiogram.dev/en/v3.20.0.post0/")]
    ]
)

# Клавиатура с кнопками переключения
keyboard_swap = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️", callback_data="prev"),
            InlineKeyboardButton(text="➡️", callback_data="next")
        ]
    ]
)

kb_start = InlineKeyboardMarkup(
    inline_keyboard= [
        [
        InlineKeyboardButton(text="Контакты\nразработчика", callback_data="contact"),
        InlineKeyboardButton(text="Случайная игра", callback_data="random_game")
        ]
    ]
)

yes_no_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Да",callback_data="yes"),
            InlineKeyboardButton(text="Нет",callback_data="no")
        ]
    ]
)

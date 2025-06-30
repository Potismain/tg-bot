from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import keyboard_swap


callback_router = Router()

@callback_router.callback_query(F.data == "send_test")
async def handle_button(callback: CallbackQuery):
    await callback.answer("Test button was clicked")

@callback_router.callback_query(F.data.in_(["prev", "next"]))
async def page_callback(callback: CallbackQuery):
    if callback.data == "next":
        await callback.message.edit_text("Страница 2", reply_markup=keyboard_swap)
    else:
        await callback.message.edit_text("Страница 1", reply_markup=keyboard_swap)

    await callback.answer()

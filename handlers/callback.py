from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from handlers.comands import send_first_page, show_menu
from keyboards.inline import keyboard_swap


callback_router = Router()

@callback_router.callback_query(F.data == "send_test")
async def handle_button(callback: CallbackQuery):
    await callback.answer("Test button was clicked")

@callback_router.callback_query(F.data.in_(["prev", "next"]))
async def page_callback(callback: CallbackQuery):
    if callback.data == "next":
        await callback.message.edit_text("Страница 3", reply_markup=keyboard_swap)
    else:
        await callback.message.edit_text("Страница 2", reply_markup=keyboard_swap)

    await callback.answer()


@callback_router.callback_query(F.data == "Нет")
async def process_dont_like_write_bots(callback: CallbackQuery, state: FSMContext):
    await state.update_data(like_bots="no")
    await callback.message.answer(
        "Not bad terrible.\\nSee you soon",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()
    await callback.answer()

@callback_router.callback_query()
async def handle_callback_query(callback_query: CallbackQuery):
    if callback_query.data == "random_game":
        await send_first_page(callback_query.message)
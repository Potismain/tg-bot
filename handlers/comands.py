import random
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from handlers.fsm import Form
from keyboards.inline import keyboard_swap, about_kb
from keyboards.inline import kb_start
from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from keyboards.inline import yes_no_keyboard
from aiogram.types import ReplyKeyboardRemove
from database import get_game


command_router = Router()

fsm_router = Router

# Обработка команды start
@command_router.message(Command("start"))
async def photo_start(message: Message):
    start_photo = FSInputFile("Start.png")
    await message.answer_photo(photo=start_photo, caption="Привет! Я твой бот помощник в подборке игр)\n"
                                                          "Чтобы узнать список команд напиши /help",
    reply_markup = kb_start)

# Обработка команды about
@command_router.message(Command("about"))
async def cmd_about(message: Message):
    cmd_about_text = (
        "Этот бот умеет подбирать игры случайно "
    )
    await message.answer(text=cmd_about_text)

# Обработка команды help
@command_router.message(Command("help"))
async def cmd_help(message: Message):
    cmd_help_text = (
        "Эти Команды могут помочь вам\n"
        "/start - Запустить бота.\n"
        "/help - Список команд.\n"
        "/about - Информация о боте.\n"
        "/contact - Контакты разработчика\n"
        "/random_game -Подбирает рандомную игру.\n"
    )
    await message.answer(text=cmd_help_text)

# Обработка сообщения "Привет"
@command_router.message(F.text.lower() == "привет")
async def hello_say(message: Message):
    await message.answer("Привет! Что бы узнать список доступных команд\n/help")

# Обработка стикера
@command_router.message(F.sticker)
async def sticker_say(message: Message):
    await message.answer("Стикеры запрешены")

# Обработка сообщений с эмодзи
@command_router.message(F.text.lower().contains("❤️"))
async def emoji_say(message: Message):
    await message.answer("Спасибо за сердечко но эмоджи запрешены")

# Обработка фото
@command_router.message(F.photo)
async def handle_photo(message: Message):
    await message.answer("Фото не принимаю")

# Обработка команды contact
@command_router.message(Command("contact"))
async def show_menu(message: Message):
    contact_message = "Контакты разработчика"

    await message.answer(text=contact_message, reply_markup=about_kb)


@command_router.message(Command("random_game"))
async def send_first_page(message: Message):
    games = get_game()
    # if not games:
    #     await message.answer(text="Нет доступных игр.")
    #     return
    # random_game = random.choice(games)
    #
    # await message.answer_photo(photo=random_game[1], caption=f"Описание: {random_game[2]}")
    str(games)
    r = random.choice(games)
    await message.answer_photo(photo = FSInputFile(r[1]), caption = r[2])


@command_router.callback_query(F.data == "next")
async def next_page(callback: CallbackQuery):
    photo_cover = FSInputFile("src/Don't_Starve.jpg")
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo_cover, caption="Don't Starve - это приключенческая игра на выживание с элементами roguelike, где игрок, играя за 1 из 15 персонажей, оказавшись в странном и враждебном мире, должен искать еду, ресурсы и строить убежище, чтобы выжить.\nОсновные цели - поддерживать здоровье, сытость и рассудок на достаточном уровне, исследовать мир и справляться с различными угрозами, включая смену времен года и монстров."),
        reply_markup=keyboard_swap
    )
    await callback.answer()

@command_router.callback_query(F.data == "prev")
async def prev_page(callback: CallbackQuery):
    photo = FSInputFile("src/Beholder_video_game.jpg")
    await callback.message.edit_media(
        media=InputMediaPhoto(media=photo, caption="Beholder - это антиутопическая игра, в которой вы играете за управляющего многоквартирным домом в тоталитарном государстве.\nВаша основная задача – шпионить за жильцами, собирать компромат и доносить на них в соответствующие органы.\nВ то же время, вы должны заботиться о своей семье и решать, как поступать в сложных моральных дилеммах, возникающих в условиях тоталитарного режима.\nИгра предлагает множество вариантов развития событий и концовок, зависящих от ваших решений."),
        reply_markup=keyboard_swap
    )


@command_router.message(Command("from"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет! Как тебя зовут?")
    await state.set_state(Form.name)

@command_router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer(text="Сколько тебе лет?")

@command_router.message(Form.age, F.text.isdigit())
async def progress_age(message:Message, state: FSMContext):
    await state.update_data(age = message.text)
    await state.set_state(Form.like_bots)
    data = await state.get_data()
    await message.answer(text=f"Приятно познакомится, {data['name']}\n Do yo liks tg bots?",
                         reply_markup = yes_no_keyboard)

@command_router.message(Form.like_bots, F.text.casefload() == "Нет")
async def process_dont_like_write_bots(message: Message, state: FSMContext):
    await state.update_data(like_bots = "no")
    await message.answer(
        "Not bad terriible.\nSee you soon",
        reply_markup = ReplyKeyboardRemove(),
    )

    await state.clear()


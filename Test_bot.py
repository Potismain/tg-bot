import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import TOKEN
from handlers.comands import command_router
from handlers.callback import callback_router


bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(command_router)
dp.include_router(callback_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from handlers.comands import command_router
from handlers.callback import callback_router
from Antiflood import AntiFloodMiddleware


storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

dp.message.middleware(AntiFloodMiddleware())


dp.include_router(command_router)
dp.include_router(callback_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


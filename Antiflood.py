import time
# необходимый для middleware компонент (родительский класс)
from aiogram import BaseMiddleware

from aiogram.types import Message
from collections import defaultdict

class AntiFloodMiddleware(BaseMiddleware):

    def __init__(self, delay: float = 2.5):
        self.delay = delay
        self.last_time = defaultdict(lambda: 0)

    async def __call__(self, handler, event: Message, data):
        # записываем id пользоваиеля в user_id
        user_id = event.from_user.id
        # записываем время обращения
        current_time = time.time()

        # 10.30.20 -- 10.15
        if current_time - self.last_time[user_id] < self.delay:
            # если ничего не писать --> игнорируем пользователя
            await event.answer("Подожди немного")
            return
        else:
            self.last_time[user_id] = current_time
            # выполняем обработку
            return await handler(event, data)



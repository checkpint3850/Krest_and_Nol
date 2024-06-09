import asyncio
import logging
import sys


from aiogram.filters import Command
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F
from aiogram.types import FSInputFile

from token_data import TOKEN

import info_text
from quiz_handler import router
from feedback import fdb_router
import kb_types

dp = Dispatcher()
dp.include_router(router)
dp.include_router(fdb_router)


@dp.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    photo = FSInputFile(r'D:\Python Projects\python_practice\Zoo.Moscow\Image_zoo\hello.jpg')
    await bot.send_photo(message.chat.id, photo, caption='Привет!👋')
    await message.answer(f"🐾Хочешь узнать кем бы Ты был(-а) в мире животных? Жми на викторину!🐾",
                         reply_markup=kb_types.kb_start_in)


@dp.callback_query(F.data == "о боте")
async def description(callback: types.CallbackQuery) -> None:
    await callback.message.answer(info_text.info_bot)


@dp.callback_query(F.data == "наши контакты")
async def description(callback: types.CallbackQuery) -> None:
    await callback.message.answer(info_text.contact_information)


@dp.callback_query(F.data == "опека")
async def description(callback: types.CallbackQuery) -> None:
    await callback.message.answer(info_text.custody)


@dp.message(Command('delete_data', 'shutdown_bot'))
async def danger(message: Message) -> None:
    await message.answer(f'Не стоит этого делать')


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

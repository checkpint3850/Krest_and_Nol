import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F
from token_data import TOKEN
from aiogram.utils.formatting import (
   Bold, as_list, as_marked_section
)

from recipes_handler import router

dp = Dispatcher()
dp.include_router(router)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    kb = [
        [
            types.KeyboardButton(text="Рецепты"),
            types.KeyboardButton(text="Описание бота"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(f"Привет! С чего начнем?", reply_markup=keyboard)


@dp.message(F.text.lower() == "описание бота")
async def description(message: types.Message):
    await message.answer("Этот бот предоставляет базу данных рецептов со всего мира.")


@dp.message(F.text.lower() == "рецепты")
async def commands(message: types.Message):
    response = as_list(
        as_marked_section(
            Bold("Команды:"),
            "/category_search_random - количество рецептов",
            marker="✅ ",
        ),
    )
    await message.answer(
        **response.as_kwargs()
    )

choises = {'Показать рецепт(ы)'}
cats = {'Beef', 'Breakfast', 'Chicken', 'Dessert', 'Goat', 'Lamb', 'Miscellaneous', 'Pasta', 'Pork', 'Seafood', 'Side',
        'Starter', 'Vegan', 'Vegetarian'}


@dp.message(~F.text.lower().startswith("/"), ~F.text.in_(cats), ~F.text.in_(choises))
async def handle_invalid_message(message: types.Message):
    await message.answer("Простите, я не понимаю вашего сообщения. Пожалуйста, используйте доступные команды.")


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

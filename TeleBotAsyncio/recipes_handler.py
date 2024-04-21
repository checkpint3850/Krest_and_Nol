import aiohttp

from random import choices
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.formatting import (
   Bold, as_list, as_marked_section
)

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, types
from aiogram import F

from utils import random_meal
from utils import choose_by_category

router = Router()
builder = ReplyKeyboardBuilder()
class NewMeal(StatesGroup):
    CATEGORY = State()
    ID = State()

@router.message(Command("category_search_random"))
async def category_search_random(message: Message, command: CommandObject, state: FSMContext):
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    async with aiohttp.ClientSession() as session:
        rand_category = await random_meal(session, command.args)

        for m in rand_category:
            builder.add(types.KeyboardButton(text=m))
        builder.adjust(4)
        await message.answer(
            f"Выберите категорию:",
            reply_markup=builder.as_markup(resize_keyboard=True),
        )
        await state.set_data({'category': command.args, 'quantity_meal': message.text})
        await state.set_state(NewMeal.CATEGORY.state)


@router.message(NewMeal.CATEGORY)
async def range_of_meal(message: types.Message, state: FSMContext):
    data = state.get_data()
    quant_meal = int(data['quantity_meal'])
    async with aiohttp.ClientSession() as session:
        rand_category = await choose_by_category(session, data['category'])
        if quant_meal > len(rand_category):
            await message.answer(f'В данной категории не больше {len(rand_category)} рецепта(ов)')
            new_range_meal = len(rand_category)
        select_meal = choices(rand_category, k=new_range_meal)
        for m in select_meal:
            builder.add(types.KeyboardButton(text=m))
        builder.adjust(4)
        await message.answer(
            f"Показать рецепты",
            reply_markup=builder.as_markup(resize_keyboard=True),
        )
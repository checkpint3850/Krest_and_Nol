import aiohttp

import random
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from googletrans import Translator

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, types

from utils import random_meal


router = Router()
builder = ReplyKeyboardBuilder()
translator = Translator()


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
    else:
        try:
            num_recipes = int(command.args)
            async with aiohttp.ClientSession() as session:
                rand_category = await random_meal(session, command.args)

            for m in rand_category:
                builder.add(types.KeyboardButton(text=m))
            builder.adjust(4)
            await message.answer(
                f"Выберите категорию:",
                reply_markup=builder.as_markup(resize_keyboard=True),
            )
            await state.update_data(CATEGORY=num_recipes)
            await state.set_state(NewMeal.CATEGORY.state)
        except ValueError:
            await message.answer("Ошибка: аргумент должен быть числом.")
        return


@router.message(NewMeal.CATEGORY)
async def range_of_meal(message: types.Message, state: FSMContext):
    data = await state.get_data()
    num_recipes = data['CATEGORY']
    chosen_category = message.text

    async with aiohttp.ClientSession() as session:
        url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={chosen_category}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data_meals = await resp.json()

        meals = data_meals.get("meals", [])
        if not meals:
            await message.answer("Извините, но для этой категории нет рецептов.")
            return

        if num_recipes > len(meals):
            await message.answer(f"Извините, но в этой категории доступно только {len(meals)} рецепта.")
            num_recipes = len(meals)

        selected_meals = random.sample(meals, k=num_recipes)
        await state.set_data({'selected_meals': selected_meals})
        recipe_names = [meal.get('strMeal') for meal in selected_meals]
        recipe_id = [meal.get('idMeal') for meal in selected_meals]

        await state.update_data(CATEGORY=recipe_id)
        translations_name = translator.translate(recipe_names, dest="ru")
        new_recipe_names = [recipe_name.text for recipe_name in translations_name]

        message_text = "<----Могу предложить такие варианты:---->\n" + "\n" + "\n".join(new_recipe_names)

        reply_markup = types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton(text="Показать рецепт(ы)")]],
            resize_keyboard=True
        )
        await message.answer(message_text, reply_markup=reply_markup)
        await state.set_state(NewMeal.ID.state)


@router.message(NewMeal.ID)
async def id_search_meal(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id_meals = data['CATEGORY']
    book_name_recipes = []
    book_instructions_recipes = []
    for m in id_meals:
        async with aiohttp.ClientSession() as session:
            url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={m}"

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    all_data_meals = await resp.json()
                    data_meals = all_data_meals.get('meals')
                    book_name_recipes.append(data_meals[0]['strMeal'])
                    book_instructions_recipes.append(data_meals[0]['strInstructions'])

    tr_book_name_recipes = []
    tr_book_instructions_recipes = []

    translations_name = translator.translate(book_name_recipes, dest="ru")
    for translation_n in translations_name:
        tr_book_name_recipes.append(translation_n.text)
    translations_inst = translator.translate(book_instructions_recipes, dest="ru")
    for translation_i in translations_inst:
        tr_book_instructions_recipes.append(translation_i.text)

    for n, i in zip(tr_book_name_recipes, tr_book_instructions_recipes):
        await message.answer(f'{n}'
                             f'\n'
                             f'\n Рецепт:'
                             f'\n'
                             f'\n {i}')
    reply_markup = types.ReplyKeyboardRemove()
    await message.answer(f'Приятного аппетита!'
                         '\n Чтобы посмотреть другие рецепты введите:'
                         '\n /category_search_random (количество рецептов)', reply_markup=reply_markup)
    await state.clear()

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Bot, Router, types
from aiogram.types import FSInputFile


import kb_types
from filter_dict import filer_dict_def
from filter_dict import filter_final
from information_animals import info_about_animals
import info_text


router = Router()


class QuizStep(StatesGroup):
    DICT_OF_ANIMALS = State()
    BIG_SIZE = State()
    SMALL_SIZE = State()
    PREDATOR = State()
    NIGHTTIME = State()
    FLY = State()
    COLOR = State()
    BEAK = State()
    UNDERWATER = State()
    CAT = State()
    DANGEROUS = State()
    HORNS = State()
    FROG = State()
    LIZARD = State()
    SHELL = State()
    TEETH = State()
    LEGS = State()
    RESULT = State()


@router.callback_query(F.data == "quiz")
async def begin_quiz(callback: types.CallbackQuery, state: FSMContext) -> None:
    dict_animals = info_about_animals.copy()
    await callback.message.answer(f'Вы маленький?:', reply_markup=kb_types.keyboard_small_size)
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    await state.set_state(QuizStep.SMALL_SIZE.state)


@router.message(QuizStep.BIG_SIZE)
async def big_or_not(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    predator = data['PREDATOR']
    dict_animals = data['DICT_OF_ANIMALS']
    answer = None

    if message.text == info_text.inf_size_b[0]:
        answer = True
    elif message.text == info_text.inf_size_b[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_big_size)
        return

    await filer_dict_def(answer, dict_animals, 'big_size')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    my_animal = await filter_final(dict_animals)

    if predator == info_text.inf_predator[1]:
        await message.answer(f'Возможно у вас есть рога?', reply_markup=kb_types.keyboard_horns)
        await state.set_state(QuizStep.HORNS.state)
    else:
        for i in my_animal:
            photo = FSInputFile(rf"Image_zoo\{i}.jpg")
            await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                                 reply_markup=kb_types.keyboard_after)
            await state.update_data(RESULT=i)
            await state.set_state(QuizStep.RESULT.state)


@router.message(QuizStep.SMALL_SIZE)
async def small_or_not(message: types.Message, state: FSMContext):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    answer = None

    if message.text == info_text.inf_size_s[0]:
        answer = True
    elif message.text == info_text.inf_size_s[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_small_size)
        return

    await filer_dict_def(answer, dict_animals, 'small_size')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)

    await state.update_data(SMALL_SIZE=message.text)
    await message.answer(f'Хищник ли вы?', reply_markup=kb_types.keyboard_predator)
    await state.set_state(QuizStep.PREDATOR.state)


@router.message(QuizStep.PREDATOR)
async def predator_or_not(message: types.Message, state: FSMContext):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    answer = None

    if message.text == info_text.inf_predator[0]:
        answer = True
    elif message.text == info_text.inf_predator[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_predator)
        return

    await filer_dict_def(answer, dict_animals, 'predator')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)

    await state.update_data(PREDATOR=message.text)
    await message.answer(f'Умеете ли вы летать?', reply_markup=kb_types.keyboard_fly)
    await state.set_state(QuizStep.FLY.state)


@router.message(QuizStep.NIGHTTIME)
async def night_or_not(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    small_size = data['SMALL_SIZE']
    predator = data['PREDATOR']
    fly_ = data['FLY']
    answer = None

    if message.text == info_text.inf_night[0]:
        answer = True
    elif message.text == info_text.inf_night[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_night)
        return

    await filer_dict_def(answer, dict_animals, 'nighttime')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    my_animal = await filter_final(dict_animals)

    if fly_ == info_text.inf_fly[0]:
        if answer is True:
            for i in my_animal:
                photo = FSInputFile(rf"Image_zoo\{i}.jpg")
                await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                                     reply_markup=kb_types.keyboard_after)
                await state.update_data(RESULT=i)
                await state.set_state(QuizStep.RESULT.state)
        else:
            if small_size == info_text.inf_size_s[1]:
                await message.answer(f'Быть может у вас большой клюв?', reply_markup=kb_types.keyboard_beak)
                await state.set_state(QuizStep.BEAK.state)
            else:
                for i in my_animal:
                    photo = FSInputFile(rf"Image_zoo\{i}.jpg")
                    await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                                         reply_markup=kb_types.keyboard_after)
                    await state.update_data(RESULT=i)
                    await state.set_state(QuizStep.RESULT.state)
    else:
        if answer is True and predator == info_text.inf_predator[0]:
            await message.answer(f'Возможно вы из семейства кошачих?', reply_markup=kb_types.keyboard_cat)
            await state.set_state(QuizStep.CAT.state)
        else:
            if small_size == info_text.inf_size_s[1]:
                await message.answer(f'Возможно вы очень большой?:', reply_markup=kb_types.keyboard_big_size)
                await state.set_state(QuizStep.BIG_SIZE.state)
            else:
                if predator == info_text.inf_predator[1] and small_size == info_text.inf_size_s[1]:
                    await message.answer(f'Возможно у вас есть рога?', reply_markup=kb_types.keyboard_horns)
                    await state.set_state(QuizStep.HORNS.state)
                else:
                    for i in my_animal:
                        photo = FSInputFile(rf"Image_zoo\{i}.jpg")
                        await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                                             reply_markup=kb_types.keyboard_after)
                        await state.update_data(RESULT=i)
                        await state.set_state(QuizStep.RESULT.state)


@router.message(QuizStep.FLY)
async def fly_or_not(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    predator = data['PREDATOR']
    answer = None

    if message.text == info_text.inf_fly[0]:
        answer = True
    elif message.text == info_text.inf_fly[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_fly)
        return

    await filer_dict_def(answer, dict_animals, 'fly')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    await state.update_data(FLY=message.text)
    my_animal = await filter_final(dict_animals)

    if answer is True:
        if predator == info_text.inf_predator[1]:
            await message.answer(f'А расцветка у вас экзотическая?', reply_markup=kb_types.keyboard_color)
            await state.set_state(QuizStep.COLOR.state)
        else:
            await message.answer(f'Любите гулять ночью?', reply_markup=kb_types.keyboard_night)
            await state.set_state(QuizStep.NIGHTTIME.state)
    else:
        await message.answer(f'Вы можете жить как в воде так и на суше', reply_markup=kb_types.keyboard_undwater)
        await state.set_state(QuizStep.UNDERWATER.state)


@router.message(QuizStep.UNDERWATER)
async def underwater_or_not(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    small_size = data['SMALL_SIZE']
    predator = data['PREDATOR']
    answer = None

    if message.text == info_text.inf_underwater[0]:
        answer = True
    elif message.text == info_text.inf_underwater[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_undwater)
        return

    await filer_dict_def(answer, dict_animals, 'underwater')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    await state.update_data(UNDERWATER=message.text)
    my_animal = await filter_final(dict_animals)

    if answer is True:
        if small_size == info_text.inf_size_s[1] and predator == info_text.inf_predator[0]:
            await message.answer(f'Есть ли у вас много мощных зубов?', reply_markup=kb_types.keyboard_teeth)
            await state.set_state(QuizStep.TEETH.state)
        elif small_size == info_text.inf_size_s[0] and predator == info_text.inf_predator[0]:
            await message.answer(f'Сидеть на болоте?', reply_markup=kb_types.keyboard_frog)
            await state.set_state(QuizStep.FROG.state)
        else:
            for i in my_animal:
                photo = FSInputFile(rf"Image_zoo\{i}.jpg")
                await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                                     reply_markup=kb_types.keyboard_after)
                await state.update_data(RESULT=i)
                await state.set_state(QuizStep.RESULT.state)
    else:
        await message.answer(f'Любите гулять ночью?', reply_markup=kb_types.keyboard_night)
        await state.set_state(QuizStep.NIGHTTIME.state)


@router.message(QuizStep.CAT)
async def cat_or_not(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    answer = None

    if message.text == info_text.inf_cat[0]:
        answer = True
    elif message.text == info_text.inf_cat[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_cat)
        return

    await filer_dict_def(answer, dict_animals, 'cat')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    my_animal = await filter_final(dict_animals)

    for i in my_animal:
        photo = FSInputFile(rf"Image_zoo\{i}.jpg")
        await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                             reply_markup=kb_types.keyboard_after)
        await state.update_data(RESULT=i)
        await state.set_state(QuizStep.RESULT.state)


@router.message(QuizStep.HORNS)
async def horns_or_not(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    answer = None

    if message.text == info_text.inf_horns[0]:
        answer = True
    elif message.text == info_text.inf_horns[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_horns)
        return

    await filer_dict_def(answer, dict_animals, 'horns')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    my_animal = await filter_final(dict_animals)

    for i in my_animal:
        photo = FSInputFile(rf"Image_zoo\{i}.jpg")
        await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                             reply_markup=kb_types.keyboard_after)
        await state.update_data(RESULT=i)
        await state.set_state(QuizStep.RESULT.state)


@router.message(QuizStep.TEETH)
async def teeth_or_not(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    answer = None

    if message.text == info_text.inf_teeth[0]:
        answer = True
    elif message.text == info_text.inf_teeth[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_teeth)
        return

    await filer_dict_def(answer, dict_animals, 'teeth')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    my_animal = await filter_final(dict_animals)

    for i in my_animal:
        photo = FSInputFile(rf"Image_zoo\{i}.jpg")
        await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                             reply_markup=kb_types.keyboard_after)
        await state.update_data(RESULT=i)
        await state.set_state(QuizStep.RESULT.state)


@router.message(QuizStep.COLOR)
async def color_or_not(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    answer = None

    if message.text == info_text.inf_color[0]:
        answer = True
    elif message.text == info_text.inf_color[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_color)
        return

    await filer_dict_def(answer, dict_animals, 'color')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    my_animal = await filter_final(dict_animals)

    for i in my_animal:
        photo = FSInputFile(rf"Image_zoo\{i}.jpg")
        await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                             reply_markup=kb_types.keyboard_after)
        await state.update_data(RESULT=i)
        await state.set_state(QuizStep.RESULT.state)


@router.message(QuizStep.BEAK)
async def beak_or_not(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    answer = None

    if message.text == info_text.inf_beak[0]:
        answer = True
    elif message.text == info_text.inf_beak[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_beak)
        return

    await filer_dict_def(answer, dict_animals, 'beak')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    my_animal = await filter_final(dict_animals)

    for i in my_animal:
        photo = FSInputFile(rf"Image_zoo\{i}.jpg")
        await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                             reply_markup=kb_types.keyboard_after)
        await state.update_data(RESULT=i)
        await state.set_state(QuizStep.RESULT.state)


@router.message(QuizStep.FROG)
async def frog_or_not(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    dict_animals = data['DICT_OF_ANIMALS']
    answer = None

    if message.text == info_text.inf_frog[0]:
        answer = True
    elif message.text == info_text.inf_frog[1]:
        answer = False
    else:
        await message.answer(f'Выберите пожалуйста из предложенных ответов', reply_markup=kb_types.keyboard_frog)
        return

    await filer_dict_def(answer, dict_animals, 'frog')
    await state.update_data(DICT_OF_ANIMALS=dict_animals)
    my_animal = await filter_final(dict_animals)

    for i in my_animal:
        photo = FSInputFile(rf"Image_zoo\{i}.jpg")
        await bot.send_photo(message.chat.id, photo, caption=f'Поздравляем! Вы - {i}',
                             reply_markup=kb_types.keyboard_after)
        await state.update_data(RESULT=i)
        await state.set_state(QuizStep.RESULT.state)


@router.message(QuizStep.RESULT)
async def result(message: types.Message, state: FSMContext):
    data = await state.get_data()
    animal = data['RESULT']

    inline_btn_after = [[types.InlineKeyboardButton(text='Попробовать еще раз🦊', callback_data='quiz')],
                        [types.InlineKeyboardButton(text='Опека🧸', callback_data='опека')],
                        [types.InlineKeyboardButton(text='Наши контакты📔', callback_data='наши контакты')],
                        [types.InlineKeyboardButton(text='Поделиться✉️',
                                                    switch_inline_query=f'Я {animal}, а кто ты?🦉\n'
                                                                        f'🦧Пройди небольшую викторину, '
                                                                        f'чтобы узнать своё тотемное животное🦬\n'
                                                                        f'https://t.me/Zoo_for_Me_bot')],
                        [types.InlineKeyboardButton(text='Оставить отзыв📝', callback_data='оставить отзыв')]
                        ]
    kb_after_in = types.InlineKeyboardMarkup(inline_keyboard=inline_btn_after)

    await message.answer(f'👭Хотите начать заново или поделиться с друзьями👬', reply_markup=kb_after_in)
    await state.clear()






from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, types


import info_text
from quiz_handler import router
import kb_types


fdb_router = Router()
feedback = {}


class FeedBackStep(StatesGroup):
    FEEDBACK = State()


@router.callback_query(F.data == "оставить отзыв")
async def begin_feedback(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(info_text.feedback)
    await state.set_state(FeedBackStep.FEEDBACK.state)


@router.message(FeedBackStep.FEEDBACK)
async def end_feedback(message: types.Message, state: FSMContext):
    feedback_ = {message.from_user.id: {'name': message.from_user.full_name,
                                        'feedback': message.text}}

    with open('feedback.txt', 'a', encoding='utf-8') as f:
        f.write(str(feedback_))

    await message.answer(f'Спасибо за ваш отзыв!🙏', reply_markup=kb_types.kb_start_in)
    await state.clear()

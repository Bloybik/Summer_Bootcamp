from assi import Token, game

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from assi import game, game_data


class ProgramState(StatesGroup):
    game_state = State()


bot = Bot(token=Token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def process_start_command(message: types.Message, state: FSMContext):
    if await state.get_state() != ProgramState.game_state.state:
        Button = types.InlineKeyboardMarkup()
        Button.add(types.InlineKeyboardButton(text="Начать играть", callback_data="start"))
        await message.answer("Привет!\nНажми на кнопку, чтобы начать играть!", reply_markup=Button)
    else:
        await message.answer("Вы уже начали игру, пожалуйста введите букву")


@dp.message_handler(commands=['help'], state='*')
async def process_help_command(message: types.Message, state: FSMContext ):
    if await state.get_state() != ProgramState.game_state.state:
        await message.answer("Введите /start чтобы начать играть")
    else:
        await message.answer("Введите одну букву")


@dp.message_handler(state=ProgramState.game_state)
async def game_handler(message: types.Message, state: FSMContext):
    await game(message, state)


@dp.callback_query_handler(state='*')
async def game_start(call: types.CallbackQuery, state: FSMContext):
    if call.data == "start":
        if await state.get_state() != ProgramState.game_state.state:
            await call.message.delete()
            await game_data(call.message)
            await ProgramState.game_state.set()
        else:
            await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp)

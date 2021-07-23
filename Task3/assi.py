from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext


Token = '1898258671:AAGJ-VKbtdkJZ-YHJdOSCbyTPl39zwoMFQo'


user_data = {}
in_word = []


async def game_data(message: types.Message):
    import random
    in_word.clear()
    words = ['Лягушка', 'Дерево', 'Собака', 'Чебурек', 'Амфитеатр', 'Дом', 'Антибиотик', 'Коробка',
             'Оториноларинголог', 'Педиатр', 'Компьютер', 'Салат']
    word = words[random.randint(0, len(words) - 1)].lower()
    mis = 0
    pop = 10
    full = 1
    user_data[message.chat.id] = {
        'mistake': mis,
        'pop': pop,
        'full': full,
        'word': word
    }
    for i in range(len(word)):
        in_word.append("_")
    await message.answer("Загаданное слово: " + " ".join(in_word))
    await message.answer("\nВведите букву")


async def game(message: types.Message, state: FSMContext):
    user = user_data[message.chat.id]
    if user['mistake'] < 10 and user['full'] <= 1:
        inp = message.text.lower()
        if len(inp) == 1 and inp.isalpha():
            let = inp
        else:
            await message.answer("Такой буквы нет повторите ввод")
            return
        if user['word'].find(let, 0, len(user['word'])) > -1:
            for i in range(len(user['word'])):
                if user['word'][i] == let:
                    in_word[i] = let
        await message.answer(" ".join(in_word))
        if user['word'].find(let, 0, len(user['word'])) == -1 and user['pop'] >= 1:
            user['mistake'] += 1
            user['pop'] -= 1
            await message.answer(f"Такой буквы нет у вас осталось %s попыток" % user['pop'])
        elif user['pop'] == 0:
            user['mistake'] += 1
        if '_' not in in_word:
            user['full'] = 2
    if user['mistake'] == 10:
        await message.answer("Игра окончена вы проиграли :(")
        await state.finish()
    if user['mistake'] < 10 and user['full'] == 2:
        await message.answer("Вы выиграли")
        await state.finish()


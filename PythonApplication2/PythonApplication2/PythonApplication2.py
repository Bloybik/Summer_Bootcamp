import random
words = ['Лягушка', 'Дерево', 'Собака', 'Чебурек', 'Амфитеатр', 'Дом', 'Антибиотик', 'Коробка', 'Оториноларинголог', 'Педиатр', 'Компьютер', 'Салат']
word = words[random.randint(0, len(words) - 1)].lower()
in_word = []
for i in range(len(word)):
    print('_', end=' ')
    in_word.append('_')
print()
mis = 0
pop = 10
full = 1
while mis < 10 and full <= 1:
    print("Введите букву")
    inp = input().strip()
    if len(inp) > 1 or inp == " ":
        print("Такой буквы нет повторите ввод")
        continue
    else:
        let = inp
    if word.find(let,0,len(word)) > -1:
        for i in range(len(word)):
            if word[i] == let:
                in_word[i] = let
                print(in_word[i], end=' ')
            else:
                print(in_word[i], end=' ')
    print()
    if word.find(let,0,len(word)) == -1 and pop > 1:
        mis += 1
        pop -= 1
        print(f"Такой буквы нет у вас осталось %s попыток" % pop)
    else:
        mis += 1
    if '_' not in in_word:
        full = 2
if mis == 10:
    print("Игра окончена вы проиграли")
if mis < 10:
    print("Вы выиграли")

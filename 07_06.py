'''
Всі ви, можливо, стикалися з ребусами "Знайди слово". 
Вони існують як текстові варіанти, так і як програми для мобільних додатків. Нагадаємо коротко суть ребуса. 
У великому квадраті з набором букв необхідно знайти слово по горизонталі та інколи по вертикалі.

game
Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) для знаходження слова, що шукається в рядку ребуса.

Параметри функції:

riddle - рядок із зашифрованим словом.
word_length – довжина зашифрованого слова.
start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
reverse - вказує, у якому порядку записане слово. 
За замовчуванням — в прямому. 
Для значення True слово зашифроване у зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.
'''


import sys 

i = sys.argv[1]
i = int(i)  # запуск перевірки py 07_06.py 4


riddle = ["mi1powerpret", "mi1powrepret", "mi1powperet", "aaatttrrr"]
word_length = [5, 3, 3, 5]
start_letter = ["p", "r", "r", "p"]
reverse = [False, False, True, True]

def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse == False:
        d = riddle.index(start_letter)
        s = riddle[d:d+word_length]
        return s
    elif reverse == True:
        try:
            d = riddle.rindex(start_letter)
            s = riddle[d:d-word_length:-1]
            return s
        except ValueError:
            s = "Пусто"
            return s
        

print(solve_riddle(riddle[i], word_length[i], start_letter[i], reverse[i]))
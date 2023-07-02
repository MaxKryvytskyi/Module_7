'''
Рекурсія добре підходить до задачі flatentening. 
Це процес вирівнювання списків, який полягає в позбавленні вкладеної структури.
Наприклад список вигляду [1, 2, [3, 4, [5, 6]], 7] має бути перетворений на плоский (flat) список [1, 2, 3, 4, 5, 6, 7]

Напишіть функцію flatten, яка приймає на вхід список, рекурсивно вирівнюватиме цей список і повертатиме пласку версію списку.

Для виконання завдання можна дотримуватися наступного алгоритму:

Якщо вхідний список порожній, то:
  Повертаємо порожній список
Якщо перший елемент списку є списком, то:
  Отримуємо перший список, рекурсивно викликавши функцію з першим елементом списку
  Отримуємо другий список, рекурсивно викликавши функцію з рештою списку без першого елемента
  Повертаємо конкатенацію двох списків
Якщо перший елемент списку не є списком, то:
  Отримуємо перший список із першого елемента списку
  Отримуємо другий список, рекурсивно викликавши функцію з рештою списку без першого елемента
  Повертаємо конкатенацію двох списків
'''

data = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]

def flatten(data):
    new_data = []
    if data == []:
        return []
    for el in data:
        if type(el) != list:
            new_data.append(el)
        elif type(el) == list:
            for i in el:
                new_data.append(i)
    
    if len(data) != len(new_data):
        data = new_data 
        return flatten(data)
    else:
        return new_data

print(flatten(data))





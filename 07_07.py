'''
У четвертому модулі розв'язували завдання нормалізації даних. Розширимо її.

При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати з даними далі. 
Напишіть функцію data_preparation, яка приймає набір даних, список списків (Приклад: [[1,2,3],[3,4], [5,6]]).

Функція повинна видаляти з переданих списків найбільше і найменше значення, але якщо розмір списку понад два елементи. 
Після видалення даних з кожного списку необхідно злити їх разом в один список, 
відсортувати його за зменшенням та повернути отриманий список як результат (Для прикладу вище результат буде наступним: [6, 5, 4, 3, 2]).
'''


import sys 

i = sys.argv[1]
i = int(i)  # запуск перевірки py 07_07.py 0

list_data = [[[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]], [[12, 22], [13, 5, 4], [6, 11, 71]], [[], []], []]

def data_preparation(list_data):
    sesult = []
    for el in list_data:
        if len(el) <= 2:
            sesult.extend(el)
        else:
            n = min(el)
            m = max(el)
            el.remove(m)
            el.remove(n)
            sesult.extend(el)
    sesult.sort()
    sesult.reverse()
    print(sesult)

data_preparation(list_data[i])
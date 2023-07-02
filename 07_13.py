'''
Є файл зі списком працівників компанії. 
У кожному рядку файлу записано інформацію лише одного співробітника. Формат запису, в межах навчання приймемо спрощений, такий як: 
ім'я співробітника, символ пропуску та його посада, тобто, ким він працює.

John courier
Pipe cook
Створіть функцію get_employees_by_profession(path, profession). 
Функція повинна у файлі (параметр path) знайти всіх співробітників зазначеної професії (параметр profession)

Вимоги:

відкрийте файл за допомогою with для читання
отримайте рядки з файлу за допомогою методу readlines()
за допомогою методу find знайдіть усі рядки у файлі, де є вказана profession, та помістіть записи до списку
об'єднайте всі ці рядки в списку в один рядок за допомогою методу join 
(пам'ятайте про символ перенесення рядків '\n' та зайві прогалини, які треба прибрати)
приберіть значення змінної 'profession' (замініть на порожній рядок "" методом replace)
поверніть отриманий рядок із файлу
'''


import re

path = "file14.txt"
profession = "courier"

def get_employees_by_profession(path, profession):
    with open(path, "r") as f:
        result = ""
        text = f.readlines()
        for i in text:
            flag = i.find(profession)
            if flag > 0:
                new_text = re.sub(r"\n", "", i)
                new_text = new_text.replace(profession, "")
                result += "".join(new_text)
        return result.rstrip()

print(get_employees_by_profession(path, profession))
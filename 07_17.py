'''
Повернемося до попереднього завдання та виконаємо зворотне. Напишіть рекурсивну функцію encode для кодування списку або рядка. 
Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) або рядок (наприклад, "XXXZZXXYYYZZ"). 
Функція повинна повернути закодований список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).
'''

data = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']

def encode(data):
    if len(data) == 0:
        return []
    value = data[0]
    result = []
    num = 0
    for val in data:
        if val == value:
            num += 1
        else:
            result.append(value)
            result.append(num)
            return result + encode(data[num:])
    return [value, num] + encode(data[num:])

print(encode(data))
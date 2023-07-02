'''
При роботі веб-сервісів спілкування, за протоколом HTTP, найчастіше відбувається в форматі JSON. 
І надсилання даних на сервер при запиті POST - це необхідність використовувати словник, оскільки структура формату JSON ідентична словнику Python.

Реалізуйте допоміжну функцію, яка формуватиме запит на сервер у вигляді словника. 
Дана функція make_request(keys, values) приймає два параметри у вигляді списків. 
Функція повинна створити словник із ключами з списку keys та значеннями зі списку values.

Порядок відповідності збігається з індексами списків keys та values.
Якщо довжина keys та values не збігаються, поверніть порожній словник.
'''

keys = ['name', 'age', 'email']
values = ['Nick', '23', 'nick@test.com']
def make_request(keys, values):
    new_dict = dict()
    if len(keys) != len(values):
        return new_dict
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    return new_dict
        
        
print(make_request(keys, values))
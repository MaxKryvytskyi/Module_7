'''
Дуже часто люди у своїх повідомленнях не ставлять великі літери, особливо це стало масовим явищем в еру мобільних. пристроїв. 
Розробіть функцію capital_text, яка прийматиме на вхід рядок з текстом і повертатиме рядок з відновленими великими літерами.

Функція повинна:

зробити великою першу літеру в рядку, попри прогалини
зробити великою першу літеру після точки, попри прогалини
зробити великою першу літеру після знака оклику, попри прогалини
зробити великою першу літеру після знака питання, попри прогалини
'''

s = "alert. boss! oh"

def capital_text(s):
    st = ""
    flag = True 
    for i in s:
        if i.isalpha():
            if flag:
                i = i.upper()
                flag = False
        elif i == "." or i == "!" or i == "?":
            flag = True
        st += i
    return st

print(capital_text(s))

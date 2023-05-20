import re

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

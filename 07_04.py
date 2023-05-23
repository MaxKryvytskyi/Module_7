import re


s = ["+34", "-17", "abc"]
def is_integer(s):
    s = re.sub(r"[^a-zA-Z0-9]", "", s)
    if len(s) == 0:
        return False
    return s.isdigit()
for i in s:
    print(is_integer(i))

         

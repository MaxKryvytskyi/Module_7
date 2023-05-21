
import re
s = '(2+ 3) *4 - 5 * 3' #"2+ 34 - 5 * 3"

def token_parser(s):
    new_list = re.findall(r'\d+|\S', s)
    return new_list
print(token_parser(s))
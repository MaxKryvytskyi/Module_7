
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
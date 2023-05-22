
string = "Hi there!" # Aloha Hawaii!



def sequence_buttons(string):
    list_button = {"0":[" "],
    "1":[".", ",", "?", "!", ":"],
    "2":["A", "B", "C"],
    "3":["D", "E", "F"],
    "4":["G", "H", "I"],
    "5":["J", "K", "L"],
    "6":["M", "N", "O"],
    "7":["P", "Q", "R", "S"],
    "8":["T", "U", "V"],
    "9":["W", "X", "Y", "Z"]
    }
    new_string = ""

    for i in string:
        for keys, val in list_button.items():
            try:
                index = val.index(i.upper())
                new_string += str(keys)*(index + 1)
            except ValueError:
                continue
    return new_string



print(sequence_buttons(string))
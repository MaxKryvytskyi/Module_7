
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
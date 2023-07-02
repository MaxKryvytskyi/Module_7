'''
Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу, 
додаватиме до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.

Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.

Нумерація рядків іде від 0.
'''

source_file = "file15.txt"
output_file = "new_file15.txt"

def to_indexed(source_file, output_file):

    with open(source_file, "r") as fn, open(output_file, "w") as f:
        for num, line in enumerate(fn):
                text = f"{num}: {line}"
                f.write(text)

to_indexed(source_file, output_file)
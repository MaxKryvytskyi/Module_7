
import sys 

i = sys.argv[1]
i = int(i)  # запуск перевірки py 07_07.py 0

list_data = [[[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]], [[12, 22], [13, 5, 4], [6, 11, 71]], [[], []], []]

def data_preparation(list_data):
    sesult = []
    for el in list_data:
        if len(el) <= 2:
            sesult.extend(el)
        else:
            n = min(el)
            m = max(el)
            el.remove(m)
            el.remove(n)
            sesult.extend(el)
    sesult.sort()
    sesult.reverse()
    print(sesult)

data_preparation(list_data[i])
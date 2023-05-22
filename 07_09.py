
import sys

i = sys.argv[1] # Параметри запуска py 07_09.py 0-2
i = int(i)

data = [[4, 6, 1, 3], [0, 1, 1, 2],[]]
# [[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]
# [[], [0], [1], [1], [2], [0, 1], [1, 1], [1, 2], [0, 1, 1], [1, 1, 2], [0, 1, 1, 2]]
# [[]]

def all_sub_lists(data):
    list_data = []
    if not data:
        list_data = [[]]
        return list_data
    
    list_data.append([])

    for i in data:
        list_1 = []
        list_1.append(i)
        list_data.append(list_1)

    for x in range(0,len(data)):
        c = (len(data)-1)
        if x == c:
            break
        else:
            list_2 = [data[x], data[x+1]]
            list_data.append(list_2)

    for v in range(0,len(data)):
        b = (len(data)-2)
        if v == b:
            break
        else:
            list_3 = [data[v], data[v + 1], data[v + 2]]
            list_data.append(list_3)
            
    list_data.append(data)
    return list_data
            

print(all_sub_lists(data[i]))


data = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']

# def encode(data):
#     if len(data) == 0:
#         return [] 
#     value = data[0]
#     num = 0
#     while num < len(data) and data[num] == value:
#         num += 1
#     return [value, num] + encode(data[num:])
# print(encode(data))

def encode(data):
    if len(data) == 0:
        return []
    value = data[0]
    result = []
    num = 0
    for val in data:
        if val == value:
            num += 1
        else:
            result.append(value)
            result.append(num)
            return result + encode(data[num:])
    return [value, num] + encode(data[num:])

print(encode(data))
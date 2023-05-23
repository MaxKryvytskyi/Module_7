

data = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]

def flatten(data):
    new_data = []
    if data == []:
        return []
    for el in data:
        if type(el) != list:
            new_data.append(el)
        elif type(el) == list:
            for i in el:
                new_data.append(i)
    
    if len(data) != len(new_data):
        data = new_data 
        return flatten(data)
    else:
        return new_data

print(flatten(data))











# def flatten(data):
#     result = []
#     for item in data:
#         if isinstance(item, list):
#             result += flatten(item)
#         else:
#             result.append(item)
#     return result
# flatten(data)



# def flatten(S):
#     if S == []:
#         return S
#     if isinstance(S[0], list):
#         return flatten(S[0]) + flatten(S[1:])
#     return S[:1] + flatten(S[1:])
# flatten(data)


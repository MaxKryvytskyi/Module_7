
data = [[], ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]]

def decode(data):
    result = []
    if not data:
        return data
    else:
        a = data.pop(0)
        b = data.pop(0)
        for _ in range(0, b):
            result.append(a)
        return result + decode(data)

print(decode(data[1]))



# def factorial(n):
#     if n == 0:  # базовий випадок: факторіал 0 = 1
#         return 1
#     else:  # рекурсивний випадок: факторіал n = n * факторіал (n-1)
#         return n * factorial(n-1)
    
# print(factorial(10))


# Працює але не рекурсія 

# def decode(data):
#     result = ""
#     if not data:
#         return data
#     else:
#         val = data[::2]
#         num = data[1::2]
#         for i in range(len(num)):
#             result += val[i] * num[i] 
#         return result
# print(decode(data[1]))

# def decode(data):
#     result = ""
#     if not data:
#         return data
#     else:
#         for i, val in enumerate(data):
#             if type(val) == str:
#                 result += data[i] * data[i+1]
#         return result

# print(decode(data[1]))
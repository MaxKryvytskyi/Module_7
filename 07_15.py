
 
data = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]

def flatten(data):
    if data == []:
        return data
    
    


flatten(data)
# def flatten(S):
#     if S == []:
#         return S
#     if isinstance(S[0], list):
#         return flatten(S[0]) + flatten(S[1:])
#     return S[:1] + flatten(S[1:])
# flatten(data)



keys = ['name', 'age', 'email']
values = ['Nick', '23', 'nick@test.com']
def make_request(keys, values):
    new_dict = dict()
    if len(keys) != len(values):
        return new_dict
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    return new_dict
        
        
print(make_request(keys, values))
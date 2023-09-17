my_dict = {'a': 5, 'b': 6}

new_dict = {}

for key, value in my_dict.items():
    new_dict[value] = key

print(new_dict)
def count_number(var):
    new_dict = {}
    for key in var:
        value = 0
        for j in var:
            if key == j:
                value += 1
                new_dict[key] = value
    return new_dict


list_number = [
    1, 2, 3,
    4, 5, 6,
    6, 3, 2
    ]

print(count_number(list_number))

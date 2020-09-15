dct = {
    "lol": "kek",
    'bobo': 12,
    True: [1, 2, 3],
    10: {
        'Sasha': "Larionov",
        'Vasya': "Vasionov"
    }
}


# print(dct[True])  # достать элемент
# dct['lol'] = 'azaza'  # заменить элемент
# dct['name'] = 'Ira'  # добавить пару
# dct.pop('bobo')  # удалить пару

for key in dct:
    print(dct[key])

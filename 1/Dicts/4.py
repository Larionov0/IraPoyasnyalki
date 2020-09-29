def find_sweety_pigs(piggies, min_milota=7, max_zubya=4):
    """
    :param piggies: список свиняшей
    :param min_milota: минимальная милота, при которой свиняша считается sweety
    :param max_zubya: максимальная кусючесть, при которой свиняша считается sweety
    :return: list: список свиняшей, подпадающих под категорию sweety
    """
    new_piggies = []
    for pig in piggies:  # pig: dict    {'name': 'Peppa','milota': 7,'zubya': 8}
        if pig['milota'] >= min_milota and pig['zubya'] <= max_zubya:
            new_piggies.append(pig)
    return new_piggies


piggies = [
    {
        'name': 'Peppa',
        'milota': 7,
        'zubya': 8
    },
    {
        'name': 'Zubba',
        'milota': 5,
        'zubya': 9
    },
    {
        'name': 'Irisha',
        'milota': 8,
        'zubya': 2
    },
    {
        'name': 'Zoppa',
        'milota': 10,
        'zubya': 4
    },
    {
        'name': 'Poro',
        'milota': 9,
        'zubya': 9
    },
    {
        'name': 'Buzyash',
        'milota': 9,
        'zubya': 7
    }
]


new_pigs = find_sweety_pigs(piggies)
for pig in new_pigs:
    print(pig)

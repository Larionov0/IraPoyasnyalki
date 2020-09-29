def sum_calculator():
    string = input("Введите числа через знак +\n")  # "2+5+4+1"
    numbers_list = string.split('+')  # ['2', '5', '4', '1']
    sum_ = 0
    for str_number in numbers_list:  # str_number = '2'
        number = int(str_number)  # 2
        sum_ += number
    print(f"Сумма чисел: {sum_}")  # Форматированная строка


def string_upper():
    string = input("Введите строку:\n")
    upper_string = string.upper()
    print(upper_string)


def store_menu():
    while True:
        print('--= Магазин =--')
        print('1 - купить функцию деления на 2')
        print('2 - купить всю лицензию')
        print('3 - купить раба')
        print('4 - выход из магазина')

        choice = input('Ваш выбор: ')
        if choice == '1':
            pass
        elif choice == '2':
            print("Лицензия пока недоступна :(")
        elif choice == '3':
            pass
        elif choice == '4':
            break
        else:
            pass


while True:
    print("\n\n--= Главное меню =--")
    print("1 - калькулятор суммы")
    print("2 - подниматор строки")  # 'lol kek'  ->  'LOL KEK'
    print("3 - магазин")
    print("4 - выход из программы")

    choice = input("Ваш выбор: ")
    if choice == '1':
        sum_calculator()

    elif choice == '2':
        string_upper()

    elif choice == '3':
        store_menu()

    elif choice == '4':
        break
    else:
        print("Такого варианта нету")

password = '12345'

while True:
    u_password = input("Введите пароль: ")
    if u_password == password:
        break
    else:
        print("Неправильный пароль!")


print("Secret")

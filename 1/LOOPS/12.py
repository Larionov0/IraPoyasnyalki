numbers = [12, 61, 51, 5, 3, 26, 1, 11, 32, 83, 35, 36, 12, 11, 53, 82]

current_max = float('-inf')
for number in numbers:
    if number > current_max:
        current_max = number

print(current_max)

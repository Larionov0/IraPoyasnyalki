numbers = [1, 5, 3, 6, 1, 6, 3, 8, 5, 3, 12, 11, 163, 14536273, 1231212, 75684]

count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1

print(count)

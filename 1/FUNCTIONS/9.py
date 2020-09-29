def incrementer(a):
    return a + 1


numbers = [1, 5, 4, 6, 2, 3]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] + 1

new_list = list(map(incrementer, numbers))

print(new_list)

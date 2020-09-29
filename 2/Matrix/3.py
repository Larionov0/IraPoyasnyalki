matrix = [
    [1, 5, 3, 6],
    [6, 2, 4, 1],
    [8, 3, 1, 5]
]

sum_ = 0
for row in matrix:  # [1, 5, 3, 6]
    row_sum = 0
    for element in row:
        row_sum += element
    sum_ += row_sum

print(sum_)

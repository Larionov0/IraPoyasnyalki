def transpose_matrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    matrix2 = []
    j = 0
    while j < len(matrix[0]):
        new_row = []
        for row in matrix:
            number = row[j]
            new_row.append(number)
        matrix2.append(new_row)
        j += 1
    return matrix2


def print_matrix(matrix):
    for row in matrix:
        text = ''
        for element in row:
            text += str(element) + ' '
        text = text[:-1]
        print(text)


matrix = [
    [1, 5, 3, 6],
    [6, 2, 4, 1],
    [8, 3, 1, 5]
]

print_matrix(matrix)
new_matrix = transpose_matrix(matrix)
print()
print_matrix(new_matrix)

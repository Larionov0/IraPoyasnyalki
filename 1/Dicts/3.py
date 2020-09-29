string = 'I love my mother, because she loves me!!!'

letters_counts = {}

for letter in string:  # 'm'
    if letter in letters_counts:
        letters_counts[letter] += 1
    else:
        letters_counts[letter] = 1

for letter in letters_counts:
    print(f"{letter} - {letters_counts[letter]}")
print(letters_counts)

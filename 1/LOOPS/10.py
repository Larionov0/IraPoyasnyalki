names = ['Ира', "Саша", "Кеша", "Глаша", 'Алина', "Боб", "Толик"]

count = 0
for name in names:
    # if 'а' in name or "A" in name:
    if 'а' in name.lower():
        count += 1

print(count)

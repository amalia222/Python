lst = [5, 98, 741, 22, 123, 111, 12, 1, 4, 4, 32]

# Функция, изменяющая список
lst.sort()
print(lst)

# Функция, не изменяющая список
sorted_lst = sorted(lst)
print(sorted_lst)

# --- --- --- --- --- --- --- ---

# Сортировка по последней цифре
lst.sort(key=lambda x: x % 10)
print(lst)

people = [
    ('Иван', 32),
    ('Максим', 32),
    ('Андрей', 21),
    ('Евгений', 44),
    ('Артем', 33),
    ('Алексей', 18),
    ('Даниил', 25),
    ('Константин', 32),
    ('Максим', 27),
    ('Владислав', 32),

]

# Сортировка по возрасту
people.sort(key=lambda x: x[1])
print(*people,  sep='\n')
print()

# Сортировка по нескольким полям
# Сортировка по возрасту, при одинаковом возрасте, сортировать по алфавиту
people.sort(key=lambda x: (x[1], x[0]))
print(*people,  sep='\n')

words = ['hello', 'hi', 'w', 'pyt', 'artem', 'andrey']

# Сортировка по длине слова
words.sort(key=len)
print(words)

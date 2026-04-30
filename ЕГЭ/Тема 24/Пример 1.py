# Неправильные последовательности
# ** и более подряд
# -- и более подряд
# 8, 9
#



max_len = 0
max_seq = ""

line = open('Пример 1.txt').read()

left = 0
right = 0
last_minus_pos = -1  # позиция последнего '-' в текущем окне

while right < len(line):
    c = line[right]

    if c not in '01234567*-':
        # Недопустимый символ (8, 9, пробелы и т.д.)
        left = right + 1
        last_minus_pos = -1

    elif c in '*-' and right > left and line[right - 1] in '*-':
        # Два спецсимвола подряд: **, --, -*, *-
        left = right + 1
        last_minus_pos = -1

    elif c == '*' and last_minus_pos >= left:
        # '*' после '-' — нарушение порядка операций!
        # Новое окно начинается сразу после последнего '-'
        left = last_minus_pos + 1
        last_minus_pos = -1
    # Если текущая подстрока верная
    else:
        if c == '-':
            last_minus_pos = right
        cur_len = right - left + 1
        if cur_len > max_len:
            max_len = cur_len
            max_seq = line[left:right + 1]

    right += 1

max_seq = max_seq.strip('-*')
print(max_seq, len(max_seq))

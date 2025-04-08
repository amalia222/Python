# ПРАВИЛЬНАЯ Генерация пустого двумерного списка
matrix = [[0] * 5 for i in range(5)]

# НЕПРАВИЛЬНАЯ (Создаются копии строк списка и меняются одновременно)
# matrix = [[0] * 5] * 5

# Таблица умножения
n = 10
m = 10
mult_table = [[i * j for i in range(1, m)] for j in range(1, n)]
print(*mult_table, sep='\n')
# -------------------------------------------------------

print(*matrix, sep='\n')
print()
matrix[0][0] = 1
print(*matrix, sep='\n')
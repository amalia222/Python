import hashlib

# Решение









# Ответ
answer = ...
print("Верно" if (hashlib.md5(str(answer).encode()).hexdigest() == 'e369853df766fa44e1ed0ff613f563bd') else "Неверно")

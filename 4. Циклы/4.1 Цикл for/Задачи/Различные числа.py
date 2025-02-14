n=int(input())
pos=0
z=0
neg=0
for i in range(n):
    num = int(input())
    if num > 0:
        pos += 1
    elif num == 0:
        neg += 1
    else:
        z += 1
print(f"Положительных: {pos}", f"Нулей: {z}", f"Отрицательных: {neg}",sep='\n')

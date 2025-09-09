a = int(input())
if a % 10 == 0 or 5 <= a % 10 <= 9 or 11 <= a % 100 <= 14:
    print(f'{a} грибов')
elif 2 <= a % 10 <= 4:
    print(f'{a} гриба')
else:
    print(f'{a} гриб')

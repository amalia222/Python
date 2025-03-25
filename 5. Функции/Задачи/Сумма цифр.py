def sumdigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumdigits(n // 10)
num = int(input())
print(sumdigits(num))
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)
num = int(input())
lst = [int(i) for i in input().split()]
lst.sort(key = sum_digits)
print(*lst)

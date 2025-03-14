def all_sum(n):
    if n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            print(all_sum(n - i))
num = int(input())
print(all_sum(num))
lst = [int(i) for i in input().split()]
lst[::2] = sorted(lst[::2])
print(*lst)
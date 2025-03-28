lst = [int(i) for i in input().split()]
k, m, d = [int(i) for i in input().split()]
lst[k - 1 : m] = sorted(lst[k - 1 : m], reverse = d < 0)
print(*lst)
lst = [int(i) for i in input().split()]
lst1 = [int(i) for i in input().split()]
k, m, d = lst1
lst[k - 1 : m] = sorted(lst[k - 1 : m], reverse = d < 0)
print(*lst)
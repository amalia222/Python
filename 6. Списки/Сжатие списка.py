lst = [int(i) for i in input().split()]
n = len(lst)
"""for i in range(len(lst) - 1, -1, -1):
    if lst[i] == 0:
        lst.append(lst.pop(i))"""
lst.sort(key = lambda x: x if x == 0 else float("inf"), reverse = True)
print(*lst)

def shift_right(lst, st):
    st = st % len(lst)
    return lst[-st:] + lst[:-st]
def shift_left(lst, st):
    return shift_right(lst, -st)
n = [int(i) for i in input().split()]
steps = int(input())
print(shift_right(n, steps))
print(shift_left(n, steps))
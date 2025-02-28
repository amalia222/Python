el = int(input())
n_el = el
p_el = n_el
max_st = 0
curr_st = 0
while n_el != 0:
    if n_el == p_el:
        curr_st += 1
    else:
        curr_st = 1
    if curr_st > max_st:
        max_st = curr_st
    p_el = n_el
    n_el = int(input())
print(max_st)

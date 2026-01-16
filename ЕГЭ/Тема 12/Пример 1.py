def f(s):
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    return s

s = '1' * 100
min_nums = 100
min_len = 0
while min_nums > 1:
    s += '1'
    res = f(s)
    if res.count('1') < min_nums:
        min_nums = res.count('1')
        min_len = len(s)
print(min_len, min_nums)

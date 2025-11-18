from itertools import product

def red(s):
    while not('00' in s):
        s = s.replace('033', '21120')
        s = s.replace('034', '22120')
        s = s.replace('04', '220')
        s = s.replace('030', '100')
    return s

list_a = list(product('34', repeat = 26))
for a in list_a:
    a = '0' + ''.join(a) + '0'
    b = red(a)
    if len(b) == 65:
        print(sum(b), a.count('3'))
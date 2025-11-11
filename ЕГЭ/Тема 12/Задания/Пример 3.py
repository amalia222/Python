from itertools import product

def red(s):
    s = s.replace('033', '21120')
    s = s.replace('034', '22120')
    s = s.replace('04', '220')
    s = s.replace('030', '100')
    return s

list_a = list(product('1234', repeat = 10))
for i in list_a:
    i = '0' + ''.join(i) + '0'
    if '3' in i:
        while not('00' in i):
            b = red(i)
            if len(b) == 65 and 
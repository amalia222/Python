from fnmatch import fnmatch

for i in range(0, 10 ** 10, 2026):
    i = str(i)
    if fnmatch(i, '7?23?64*8'):
        if int(i[1]) % 2 == 0 and int(i[4]) % 2 == 0:
            print(i)

'''
782386498
7023064168
7023864438
7623064068
7623864338
'''
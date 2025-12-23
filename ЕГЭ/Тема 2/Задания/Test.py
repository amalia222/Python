'''
s = []
for x in range(10, 200):
    for y in range(10, 200):
        if 3 * x + 5 * y == 340:
            s.append(500 * (x ** 2 + y ** 2))
            if 500 * (x ** 2 + y ** 2) == 1700000:
                print(x, y)
print(min(s))
'''
s = []
for x in range(10, 200):
    for y in range(10, 200):
        if 400 * x ** 2 + 500 * y ** 2 == 7200000:
            s.append(x + y)
print(max(s))
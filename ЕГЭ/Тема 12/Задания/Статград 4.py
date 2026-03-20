z = []
for a in range(0, 500):
    for b in range(0, 500):
        for c in range(0, 500):
            s = a * 7 + b * 8 + c * 3
            n = a + b + c
            if n > 300 and a * 7 + c * 3 >= 300 and 100000 <= s <= 999999:
                z.append(s + n)

print(min(z))
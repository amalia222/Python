for x in range(22):
    x1 = (9 * 22 ** 7) + (8 * 22 ** 6) + (x * 22 ** 5) + (7 * 22 ** 4) + (9 * 22 ** 3) + (6 * 22 ** 2) + (4 * 22 * 1) + (1 * 22 ** 0)
    x2 = (2 * 22 ** 4) + (5 * 22 ** 3) + (x * 22 ** 2) + (4 * 22 ** 1) + (9 * 22 ** 0)
    x3 = (6 * 22 ** 3) + (3 * 22 ** 2) + (x * 22 ** 1) + (5 * 22 ** 0)
    res = x1 + x2 + x3
    if res % 21 == 0:
        print(res // 21)
        break

# II способ

for x in sorted('0123456789qwertyuiopasdfghjklzxcvbnm'):
    x1 = int(f'98{x}79641', 22)
    x2 = int(f'25{x}49', 22)
    x3 = int(f'63{x}5', 22)
    res = x1 + x2 + x3
    if res % 21 == 0:
        print(res // 21)
        break
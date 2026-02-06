def is_simp(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


def get_divs(n):
    count_divs = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_simp(i):
            count_divs.add(i)
    return sum(count_divs)


for i in range(1475000, 1, -1):
    divs = get_divs(i)
    if 0 < divs < 42000 and (divs % 6 == 0):
        print(i)

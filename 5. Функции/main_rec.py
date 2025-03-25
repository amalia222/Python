def sum_seq(a, b):
    if a <= b:
        return a + sum_seq(a + 1, b)
    return 0

print(sum_seq(1, 10))
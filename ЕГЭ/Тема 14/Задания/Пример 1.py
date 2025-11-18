for x in range(10):
    res = int(f'2AB{x}', 12) + int(f'{x}8E', 17)
    if res % 27 == 0:
        print(res // 27)
        break

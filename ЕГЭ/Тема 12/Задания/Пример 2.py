for i in range(50):
    for j in range(50):
        for k in range(50):
            n = '0' + '1' * i + '2' * j + '3' * k
            while '01' or '02' or '03' in n:
                n = n.replace('01', '30', 1)
                n = n.replace('02', '101', 1)
                n = n.replace('03', '202', 1)
            if n.count('1') == 15 and n.count('2') == 10 and n.count('3') == 60:
                print(i)
from itertools import product

con = "РСМХ"
vow = "ОА"
for line in product(con, vow, con, vow, con, vow, con, vow):
    

'''for i1 in con:
    for i2 in vow:
        for i3 in con:
            for i4 in vow:
                for i5 in con:
                    for i6 in vow:
                        for i7 in con:
                            for i8 in vow:
                                s = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8
                                if s.count('') == 1 and s.count('') == 1 and s.count('') == 1 '''
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))
# Решение
import re

text = open('+Задание 101.txt').read()

print(len(re.findall(r'.ток.', text)))

answer = 31

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(10, 101, answer, 'c16a5320fa475530d9583c34fd356ef5'))
# Решение


answer = ...

#

import datetime
import hashlib
from ЕГЭ.tests.conftest import add_result
if answer is not Ellipsis:
    result = 1 if hashlib.md5(str(answer).encode()).hexdigest() == '7379de4777f5748aa568b8d0bf8c3795' else 0
    print("Верно" if result else "Неверно")
    add_result(datetime.now().timestamp(), 11, 2, result)
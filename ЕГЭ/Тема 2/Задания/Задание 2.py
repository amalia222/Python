# Решение







answer = ...

#

import datetime
import hashlib
from ЕГЭ.tests.conftest import add_result
if answer is not Ellipsis:
    result = 1 if hashlib.md5(str(answer).encode()).hexdigest() == 'e0abee87e4ba1de22c6b8cf076c5016b' else 0
    print("Верно" if result else "Неверно")
    add_result(datetime.now().timestamp(), 2, 2, result)
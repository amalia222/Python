from fnmatch import fnmatch
for i in range(107, 10 ** 9, 107):
  if fnmatch(str(i), '38?375*9'):
    print(i, i / 107)
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(24, 2401, answer, '0e65972dce68dad4d52d063967f0a705'))
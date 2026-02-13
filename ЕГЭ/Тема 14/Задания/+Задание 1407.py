x = 343 ** 5 + 343 ** 4 + 49 ** 6 - 7 ** 13 - 21
nums = set()
while x != 0:
    nums.add(x % 7)
    x //= 7
print(len(nums))

answer = 4

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1407, answer, 'a87ff679a2f3e71d9181a67b7542122c'))
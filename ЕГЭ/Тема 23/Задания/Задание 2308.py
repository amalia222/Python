def f(x, step, numbers):
    if step == 15:
        numbers.add(x)
    return f(x * 2, step + 1, numbers) + f(x * 2 + 1, step + 1, numbers)

nums = set()
f(1, 0, nums)
print(len(nums))
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(23, 2308, answer, 'f43764367fa4b73ba947fae71b0223a4'))
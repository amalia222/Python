from turtle import *
tracer(0)
k = 10
for i in range(2):
    forward(15 * k)
    right(90)
    forward(8 * k)
    right(90)

up()
for x in range(-k, k + 1):
    for y in range(-k, k + 1):
        goto(x * k, y * k)
        dot(3)
exitonclick()
answer = 49

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 64, answer, '9f61408e3afb633e50cdf1b20de6f466'))
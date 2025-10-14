# Решение
from turtle import *

tracer(0)
k = 20

for i in range(2):
    forward(3 * k)
    left(90)
    backward(10 * k)
    left(90)

up()

backward(10 * k)
right(90)
forward(8 * k)
left(90)

down()

for i in range(2):
    forward(8 * k)
    right(90)
    forward(8 * k)
    right(90)

up()

for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()
answer = 185

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(6, 6, answer, 'eecca5b6365d9607ee5a9d336962c534'))

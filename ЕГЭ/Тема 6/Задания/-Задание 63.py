'''from turtle import *
tracer(0)
k = 10

for i in range(7):
    forward(17 * k)
    right(90)
    forward(26 * k)
    right(90)

up()

forward(4 * k)
right(90)
forward(6 * k)
left(90)

down()

for i in range(7):
    forward(248 * k)
    right(90)
    forward(345 * k)
    right(90)

up()

for x in range(-k, k * 2):
    for y in range(-k * 2, k):
        goto(x * k, y * k)
        dot(3)

exitonclick()
'''
answer = 96058

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 63, answer, '35495f83adcdab84ab446b313a3e0cb4'))
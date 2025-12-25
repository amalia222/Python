from turtle import *
tracer(0)
k = 10
x = 14

forward((x + 2) * k)
for i in range(4):
    forward(x * k)
    right(90)
    forward((x + 2) * k)

right(90)
forward(x * 2 * k)

for i in range(4):
    right(90)
    forward((3 * x - 1) * k)

up()
for x in range(-k * 3, k * 3):
    for y in range(-k * 3, k * 3):
        goto(x * k, y * k)
        dot(3)
exitonclick()

answer = 14

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 61, answer, 'aab3238922bcc25a6f606eb525ffdc56'))
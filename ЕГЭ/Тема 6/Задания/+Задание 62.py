'''from turtle import *
tracer(1)
k = 10

right(180)

for i in range(9):
    forward(59)
    left(90)
    forward(84)
    left(90)

forward(18)
left(90)
forward(38)
right(90)

for i in range(9):
    forward(120)
    right(90)
    forward(99)
    right(90)

up()

for x in range(-k, k):
    for y in range(-k ,k):
        goto(x * k, y * k)
        dot(3)

exitonclick()
'''
answer = 158

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 62, answer, '06409663226af2f3114485aa4e0a23b4'))
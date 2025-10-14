from turtle import *
tracer(0)
k = 20
x = 6

down()

forward((x + 2) * k)
for i in range(4):
    forward(x * k)
    right(90)
    forward((x + 2) * k)
right(90)
forward(2 * x * k)
for i in range(4):
    right(90)
    forward((3 * x - 1) * k)

up()

for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()
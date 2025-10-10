from turtle import *
tracer(1)
k = 18

down()

for i in range(1, 5):
    for j in range(1, 5):
        forward(6 * k)
        right(90)
    forward(10 * k)
    right(90)
    forward(3 * k)

up()

for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()
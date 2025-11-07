from turtle import *
k = 20
tracer(0)

down()

for i in range(7):
    forward(k * 10)
    right(120)

up()

for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)

exitonclick()
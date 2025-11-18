from turtle import *
tracer(0)
k = 15

for i in range(4):
    forward(16 * k)
    right(90)
    forward(18 * k)
    right(90)

up()

right(90)
forward(10 * k)
left(90)
forward(10 * k)

down()

for i in range(4):
    forward(15 * k)
    right(90)

up()

forward(1 * k)
left(90)
forward(1 * k)
right(90)

down()

for i in range(7):
    forward(12 * k)
    right(90)

up()
for x in range(-k * 2, k * 2):
    for y in range(-k * 2, k * 2):
        goto(x * k, y * k)
        dot(3)

exitonclick()
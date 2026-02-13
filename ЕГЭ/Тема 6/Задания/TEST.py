from turtle import *

tracer(0)
k = 15

for i in range(2):
    forward(17 * k)
    right(90)
    forward(10 * k)
    right(90)

up()

forward(7 * k)
right(90)

down()

for i in range(2):
    forward(20 * k)
    right(90)
    forward(4 * k)
    right(90)
up()
for x in range(-k ,k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()
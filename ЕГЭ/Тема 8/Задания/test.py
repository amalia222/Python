from turtle import *
tracer(0)
k = 25

down()

for i in range(6):
  forward(7 * k)
  right(120)

up()

forward(3 * k)
right(90)

down()

for i in range(8):
  forward(5 * k)
  right(90)

up()

for x in range(-k, k):
  for y in range(-k, k):
    goto(x * k, y * k)
    dot(3)

exitonclick()
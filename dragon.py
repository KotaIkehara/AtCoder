import turtle
import math
kamepy = turtle.Turtle()
kamepy.speed(0)

size = kamepy.getscreen().screensize()
kamepy.penup()
kamepy.setx(- size[0] / 2)
kamepy.pendown()


def dragon(generation, length, sign):
    if(generation == 0):
        kamepy.forward(length)
    else:
        kamepy.left(sign * 45)
        dragon(generation-1, length / math.sqrt(2), 1)
        kamepy.right(sign*90)
        dragon(generation-1, length / math.sqrt(2), -1)
        kamepy.left(sign*45)


dragon(15, size[0], 1)
turtle.done()

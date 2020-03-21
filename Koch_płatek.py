from turtle import *


def Koch(length, depth):
    if depth == 0:
        forward(length)
    else:
        Koch(length / 3, depth - 1)
        right(60)
        Koch(length / 3, depth - 1)
        left(120)
        Koch(length / 3, depth - 1)
        right(60)
        Koch(length / 3, depth - 1)


Koch(500, 4)
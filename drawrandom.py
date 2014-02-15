# simple.py
# - a simple python program

from random import random
from polygon import *
from turtle import done,up,down,goto


def move(x,y):
    up()
    goto(x,y)
    down()
#move(10,10)
for i in range(50):
    x = int(random()*200)
    y = int (random()*200)
    move(x,y)
    side =int(random()*5+3)
    if (side == 3):
        color('green')
    elif side == 5:
        color('blue')
    elif side == 7:
        color('red')
    else:
        color('black')
    polygon(int(random()*50),side)

done()
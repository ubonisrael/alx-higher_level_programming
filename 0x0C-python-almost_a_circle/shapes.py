#!/usr/bin/python3
import os
from turtle import *

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

window = Screen()
window.bgcolor("white")

turtle_1 = Turtle()
turtle_1.shape("turtle")
turtle_1.color("red")

window.exitonclick()

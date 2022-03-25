""" Videogame 'PAINT' from the library 'freegames' of Python3
    This version have been modified from the original.
    Authors: Frida Cano Falcón & Yahir
"""
from turtle import *
import turtle
from freegames import vector
import math

def line(start, end):
    """Draw line from start to end,
       using the function goto() of turtle that move the pen between 2 coordinates.

    Args:
        start (int): Coordenate (pixels) in x and y of the first tap.
        end (int): Coordenate (pixels) in x and y of the last tap.
    """
    up()                   #Pull the pen up  - no drawing when moving
    goto(start.x, start.y) #Move the pen in order of the 2 coordinates (x, y)
    down()                 #Pull the pen down - drawing when moving
    goto(end.x, end.y)     #Move the pen in order of the 2 coordinates (x, y)

def square(start, end):
    """Draw square from start to end filled.
       using the function goto() of turtle that move the pen between 2 coordinates.
    Args:
        start (int): Coordenate (pixels) in x and y of the first tap.
        end (int): Coordenate (pixels) in x and y of the last tap.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()                 #This function is used to appoint the shape that is going to be fill

    for count in range(4):       #Make the shape of the square : 4 lines with end.x - start.x lenght
        forward(end.x - start.x)
        left(90)                 #Angle between the lines

    end_fill()                   #This function is used to close the shape that is going to be fill

def circle(start, end):
    """Draw circle from start to end filled.
       using the function goto() of turtle that move the pen between 2 coordinates.
    Args:
        start (int): Coordenate (pixels) in x and y of the first tap.
        end (int): Coordenate (pixels) in x and y of the last tap.
    """

    r=math.dist(start,end)
    up()
    goto(start.x, start.y-r)
    down()
    begin_fill()
    turtle.circle(r)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end filled.
       using the function goto() of turtle that move the pen between 2 coordinates.
    Args:
        start (int): Coordenate (pixels) in x and y of the first tap.
        end (int): Coordenate (pixels) in x and y of the last tap.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):                 #Make shape of the rectangle.
        forward(end.x - start.x - start.x) #Longest side
        left(90)                           #Angle between the lines
        forward(end.x - start.x)           #Shorter side
        left(90)                           #Angle between the lines

    end_fill()

def triangle(start, end):
    """Draw triangle from start to end filled,
       using the function goto() of turtle that move the pen between 2 coordinates.
    Args:
        start (int): Coordenate (pixels) in x and y of the first tap.
        end (int): Coordenate (pixels) in x and y of the last tap.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):       #Shape of the scalene triangle: only 3 lines
        forward(end.x - start.x) 
        left(120)                #Angle between the lines

    end_fill()

def tap(x, y):
    """Store starting point or draw shape.

    Args:
        x (int): Coordenate (pixels) in x of the tap in the field.
        y (int): Coordenate (pixels) in y of the tap in the field.
    """
    start = state['start']

    if start is None:
        state['start'] = vector(x, y) # Assign the coordinates of the tap to the variable
    else:
        shape = state['shape'] #Detect the shape to make according to the nomenclature
        end = vector(x, y)     #Assign the coordinates of the tap to the variable
        shape(start, end)
        state['start'] = None  

def store(key, value):
    """Store value in state at key.

    Args:
        key (string): Describe the thing to do.
        value (function): Designates the type of figure according to the function.
    """
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
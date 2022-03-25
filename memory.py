""" Videogame 'MEMORY' from the library 'freegames' of Python3.
    This version have been modified from the original.
    Simulates the Memory puzzle.
    Authors: Frida Cano Falcón & Yahir Ulises Villa Camorlinga
"""
from random import *
from turtle import *
from freegames import path

#Principal variables
car = path('car.gif') #Insert the image of the puzzle
tiles = list(range(32)) * 2 #Cards
state = {'mark': None, 'num_tap': 0, 'num_par':0}
hide = [True] * 64 #Hide the image

def square(x, y):
    """Draw white square with black outline at (x, y).

    Args:
        x (int): Coordenate (pixels) in x.
        y (int): Coordenate (pixels) in y.
    """
    up()
    goto(x, y)
    down()
    color('black', 'white') # Squares colors : of the outline and the filled.
    begin_fill()
    for count in range(4):  # Creation of the square. Lenght: 50px.
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index.

    Args:
        x (int): Coordenate (pixels) in x.
        y (int): Coordenate (pixels) in y.

    Returns:
        int : index of the tile
    """
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates.

    Args:
        count (int): Tile number.

    Returns:
        x, y (int): Coordenate (pixels) in x and y.
    """
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap.

    Args:
        x (int): Coordenate (pixels) in x.
        y (int): Coordenate (pixels) in y.
    """
    spot = index(x, y)
    mark = state['mark']
    state['num_tap'] += 1             #Taps increase
    print('Taps:', state['num_tap'])  #Print in the console
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        state['num_par'] += 1        #Number of pairs done
        if state['num_par'] == 32:   #Verify if the game is over
            print('JUEGO TERMINADO')
        else:
            print('Llevas ', state['num_par'], ' pares')

def draw():
    """Draw image and tiles. Displays the numbers of the tiles."""
    clear()
    goto(0, 0)
    shape(car)                #Display the image
    stamp()

    for count in range(64):   #Draw the tiles
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Center the digits of the tiles
        if tiles[mark] <= 9 :                         # 1 digit number
            goto(x + 15, y)
        elif tiles[mark] >= 10 and tiles[mark] <= 19 :# 2 digit number from 10 to 20
            goto(x + 3, y)
        else:                                         # 2 digit number from 20
            goto(x + 4, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)
#Organize the order of the items.
shuffle(tiles)
#Set the size ando position of the main window in the monitor.
setup(420, 420, 370, 0)
#Add the image
addshape(car)
hideturtle()
tracer(False)
#Assign the function tap to a physical mouse tap.
onscreenclick(tap)
draw()
done()
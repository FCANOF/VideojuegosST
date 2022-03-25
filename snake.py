""" Videogame 'SNAKE' from the library 'freegames' of Python3
    This version have been modified from the original.
    Simulates the game of Snake, where the snake eat an apple and get bigger each time
    Authors: Frida Cano Falcón & Yahir Ulises Villa Camorlinga
"""
from turtle import *
from random import randrange
from freegames import square, vector

#Principal variables of the elements of the game
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

valor = 0
color =""
condicion = True
valor2 = 0
color2 =""
#Generate 2 random numers to set different colors for food
#and snake body every time the code is runned again
valor =randrange(1,6) 
if (valor == 1):
    color = "pink"
if (valor == 2):
    color = "green"
if (valor == 3):
    color = "blue"
if (valor == 4):
    color = "yellow"
if (valor == 5):
    color = "orange"

while(condicion == True):
    valor2 =randrange(1,6) 
    if (valor != valor2):
        condicion = False

if (valor2 == 1):
    color2 = "pink"
if (valor2 == 2):
    color2 = "green"
if (valor2 == 3):
    color2 = "blue"
if (valor2 == 4):
    color2 = "yellow"
if (valor2 == 5):
    color2 = "orange"




def change(x, y):
    """Change modifies the snake´s moving direction and simultaneusly moves 
       one unit the food in an aleatory direction, this was on of the modification requirements

    Args:
        x (int): Coordenate (pixels) in x of the tap.
        y (int): Coordenate (pixels) in y of the tap.
    """
    #Movement of the snake - change of the coordenates
    aim.x = x
    aim.y = y

    #Random movement of the food
    food_change = randrange(-2,2) #Banner of the change of direction of the food
    if food_change == -2:         
        food.y = food.y - 10      #Move one step down.
    elif food_change == -1:
        food.x = food.x - 10      #Move one step to the left.
    elif food_change == 1:
        food.x = food.x + 10      #Move one step to the right.
    elif food_change == 2:
        food.y = food.y + 10      #Move one step up.

def inside(head):
    """Returns a true boolean value while the sanke head remain within thes afe zone

    Args:
        head (vector): the location of the snake´s head

    Returns:
        boolean: To know if the snake´s head is within the boundaries of the game
    """
    
    return -200 < head.x < 190 and -200 < head.y < 190 #Limits of the field

def move():
    """Every .100 it forces the snake to move one unit no matter 
    the movement direction given by the keybord arrows
    """
    head = snake[-1].copy()
    head.move(aim)
    #Watch if the head hits the body
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    #Generete new food in random location each time the head reaches the current one 
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    #Set the snake´s body a color
    for body in snake:
        square(body.x, body.y, 9, color)
    #Set food color
    square(food.x, food.y, 9, color2)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)# Set game size
hideturtle()
tracer(False)
listen()#Create key litener on the arrows for movement
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
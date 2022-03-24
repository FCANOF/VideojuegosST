from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

valor = 0
color =""
condicion = True
valor2 = 0
color2 =""

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

#print ("color1 = "+ color)
#print ("color2 = "+ color2)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
    food_change = randrange(-2,2)
    if food_change == -2:
        food.y = food.y - 10
    elif food_change == -1:
        food.x = food.x - 10
    elif food_change == 1:
        food.x = food.x + 10
    elif food_change == 2:
        food.y = food.y + 10

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color)

    square(food.x, food.y, 9, color2)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
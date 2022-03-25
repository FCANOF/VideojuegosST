from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    """Runs every time theres a click on the screen generating a ball

    Args:
        x (int): x coordinate of the ball
        y (int): y coordinate of the ball
    """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    """To know if the coordinates are in the game boundaries

    Args:
        xy (coordinates): location of the object in the game screen (x,y)

    Returns:
        boolean: answer to the coordinates being in the game boundaries or not
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Re draw the ball and tarjects with ther respective size and color
    """
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """Crete tarjets at the right side of the screen in random y location every period of time
    """
    #Random location and timing apearance of the tarjects
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
    #speed of tarjets
    for target in targets:
        target.x -= 0.5
    #ball falling speed
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
    draw()
    # make the game infinite by repositioning the missed tarjects
    for target in targets:
        if not inside(target):
            target.x= 190
    
    # time period
    ontimer(move, 20)
    return

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
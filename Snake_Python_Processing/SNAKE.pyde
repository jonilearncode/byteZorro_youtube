from Snake import *
from Apple import *

snake = Snake(PVector(300,200), PVector(1,0))
list_apples = []

def setup():
    # processing func run once before draw()
    size(600,400)
    frameRate(10) # processing problem with 2d graphics
    create_apple()

def draw():
    # processing func runs as a loop
    background(0,0,0) #rgb
    show_apples()
    snake.show()
    snake.move(1)
    snake.detect_wall(PVector(600,400))
    if snake.eat_apple(list_apples[0]):
        list_apples.pop(0)
        create_apple()


# Capture keyboard arrow keys

def keyPressed():
    if key == CODED:
        if keyCode == UP:
            snake.move_up()
        if keyCode == DOWN:
            snake.move_down()
        if keyCode == LEFT:
            snake.move_left()
        if keyCode == RIGHT:
            snake.move_right()

def create_apple():
    new_apple = Apple(PVector(int(random(0,600)), int(random(0,400))))
    list_apples.append(new_apple)

def show_apples():
    for a in list_apples:
        a.show()

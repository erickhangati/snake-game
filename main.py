from turtle import Turtle, Screen
from time import sleep

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize coordinates
x = 0
y = 0

snake = []


def build_snake():
    """
    Build the snake
    :return: None
    """

    s = Turtle()
    s.color("white")
    s.shape("square")
    s.shapesize(0.5)
    s.penup()
    s.setpos(x, y)
    snake.append(s)


for _ in range(3):
    build_snake()
    x -= 10

game_on = True
while game_on:
    screen.update()
    sleep(1)

    for i in range(len(snake) - 1, 0, -1):
        new_x = snake[i - 1].xcor()
        new_y = snake[i - 1].ycor()
        snake[i].goto(new_x, new_y)

    snake[0].forward(10)

# Stop screen from disappearing
screen.exitonclick()

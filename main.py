from turtle import Turtle, Screen

snake = []

# Initialize coordinates
x = 0
y = 0


def build_snake():
    """
    Build the snake
    :return: None
    """

    s = Turtle()
    s.color("white")
    s.shape("square")
    s.setpos(x, y)
    s.penup()
    snake.append(s)


for _ in range(3):
    build_snake()
    x -= 20

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Stop screen from disappearing
screen.exitonclick()

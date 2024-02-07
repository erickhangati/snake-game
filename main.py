from turtle import Screen
from time import sleep
from snake import Snake

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create snake instance
snake = Snake()

game_on = True
while game_on:
    # Update the snake movement on screen
    screen.update()
    sleep(1)

    # Move forwards
    snake.move()

# Stop screen from disappearing
screen.exitonclick()

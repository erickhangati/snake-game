from turtle import Screen
from time import sleep
from snake import Snake
from food import Food

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

# Create snake instance
snake = Snake()

# Food setup
food = Food()

# Listen to keystrokes
screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

game_on = True
while game_on:
    # Update the snake movement on screen
    screen.update()
    sleep(0.25)

    # Move forwards
    snake.move()

# Stop screen from disappearing
screen.exitonclick()

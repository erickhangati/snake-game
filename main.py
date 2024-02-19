from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

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

# Scoreboard
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 10:
        food.position_food()
        snake.create_segment()
        scoreboard.update_scores()

    # Detect collision with wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 280 or snake.head.ycor() <= -300:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset_score()
            snake.reset_snake()

# Stop screen from disappearing
screen.exitonclick()

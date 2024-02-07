from turtle import Turtle


class Snake:
    def __init__(self):
        self.s = None
        self.x = 0
        self.y = 0
        self.snake = []
        self.initialize_snake()

    def build_snake(self):
        """
        Build the snake
        :return: None
        """
        self.s = Turtle()
        self.s.color("white")
        self.s.shape("square")
        self.s.shapesize(0.5)
        self.s.penup()
        self.s.setpos(self.x, self.y)
        self.snake.append(self.s)

    def initialize_snake(self):
        """
        Initialize the starting snake
        :return: None
        """
        # Loop through to build snake with three segments
        for _ in range(3):
            self.build_snake()
            self.x -= 10

    def move(self):
        """
        Move the snake forwards
        :return: None
        """
        for i in range(len(self.snake) - 1, 0, -1):
            # Get previous segment position and move
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)

        # Move forwards
        self.snake[0].forward(10)

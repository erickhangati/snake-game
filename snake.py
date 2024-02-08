from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.s = None
        self.x = 0
        self.y = 0
        self.snake = []
        self.initialize_snake()

    def create_segment(self):
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
            self.create_segment()
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

    def turn_up(self):
        """
        Turn snake to head north.
        :return: None
        """
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def turn_down(self):
        """
        Turn snake to head north.
        :return: None
        """
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def turn_left(self):
        """
        Turn snake to head west.
        :return: None
        """
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def turn_right(self):
        """
        Turn snake to head east.
        :return: None
        """
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

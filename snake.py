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
        self.head = None
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
            self.head = self.snake[0]
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
        self.head.forward(10)

    def turn_up(self):
        """
        Turn snake to head north.
        :return: None
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        """
        Turn snake to head north.
        :return: None
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        """
        Turn snake to head west.
        :return: None
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        """
        Turn snake to head east.
        :return: None
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        """
        Reset snake to its starting size.
        :return: None
        """
        for i in range(len(self.snake)):
            if i > 2:
                self.snake[i].goto(1000, 1000)
        self.snake = self.snake[:3]
        self.head.goto(0, 0)

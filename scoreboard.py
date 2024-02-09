from turtle import Turtle


class Scoreboard(Turtle):
    scores = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 280)
        self.color("white")
        self.display_score()

    def display_score(self):
        """
        Display contact on screen
        :return: None
        """
        self.write(f"Scoreboard: {self.scores}", font=('Courier', 12, "normal"), align="center")

    def update_scores(self):
        """
        Update score after contact with food
        :return: None
        """
        self.clear()
        self.scores += 1
        self.display_score()


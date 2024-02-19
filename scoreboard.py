from turtle import Turtle


class Scoreboard(Turtle):
    scores = 0
    high_score = 0

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
        self.write(f"Score: {self.scores} | High Score: {self.high_score}", font=('Courier', 12, "normal"), align="center")

    def update_scores(self):
        """
        Update score after contact with food
        :return: None
        """
        self.clear()
        self.scores += 1
        self.display_score()

    def reset_score(self):
        if self.scores > self.high_score:
            self.high_score = self.scores

        self.clear()
        self.scores = 0
        self.display_score()

    def game_over(self):
        """
        Display GAME OVER
        :return:
        """
        self.goto(0, 0)
        self.write(f"GAME OVER", font=('Courier', 12, "normal"), align="center")


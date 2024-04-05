from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0

        with open("data.txt") as file:
            self.highscore = int(file.read())

        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # should probably be constants, am lazy
        self.write(f"Score: {self.score} | High Score: {self.highscore}", move=False, align='center',
                   font=('Comic Sans', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")

        self.score = 0
        self.update_scoreboard()



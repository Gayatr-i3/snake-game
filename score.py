from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
             self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Courier",20,"normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode ="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
    #def game_over(self):
    #    self.goto(0,0)
    #   self.write("Game Over", align="center", font=("Courier", 20, "normal"))
    def increase_score(self):
        self.score+=1
        self.update_score()
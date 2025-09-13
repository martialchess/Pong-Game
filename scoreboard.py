# Create a new Scoreboard class, inherits from turtle class. Track and Display score. 

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(self.score, align = ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self, winner):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER\n{winner} Wins!", align="center", font=("Courier", 30, "bold"))

class Divider(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, -300)
        self.setheading(90) # face upward
        self.draw_line()

    def draw_line(self):
        for _ in range(30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    
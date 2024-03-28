from turtle import Turtle
LOCATION = (0, 260)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
COLOR = "black"


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(LOCATION)
        self.color(COLOR)
        self.level = 1
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

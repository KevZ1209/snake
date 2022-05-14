from turtle import Turtle

BIG_FONT = ("Courier", 36, "normal")
SMALL_FONT = ("Courier", 16, "normal")


class Title(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 340)
        self.write("SNAKE", font=BIG_FONT, align="center")
        self.goto(0, 310)
        self.write("USE WASD TO MOVE", font=SMALL_FONT, align="center")

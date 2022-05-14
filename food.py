from turtle import Turtle
import random


# Food class inherits from Turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(self.colors))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(self.colors))
        random_x = -280 + 20 * random.randint(0, 28)
        random_y = -280 + 20 * random.randint(0, 28)
        self.goto(random_x, random_y)

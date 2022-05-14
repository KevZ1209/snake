from turtle import Turtle


def create_boundary():
    t = Turtle()
    t.color("white")
    t.hideturtle()
    t.speed("fastest")
    t.penup()
    t.goto(-290, 290)
    t.pendown()

    for _ in range(4):
        t.forward(580)
        t.right(90)


class Boundary:
    def __init__(self):
        create_boundary()

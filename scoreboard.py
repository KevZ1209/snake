from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
ABS_FILE_LOCATION = "/Users/kevinzhang/PycharmProjects/snake_game/data.txt"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")

        # initialise high score variable
        with open(ABS_FILE_LOCATION) as file:
            self.high_score = int(file.read())

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            # write high score to data.txt
            with open(ABS_FILE_LOCATION, mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

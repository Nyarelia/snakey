from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        # some shrinkage for the food
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("white")
        self.speed("fastest")
        # plob the first piece of candy
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

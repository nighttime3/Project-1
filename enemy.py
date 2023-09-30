from turtle import Turtle
from random import randint, randrange, uniform, choice

class Enemy(Turtle):
    def __init__(self, width, height, difficulty):
        super().__init__()
        self.difficulty = difficulty
        self.speed(
            choice(["slow", "slowest"])
        )
        self.setheading(randint(0, 360))
        self.shape('circle')
        self.color(
            'darkgrey',
            (uniform(0, 1), uniform(0,1), uniform(0, 1))
        )
        self.penup()
        self.goto(
            randrange(-width/2, width/2),
            randrange(-height/2 + 80, height/2),
        )
        self.width = width
        self.height = height
    
    def move(self):
        if self.xcor() > self.width/2 \
                or self.xcor() < -self.width/2:
            self.setheading(-self.heading() + 180)
        if self.ycor() > self.height/2 \
                or self.ycor() < -self.height/2:
            self.setheading(-self.heading())
        self.forward(self.difficulty)
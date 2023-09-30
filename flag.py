from turtle import Turtle, register_shape
from random import randrange

class Flag(Turtle):
    def __init__(self, width=800, height=400):
        super().__init__()
        shape = ((0, 0)), (0, 20), (15, 15), (0, 8)
        register_shape('flag', shape)
        self.setheading(90)
        self.shapesize(2, 2, 2)
        self.color('white', 'blue')
        self.penup()
        self.goto(
            randrange(-width/2 + 20, width/2 - 20),
            randrange(-height/2 + 20, height/2 - 100)
        )

        
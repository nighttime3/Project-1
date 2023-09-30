from turtle import Turtle

class Player(Turtle):
    def __init__(self, width=800, height=400, life=50):
        super().__init__()
        self.shape('turtle')
        self.shapesize(2, 2, 2)
        self.setheading(90)
        self.width = width
        self.height = height
        self.color('red')
        self.speed('fastest')
        self.penup()
        self.goto(0, -height/2 + 20)
        self.life = life

    def decrease_life(self):
        self.life -= 1
    
    def move_up(self):
        if self.ycor() < self.height/2 - 20:
            self.setheading(90)
            self.goto(self.xcor(), self.ycor() + 20)
            self.decrease_life()

    def move_down(self):
        if self.ycor() > -self.height/2 + 20:
            self.setheading(270)
            self.goto(self.xcor(), self.ycor() - 20)
            self.decrease_life()

    def move_left(self):
        if self.xcor() > -self.width/2 + 20:
            self.setheading(180)
            self.goto(self.xcor() - 20, self.ycor())
            self.decrease_life()

    def move_right(self):
        if self.xcor() < self.width/2 - 20:
            self.setheading(0)
            self.goto(self.xcor() + 20, self.ycor())
            self.decrease_life()

    def next_level(self, next_level_life):
        self.setheading(90)
        self.goto(0, -self.height/2 + 20)
        self.life = next_level_life

    
from turtle import Turtle
import settings

class Board(Turtle):
    def __init__(
            self,
            message='', position=(0, 0),
            align='center', color='white'
    ):
        super().__init__()

        self.penup()
        self.message = message
        self.position = position
        self.goto(self.position)
        self.align = align
        self.color(color)
        self.update_message()
        self.hideturtle()

    def update_message(self):
        self.clear()
        self.write(f'{self.message}', align=f'{self.align}', font=settings.FONT)
    
    def set_message(self, updated_message):
        self.message = updated_message
        self.update_message()

    def set_position(self, updated_position):
        self.position = updated_position

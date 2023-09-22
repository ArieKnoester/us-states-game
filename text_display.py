from turtle import Turtle


class TextDisplay(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def display_state_name(self, state_to_display):
        name = state_to_display.state.item()
        xcor = float(state_to_display.x.item())
        ycor = float(state_to_display.y.item())
        self.goto((xcor, ycor))
        self.write(name, align="center")

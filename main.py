import turtle
import pandas
from text_display import TextDisplay


def initialize_screen():
    new_screen = turtle.Screen()
    new_screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    new_screen.addshape(image)
    turtle.shape(image)
    new_screen.setup(width=750, height=500)
    return new_screen


states = pandas.read_csv("50_states.csv")
screen = initialize_screen()
correct_states = []
number_correct = 0
text_display = TextDisplay()

while number_correct < 50:

    user_input = turtle.textinput(title=f"{number_correct}/50 States Correct", prompt="Enter a state name.")
    if user_input:
        user_input = user_input.title()
    # User hits Cancel
    else:
        break

    if user_input in states["state"].values:
        state = states[states.state == user_input]
        state_name = state.state.item()
        if state_name not in correct_states:
            correct_states.append(state_name)
            number_correct = len(correct_states)
            text_display.display_state_name(state_to_display=state)

turtle.mainloop()

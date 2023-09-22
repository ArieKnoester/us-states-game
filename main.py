import turtle
import pandas
from text_display import TextDisplay


def initialize_screen():
    new_screen = turtle.Screen()
    new_screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    new_screen.addshape(image)
    turtle.shape(image)
    return new_screen


state_locations = pandas.read_csv("50_states.csv")
screen = initialize_screen()
correct_guesses = []
text_display = TextDisplay()

# TODO: refactor so that I'm not calling len(correct_guesses) multiple times.
while len(correct_guesses) < 50:

    num_correct = len(correct_guesses)
    user_input = turtle.textinput(title=f"{num_correct}/50 States Correct", prompt="Enter a state name.")
    if user_input:
        user_input = user_input.title()
        print(user_input)
    # User hits Cancel
    else:
        break

    if user_input in state_locations["state"].values:
        state_entered = state_locations[state_locations.state == user_input]
        print(state_entered)


turtle.mainloop()

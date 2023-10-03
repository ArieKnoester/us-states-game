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


all_states = pandas.read_csv("50_states.csv")
screen = initialize_screen()
correct_states = []
number_correct = 0
text_display = TextDisplay()

while number_correct < 50:

    user_input = turtle.textinput(title=f"{number_correct}/50 States Correct", prompt="Enter a state name.")
    if user_input:
        user_input = user_input.title()
    # User clicks Cancel
    else:
        break

    if user_input in all_states["state"].values:
        user_state = all_states[all_states.state == user_input]
        print(user_state)
        state_name = user_state.state.item()
        if state_name not in correct_states:
            correct_states.append(state_name)
            number_correct = len(correct_states)
            text_display.display_state_name(state_to_display=user_state)

# If the player quits before guessing all 50 states (clicks the 'Cancel' button),
# write the missing states to a file.
if number_correct < 50:
    missing_states = list(set(all_states.state).difference(correct_states))
    states_missed_df = pandas.DataFrame(data={"States Missed": missing_states})
    states_missed_df.to_csv("./states_missed.csv", sep=',', index=False)

    # Writing the missing state names to a .csv file was a requirement for this exercise.
    # While I understand this was intended to reinforce writing to a file with Pandas,
    # I feel a better way to give the player feedback is to display them on the map in red.
    text_display.display_missing_states(all_states, missing_states)

turtle.mainloop()
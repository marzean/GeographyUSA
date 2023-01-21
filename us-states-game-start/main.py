import turtle
import pandas

"""Setting up the screen, with a image of 50 states in USA"""
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

"""getting the state names from the data frame"""
data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()


guess_list = []
correct_list = []
while len(guess_list) < 50:
    """checking if the answer state is in the list"""
    answer_state = screen.textinput(title=f"{len(guess_list)}/50", prompt="What is your guess? "
                                                                          "\n Write the first letter in capital.")
    guess_list.append(answer_state)
    """if the user wants to exit"""
    if answer_state == "Exit":
        missing_states = [state for state in list_of_states if state not in correct_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    """if the user answering correctly, the showing the location of the state in the map"""
    if answer_state in list_of_states:
        state_location = turtle.Turtle()
        state_location.hideturtle()
        state_location.penup()
        state_data = data[data.state == answer_state]
        state_location.goto(int(state_data.x), int(state_data.y))
        state_location.write(answer_state)
        correct_list.append(answer_state)
    else:
        print("not in the list")

"""Create a new list of all the missed list, to learn again"""
missed_states = set(list_of_states).difference(set(correct_list))
print(f"You need to learn about these states: {missed_states}.")
screen.exitonclick()


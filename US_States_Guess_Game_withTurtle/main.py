import turtle
import pandas

FONT = ("Courier", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
score = 0
print_states = turtle.Turtle()
print_states.color("black")
print_states.penup()
print_states.hideturtle()

answer_record = []


def print_state(answer):
    state_info = data[data.state == answer]
    print_states.goto(int(state_info.x.item()), int(state_info.y.item()))
    print_states.write(answer)


while len(answer_record) < 50:
    answer_state = turtle.textinput(title=f"{score}/50 States Correct", prompt="What another state's name")
    if answer_state == "Exit":
        missing_state = [state for state in states if state not in answer_record]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_missing.csv")
        break
    if answer_state in states and answer_state not in answer_record:
        score += 1
        answer_record.append(answer_state)
        print_state(answer_state)


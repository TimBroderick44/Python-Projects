import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = turtle.Turtle()
answer.hideturtle()
answer.penup()

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
coords = list(zip(data["x"].to_list(), data["y"].to_list()))
country_dictionary = dict(zip(states, coords))

guessed = []

while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What's another states name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        answer.goto(country_dictionary[answer_state])
        answer.write(answer_state)
        guessed.append(answer_state)

answer.goto(0,240)
answer.write("You got them all! Well Done!", align="center", font=("Verdana", 24, "normal"))

screen.exitonclick()
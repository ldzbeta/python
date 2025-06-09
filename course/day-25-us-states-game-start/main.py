import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text = turtle.Turtle()
text.hideturtle()
text.penup()

data = pandas.read_csv("50_states.csv")
correct=0
is_game_on = True

while is_game_on:
    choice = screen.textinput(f"{correct}/50 states","Which state you know?").title()
    print(type(data[choice==data.state]))
    if choice in data.state.to_list():
        coordinates = data[data.state == choice].iloc[0]
        text.goto(coordinates.x, coordinates.y)
        text.write(f"{choice}")
        correct+=1
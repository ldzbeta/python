from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
# using width= arg is called key word argument where normal general putting of argument is called positional argument , where argument evaluated based on positon of argument

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")
# taking input from new window
start =-70
colors = ["red","blue","yellow","orange","green","purple"]
all_turtles = []
for item in colors:
    t = Turtle(shape="turtle")
    t.color(item)
    t.penup()
    t.goto(x=-230,y=start)
    start+=30
    all_turtles.append(t)

is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
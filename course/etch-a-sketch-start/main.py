from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
    
def move_back():
    tim.back(10)

def rotate_clk():
    tim.setheading(tim.heading()+10)

def rotate_aclk():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()
    
screen.listen()
# onkey - as event listener to execute that function when key is triggered
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=rotate_clk)
screen.onkey(key="d", fun=rotate_aclk)
screen.onkey(clear,"c")
screen.exitonclick()

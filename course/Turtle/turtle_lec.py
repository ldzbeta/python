from turtle import Turtle,Screen

# from turtle module import Turtle class other wise use turtle.Turtle()
timmy = Turtle()
# accessing turtle object

print(timmy)
# printing the object not the turtle, details shown in terminal
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
timmy.left(90)

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
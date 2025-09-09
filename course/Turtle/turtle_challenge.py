from turtle import Turtle,Screen
import random
t = Turtle()
t.screen.colormode(255)  # Set color mode to accept 0-255 RGB values
# or "turtle.colormode(255)" - changing for module not for object

def random_color(self):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    self.color(r, g, b)
    

# draw form triangle to decogan
# for side in range(3,10):
#     random_color(t)
#     for _ in range(side):
#         t.forward(50)
#         t.left(360/side)

# - Graph of random directional movement
# direction = [0,90,180,270]
t.pensize(5)
t.speed("fastest")
# for _ in range(0,20):
#     random_color(t)
#     t.setheading(random.choice(direction)) 
#     # rotate to that taken angle 
#     t.forward(50)

# -Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        random_color(t)
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)
        # t.heading()returns current angle of the cursor and set it adding by degree we want to tilt

draw_spirograph(10)

myScreen = Screen()
myScreen.exitonclick()
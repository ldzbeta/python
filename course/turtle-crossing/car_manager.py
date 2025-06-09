from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10

class CarManager:
    STARTING_MOVE_DISTANCE = 5
    def __init__(self):
        self.cars = []
        for _ in range(random.randint(5,10)):
            self.create_car()
            self.move()
    
    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.goto(200+random.randint(0,250), random.randint(-250, 250))
        self.cars.append(new_car)
        
    def move(self):
        for car in self.cars:
            car.backward(CarManager.STARTING_MOVE_DISTANCE)
            
        if random.randint(1,5)==1:
            self.create_car()
            
    def check_hit(self,x,y):
        for car in self.cars:
            if abs(car.xcor()-x) <= 10 and abs(car.ycor()-y) <= 5:
                # distance less than 20 hit
                return True
            
        return False
    
    def reset(self):
        CarManager.STARTING_MOVE_DISTANCE += MOVE_INCREMENT/5
        # Hide and clear existing cars
        # for car in self.cars:
        #     car.hideturtle()
        #     car.clear()
        
        # # Reset the cars list and create new cars
        # self.cars = []
        # for _ in range(random.randint(0,10)):
        #     self.create_car()
        #     self.move()
    
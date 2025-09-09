import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

new_player = Player()
car_manager = CarManager()
score_board = Scoreboard()
screen.listen()
screen.onkeypress(new_player.move,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    if car_manager.check_hit(new_player.xcor(),new_player.ycor()):
        score_board.game_over()
        game_is_on = False
    elif new_player.check_win():
        score_board.increase_score()
        car_manager.reset()

screen.exitonclick()
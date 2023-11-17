from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BACK_GROUND_COLOR = "Black"
SCREEN_TITLE = "SNAKE GAME"

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BACK_GROUND_COLOR)
screen.tracer(0)
screen.title(SCREEN_TITLE)

snake = Snake()
food = Food()
score_board = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.update_score()
        snake.extend()

    # detect collisions with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # detect collisions with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
screen.exitonclick()

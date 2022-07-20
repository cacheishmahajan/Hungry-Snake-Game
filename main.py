from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

scoreboard = ScoreBoard()
scoreboard.update_score()

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.turtles[0].distance(food) < 15:
        food.random_position()
        scoreboard.score += 1
        scoreboard.update_score()
        snake.extend_snake()

    # detect collision with wall
    if snake.turtles[0].xcor() > 295 or snake.turtles[0].xcor() < -295 or snake.turtles[0].ycor() > 295 or \
            snake.turtles[0].ycor() < -295:

        scoreboard.game_start_over()
        snake.reset_snake()
        food.reset_food()
        continue

    # detect collision with tail
    for segment in snake.turtles[1:]:
        if snake.turtles[0].distance(segment) < 15:

            scoreboard.game_start_over()
            snake.reset_snake()
            food.reset_food()
            continue

screen.exitonclick()

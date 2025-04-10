from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
# segments = []
# for i in range(3):
#     snake_block = Turtle()
#     snake_block.shape("square")
#     snake_block.color("white")
#     snake_block.penup()
#     segments.append(snake_block)
# x = -20
# for t in segments:
#     t.goto(x,0)
#     x+=20
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg_no in range(len(segments)-1,0,-1):
    #     new_x = segments[seg_no-1].xcor()
    #     new_y = segments[seg_no-1].ycor()
    #     segments[seg_no].goto(new_x,new_y)
    # segments[0].forward(20)
    snake.Move()




screen.exitonclick()
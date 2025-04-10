from turtle import Turtle
MOVE_DISTANCE = 25
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        for i in range(3):
            snake_block = Turtle()
            snake_block.shape("square")
            snake_block.color("white")
            snake_block.penup()
            self.segments.append(snake_block)
        x = -20
        for seg in self.segments:
            seg.goto(x,0)
            x+=20


    def Move(self):
        for seg_no in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_no-1].xcor()
            new_y = self.segments[seg_no-1].ycor()
            self.segments[seg_no].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
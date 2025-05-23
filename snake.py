from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)
    def add_segments(self, position):
        snake_block = Turtle()
        snake_block.shape("square")
        snake_block.color("white")
        snake_block.penup()
        snake_block.goto(position)
        self.segments.append(snake_block)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    def extend(self):
        self.add_segments(self.segments[-1].position())


    def Move(self):
        for seg_no in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_no-1].xcor()
            new_y = self.segments[seg_no-1].ycor()
            self.segments[seg_no].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
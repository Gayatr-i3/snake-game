from turtle import Turtle
positions = [(0, 0), (-20, 0), (-40, 0)]
m = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]
    def create_snake(self):
        for i in positions:
            self.add_seg(i)
    def add_seg(self, i):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(i)
        self.seg.append(new_seg)

    def reset(self):
        for i in self.seg:
            i.goto(1000, 1000)
        self.seg.clear()
        self.create_snake()
        self.head = self.seg
    def extend(self):
        self.add_seg(self.seg[-1].position())

    def move(self):
        for j in range(len(self.seg) - 1, 0, -1):
            x = self.seg[j - 1].xcor()
            y = self.seg[j - 1].ycor()
            self.seg[j].goto(x, y)
        self.seg[0].forward(m)

    def up(self):
        if self.head.heading() != DOWN:
            self.seg[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.seg[0].setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.seg[0].setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.seg[0].setheading(RIGHT)

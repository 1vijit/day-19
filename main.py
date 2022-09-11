import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.bk(10)

def move_counterclockwise() :
    new_heading=tim.heading() - 10
    tim.setheading(new_heading)

def move_clockwise():
    new_heading=tim.heading() + 10
    tim.setheading(new_heading)


def clear_drawing() :
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
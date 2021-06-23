from turtle import Turtle, Screen

mint = Turtle()
screen = Screen()


def move_forwards():
    mint.forward(10)


def move_backwards():
    mint.backward(10)


def turn_left():
    new_heading = mint.heading() + 10
    mint.setheading(new_heading)


def turn_right():
    new_heading = mint.heading() - 10
    mint.setheading(new_heading)


def clear():
    mint.clear()
    mint.penup()
    mint.home()
    mint.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()

import turtle
w=turtle.Turtle()
w.penup()
w.goto(400,-280)
w.pendown()
w.fillcolor("powder blue")
w.begin_fill()
w.setheading(270)
w.forward(85)
w.setheading(180)
w.forward(800)
w.setheading(90)
w.forward(85)
w.setheading(0)
for x in range(60):
    w.right(45)
    w.forward(50)
    w.left(105)
    w.forward(50)
    w.setheading(0)
w.end_fill()

#
# turtle.penup()
# turtle.goto(200,0)
# turtle.pendown()
# turtle.setheading(270)
# turtle.fillcolor("powder blue")
# turtle.begin_fill()
# for x in range(3):
#     turtle.forward(400)
#     turtle.right(90)
#
# turtle.right(45)
# turtle.forward(50)
# turtle.left(105)
# turtle.forward(50)
# turtle.setheading(0)
# turtle.right(45)
# turtle.forward(50)
# turtle.left(105)
# turtle.forward(50)
# turtle.setheading(0)


# turtle.right(105)
# turtle.forward(50)
# turtle.left(105)
# turtle.forward(50)
# turtle.left(-105)
# turtle.forward(50)
# turtle.right(-105)
# turtle.forward(50)
# turtle.left(-105)
# turtle.forward(50)
# turtle.setheading(0)
# turtle.forward(100)
#
# turtle.end_fill()
turtle.done()

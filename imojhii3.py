import turtle

t = turtle.Turtle()
t.speed(1)
t.begin_fill()
t.width(5)
t.circle(80)
t.fillcolor("yellow")
t.color("pink")
t.end_fill()



t.begin_fill()
t.fillcolor("black")
t.up()
t.goto(40, 80)
t.down()
t.circle(20)
t.end_fill()


t.begin_fill()
t.fillcolor("white")
t.up()
t.goto(40, 85)
t.down()
t.circle(10)
t.end_fill()

t.begin_fill()
t.fillcolor("black")
t.up()
t.goto(-40, 80)
t.down()
t.circle(20)
t.end_fill()

t.begin_fill()
t.fillcolor("white")
t.up()
t.goto(-40, 85)
t.down()
t.circle(10)
t.end_fill()

t.up()
t.goto(-32, 40)
t.down()
t.color("red")
t.width(6)
t.right(9)
t.forward(20)
t.left(9)
t.forward(20)
t.left(9)
t.forward(20)
t.hideturtle()
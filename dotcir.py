import turtle
t = turtle.Turtle()
h = turtle.Turtle()
wn =turtle.Screen()
co=["green","orange","blue","yellow","red"]

t.speed(300)
t.begin_fill()
t.color("yellow")
for i in range(200):
    wn.bgcolor(co[i%5])
    t.goto(0,0)
    #t.tilt(90)
    t.dot()
    t.forward(180-i/2)
    t.left(19)
    #t.circle(i%120,steps=5) #(10+i)%70)
    t.width(5-i%4)
    t.color(co[i%2])
    t.end_fill()
    t.hideturtle()


h.speed(300)
h.begin_fill()
h.color("yellow")
for i in range(200):
    wn.bgcolor(co[i%5])
    h.goto(0,0)
    #t.tilt(90)
    h.dot()
    h.forward(180-i/2)
    h.right(19)
    #t.circle(i%120,steps=5) #(10+i)%70)
    h.width(5-i%4)
    h.color(co[i%2])
    h.end_fill()
    h.hideturtle()

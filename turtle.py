import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.width(2)
t.speed(25)

col = ('#00e700','#e70000','#000080')
for i in range(1000):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)
    
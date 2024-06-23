import turtle
import turtle as t
import colorsys as c
t.bgcolor("black")
t.tracer(100)
t.pensize(4)
h=0
for i in range(2000):
    color=c.hsv_to_rgb(h,1,1)
    h+=0.01
    t.fillcolor(color)
    t.pencolor('black')
    t.begin_fill()
    t.fd(i)
    t.rt(67)
    t.fd(i)
    t.circle(i,30)
    t.fd(i)
    t.lt(190)
    for i in range(20):
        t.fd(i)
        t.rt(90)
        t.circle(i,10)
        t.fd(i)
        t.rt(30)
        t.fd(i)
        t.rt(90)
        t.end_fill()
        t.done()
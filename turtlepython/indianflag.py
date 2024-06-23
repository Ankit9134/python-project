#import turtle  
import turtle  
from turtle import *  
  
screen = turtle.Screen()  
# Defining a turtle Instance  
t = turtle.Turtle()  
speed(10)  
# Orange Rectangle  
#white rectangle  
def draw_orange_rectangle():  
    # initially penup()  
    t.penup()  
    t.goto(-200, 125)  
    t.pendown()  
  
    t.color("orange")  
    t.begin_fill()  
    t.forward(400)  
    t.right(90)  
    t.forward(84)  
    t.right(90)  
    t.forward(400)  
    t.end_fill()  
    t.left(90)  
    t.forward(84)  
  
# Draw Green Rectangle  
def draw_green_rectangle():  
    t.color("green")  
    t.begin_fill()  
    t.forward(84)  
    t.left(90)  
    t.forward(400)  
    t.left(90)  
    t.forward(84)  
    t.end_fill()  
  
# Big Blue Circle  
def big_blue_circle():  
    t.penup()  
    t.goto(35, 0)  
    t.pendown()  
    t.color("navy")  
    t.begin_fill()  
    t.circle(35)  
    t.end_fill()  
  
# Big White Circle  
def big_white_circle():  
    t.penup()  
    t.goto(30, 0)  
    t.pendown()  
    t.color("white")  
    t.begin_fill()  
    t.circle(30)  
    t.end_fill()  
  
#Mini Blue Circles of Flag  
def mini_blue():  
    t.penup()  
    t.goto(-27, -4)  
    t.pendown()  
    t.color("navy")  
    for i in range(24):  
        t.begin_fill()  
        t.circle(2)  
        t.end_fill()  
        t.penup()  
        t.forward(7)  
        t.right(15)  
        t.pendown()  
  
# Small Blue Circle  
def draw_small_blue_circle():  
    t.color("navy")  
    t.penup()  
    t.goto(10, 0)  
    t.pendown()  
    t.begin_fill()  
    t.circle(10)  
    t.end_fill()  
  
#The spokes of India Flag  
def flag_spokes():  
    t.penup()  
    t.goto(0, 0)  
    t.pendown()  
    t.pensize(1)  
    for i in range(24):  
        t.forward(30)  
        t.backward(30)  
        t.left(15)  
  
#for stick of the flag  
def flag_stick():  
    t.color("Brown")  
    t.pensize(10)  
    t.penup()  
    t.goto(-200,125)  
    t.right(180)  
    t.pendown()  
    t.forward(800)  
  
draw_orange_rectangle()  
draw_green_rectangle()  
big_blue_circle()  
big_white_circle()  
mini_blue()  
draw_small_blue_circle()  
flag_spokes()  
flag_stick()  
  
turtle.done()  

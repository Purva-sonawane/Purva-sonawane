import turtle
import math
  
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()
  
screen = turtle.Screen ( )
screen.bgcolor("skyblue")
  
tip = turtle.Turtle()
tip.color ("black")
tip.shape ("turtle")
tip.speed (2)
  
tip.penup()
tip.goto(100, -130)
tip.pendown()
drawRectangle(tip, 20, 40, "brown")
  
tip.penup()
tip.goto(65, -90)
tip.pendown()
drawTriangle(tip, 100, "green")
tip.penup()
tip.goto(70, -45)
tip.pendown()
drawTriangle(tip, 90, "green")
tip.penup()
tip.goto(75, -5)
tip.pendown()
drawTriangle(tip, 80, "green")

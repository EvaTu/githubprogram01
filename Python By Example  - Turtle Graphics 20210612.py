# Chapter 8 - Turtle Graphics
# Challenge 060
'''
import turtle

turtle.shape("turtle")
turtle.speed(1)
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()
'''
# Challenge 061
'''
import turtle
turtle.shape("turtle")
turtle.speed(1)
for i in range(0,3):
    turtle.left(120)
    turtle.forward(200)
turtle.exitonclick()
'''
# Challenge 062
'''
import turtle

turtle.shape("turtle")
for i in range(0,360):
    turtle.left(1)
    turtle.forward(2)

turtle.exitonclick()
'''
# Challenge 063
'''
import turtle

turtle.shape("turtle")
turtle.begin_fill()
turtle.color("pink")
for i in range(0,3):
    turtle.left(120)
    turtle.forward(200)
turtle.end_fill()
turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.begin_fill()
turtle.color("orange")
for i in range(0,3):
    turtle.left(120)
    turtle.forward(200)
turtle.end_fill()
turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
for i in range(0,3):
    turtle.left(120)
    turtle.forward(200)
turtle.end_fill()
turtle.exitonclick()
'''
# Challenge 064
'''
import turtle

turtle.shape("turtle")
for i in range(0,5):
    turtle.left(144)
    turtle.forward(150)
turtle.exitonclick()
'''
# Challenge 065
'''
import turtle
turtle.shape("turtle")

turtle.left(90)
turtle.forward(300)
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.pendown()

turtle.forward(200)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(200)

turtle.hideturtle()
turtle.exitonclick()
'''
# Challenge 066
'''
import random
import turtle

turtle.pensize(6)

for i in range(0,8):
    r_color = random.choice(["pink","purple","brown","red","green","blue"])
    turtle.color(r_color)
    turtle.left(45)
    turtle.forward(100)
    
turtle.exitonclick()
'''
# Challenge 067
'''
import turtle

for i in range(0,10):
    turtle.left(36)
    for i in range(0,8):
        turtle.right(45)
        turtle.forward(60)

turtle.exitonclick()
'''

# Challenge 068

import random
import turtle

range_num = random.randint(1,10)
for i in range(0,range_num):
    dis_num = random.randint(60,150)
    angle_num = random.randint(60,180)
    turtle.left(angle_num)
    turtle.forward(dis_num)
turtle.exitonclick()





















































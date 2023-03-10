import turtle as t
import random

t.colormode(255)

tim = t.Turtle()

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), 
               (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), 
               (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# print(random_color)
# tim.pencolor()



def go_forward():
    for _ in range(1,10):
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.dot(20,random.choice(color_list))

def go_left():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.dot(20,random.choice(color_list))

def go_right():
    tim.right(90)
    tim.forward(50) 
    tim.right(90)
    tim.dot(20,random.choice(color_list))


for _ in range(1,6):
    go_forward()

    go_left()

    go_forward()

    go_right()

screen = t.Screen()
screen.exitonclick()
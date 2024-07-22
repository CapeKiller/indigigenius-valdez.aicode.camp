import turtle

window = turtle.Screen()
window.setup(width=800, height=800)
window.bgcolor("black")
window.title("Turtle Power")

t = turtle.Turtle()
t.speed(20)

# Challenge 1: Squares in a Grid
# YOUR CODE HERE
t.penup()
t.pencolor("white")
t.setposition(-200, 250)
#t.backward(300)
t.pendown()
for j in range (0,3):
    t.penup()
    for i in range (0,4):
        t.pendown()
        t.forward(100)
        t.left(90)
        t.penup()
    t.penup()
    t.forward(150)

t.setposition(-200, 50)
#t.backward(300)
t.pendown()
for j in range (0,3):
    t.penup()
    for i in range (0,4):
        t.pendown()
        t.forward(100)
        t.left(90)
        t.penup()
    t.penup()
    t.forward(150)

t.setposition(-200, -150)
#t.backward(300)
t.pendown()
for j in range (0,3):
    t.penup()
    for i in range (0,4):
        t.pendown()
        t.forward(100)
        t.left(90)
        t.penup()
    t.penup()
    t.forward(150)


# DON'T TOUCH THIS
turtle.mainloop()


import turtle

window = turtle.Screen()
window.setup(width=800, height=800)
window.bgcolor("black")
window.title("Turtle Power")

t = turtle.Turtle()
t.speed(25)


# Challenge 2: Circles in a Grid with One Missing

# YOUR CODE HERE
t.penup()
t.pencolor("white")
t.setposition(-200, 125)
t.pendown()
t.circle(50)

t.penup()
t.setposition(-50, 125)
t.pendown()
t.circle(50)

t.penup()
t.setposition(100, 125)
t.pendown()
t.circle(50)

t.penup()
t.setposition(-200, 0)
t.pendown()
t.circle(50)

t.penup()
t.setposition(-50, 0)
t.pendown()
t.circle(50)

t.penup()
t.setposition(100, 0)
t.pendown()
t.circle(50)

t.penup()
t.setposition(-50, -125)
t.pendown()
t.circle(50)

t.penup()
t.setposition(100, -125)
t.pendown()
t.circle(50)

t.penup()
t.setposition(-275, 250)
t.pendown()

for j in range (0,4):
    t.forward(450)
    t.right(90)



# DON'T TOUCH THIS
turtle.mainloop()


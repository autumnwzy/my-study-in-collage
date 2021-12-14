import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.right(angle)
            koch(size/3,n-1)

turtle.pencolor("red")
turtle.pensize(5)
size =eval(input())
n = eval(input())
koch(size,n)
turtle.done()
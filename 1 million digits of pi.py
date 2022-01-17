import turtle
import ctypes

breite = ctypes.windll.user32.GetSystemMetrics(0)
hoehe = ctypes.windll.user32.GetSystemMetrics(1)

lines = 100000

with open("1 million digits of pi.txt", "r") as f:
    pi = f.read()

print(len(pi))
print(pi[0:9])
print(pi[-10:-1])

print(breite)
print(hoehe)

turtle.mode("logo")
turtle.tracer(False)
print(turtle.screensize())
turtle.screensize(canvwidth=100, canvheight=100, bg="Black")
turtle.colormode(255)

for n in range(lines):

    color = int(n / (lines / 255))
    turtle.pencolor(255, 255 - color, color)
    zahl = int(pi[n])
    rotation = zahl * 36
    turtle.setheading(rotation)
    turtle.forward(1)
    if n % 10000 == 0:
        turtle.update()

turtle.done()

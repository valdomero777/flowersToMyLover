import turtle
import math

def p_line(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360 / n
    p_line(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    p_line(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle, p):
    for i in range(n):
        petal(t, r, angle)
        t.lt(p/n)

def leaf(t, r, angle, p):
    t.begin_fill()
    t.down()
    flower(t, 1, r, angle, p)
    t.end_fill()

def configurar_ventana():
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Dibujando una flor")

def dibujar_flor():
    lucy = turtle.Turtle()
    lucy.shape("turtle")
    lucy.color("yellow")
    lucy.width(3)

    # Dibujando flor
    flower(lucy, 7, 60, 100, 360)

    # Dibujando pedúnculo
    lucy.color("brown")
    lucy.rt(90)
    lucy.fd(200)

    # Dibujando hoja 1
    lucy.width(1)
    lucy.rt(270)
    lucy.color("green")
    leaf(lucy, 40, 80, 180)
    lucy.rt(140)
    lucy.color("black")
    lucy.fd(30)
    lucy.lt(180)
    lucy.fd(30)

    # Dibujando hoja 2
    lucy.rt(120)
    lucy.color("green")
    leaf(lucy, 40, 80, 180)
    lucy.color("black")
    lucy.rt(140)
    lucy.fd(30)
    lucy.ht() # Esconde la tortuga

def main():
    configurar_ventana()
    dibujar_flor()
    turtle.exitonclick()

main()

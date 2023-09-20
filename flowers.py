import turtle

# Set the title of the Turtle window
turtle.title('Sixteen Petals Flower')

# Set the world coordinates for the Turtle canvas
turtle.setworldcoordinates(-2000,-2000,2000,2000)

# Define a function called "draw_flower" that takes four arguments: x, y, tilt, and radius
def draw_flower(x, y, tilt, radius):
    turtle.fillcolor("yellow")  # Establecer el color de relleno a amarillo
    turtle.begin_fill()        # Comenzar a llenar
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius, 90)
    turtle.left(90)
    turtle.circle(radius, 90)
    turtle.end_fill()          # Terminar de llenar

# Loop through a range of angles from 0 to 360 degrees in steps of 30 degrees
for tilt in range(0, 360, 30):
    draw_flower(0, 0, tilt, 1000)

# Mantener la ventana abierta hasta que se haga clic
turtle.done()

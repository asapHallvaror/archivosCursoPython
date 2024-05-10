import turtle

# Configuración inicial
turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()

# Función para dibujar un círculo
def dibujar_circulo(color, radio, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radio)
    turtle.end_fill()

# Función para dibujar un ojo
def dibujar_ojo(color, radio, x, y):
    dibujar_circulo(color, radio, x, y)

# Función para dibujar el cuerpo
def dibujar_cuerpo():
    dibujar_circulo("red", 50, 0, -50)

# Función para dibujar la visera
def dibujar_visera():
    turtle.penup()
    turtle.goto(0, -30)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color("black", "red")
    turtle.begin_fill()
    turtle.circle(60, 180)
    turtle.end_fill()

# Función para dibujar las patas
def dibujar_patas():
    turtle.penup()
    turtle.goto(30, -90)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.forward(80)
    turtle.penup()
    turtle.goto(-30, -90)
    turtle.pendown()
    turtle.setheading(-135)
    turtle.forward(80)

# Función para dibujar la mochila
def dibujar_mochila():
    turtle.penup()
    turtle.goto(0, 20)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

# Dibujar personaje de Among Us rojo
dibujar_cuerpo()
dibujar_visera()
dibujar_ojo("white", 10, -20, 0)
dibujar_ojo("white", 10, 20, 0)
dibujar_patas()
dibujar_mochila()

# Esconder la ventana al hacer clic
turtle.done()

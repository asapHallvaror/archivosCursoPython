def message():
    print("Ingresar valor: ")

print("Inicia aqui.")
message()
print("Termina aqui.")


#Si necesitamos un mensaje estático podemos escribirlo normalmente, pero si necesitamos 1000 inputs y queremos cambiar el mensaje, es mejor usar una función
"""
def message():
    print("Ingresar valor: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
"""
#Es posible usar parámetros en las funciones
def message(number):
    print("Ingresa un número:", number)
message(1)

#Con dos parámetros
def message(what, number, corte):
    print("Ingresa", what, "número", number, corte)

message("teléfono", 11, "brrrr")
message("precio", 5, "brrrr")
message("número", "number", "brrrr")

#Podemos pasar valores a una función con "="
def presentacion(p_nombre,apellido):
    print("Hola, mi nombre es:",p_nombre,apellido)

presentacion(p_nombre="Joselú", apellido="Belligoat")
presentacion(p_nombre="Travis", apellido="Scott")
presentacion(p_nombre="Crash", apellido="Bandicoot")
presentacion(p_nombre="Tyler", apellido="Okonma")

#Se puede hacer una suma mediante una función
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(5,10,23)

#También se puede hacer que una función tenga un parámetro ya definido
def introduction(first_name, last_name="Morales"):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Álvaro")
introduction("Álvaro", "Pérez") # Se puede cambiar el valor del parámetro definido, pero igual sirve si uno quiere tener un valor definido

#Función con return

def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123

print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")




numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.
 
numbers[0] = 111
numbers[4] = 69420
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

#Un elemento de una lista se puede imprimir facilmente
print(numbers[4])

#Ahora se puede imprimir la longitud de la lista
print("Longitud de la lista:",len(numbers))

#Para eliminar un elemento de una lista hay que usar el comando "del"

del numbers[4]
print("\nLongitud de lista despues de eliminar:",len(numbers))
print(numbers)

#Un elemento con un índice igual a -1 es el último en la lista.
numbers = [69, 420, 555, 777]
print("\n",numbers[-1])

#Del mismo modo, el elemento con un índice igual a -2 es el anterior al último en la lista.
print("\n",numbers[-2])

#Para agregar un elemento al final de una lista, podemos usar el comando "append(valor)"
numbers = [543,556,187,69]
print("\n\n\n\n\n",numbers)
print("Longitud lista actual:",len(numbers))

numbers.append(1000)
print(numbers)
print("Longitud lista actual:",len(numbers))

#Pero si queremos insertar un valor en el lugar que queramos de una lista, debemos usar "insert(lugar de la lista, valor)"
numbers.insert(0,2365)
print(numbers)
print("Longitud lista actual:",len(numbers))

#Podemos agregar elementos a una lista vacia con for de la siguiente manera
lista_linda = []

for i in range(7):
    lista_linda.append(i+1)
print(lista_linda)

#Ahora voy a probar lo mismo pero con insert
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

#Sumar los elementos de una lista se puede hacer facilemente con un for
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print("El total de la suma de los elementos de la lista es:",total)

#Una forma más sencilla de hacer el mismo proceso es usando "in" en vez de "len"
my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)

#Se pueden invertir los elementos de una lista de la siguiente manera
##my_list = [10, 1, 8, 3, 5]
 
##my_list[0], my_list[4] = my_list[4], my_list[0]
##my_list[1], my_list[3] = my_list[3], my_list[1]
 
##print(my_list)

#Pero para hacerlo de una manera más eficiente se puede usar un ciclo for
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)

"""
Nota:

hemos asignado la variable length a la longitud de la lista actual (esto hace que nuestro código sea un poco más claro y más corto)

hemos preparado el bucle for para que se ejecute su cuerpo length // 2 veces (esto funciona bien para listas con longitudes pares e impares, porque cuando la lista 
contiene un número impar de elementos, el del medio permanece intacto)

hemos intercambiado el elemento i (desde el principio de la lista) por el que tiene un índice igual a (length - i - 1) (desde el final de la lista); en nuestro ejemplo, 
for i igual a 0 a la (length - i - 1) da 4; for i igual a 3, da 3 - esto es exactamente lo que necesitábamos.

"""

#Para ordenar los elementos de una lista lo podemos hacer de la siguiente manera
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)

#Comandos in y not in con listas
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#Rebanadas
#Para copiar los elementos de una lista y ponerlos es una nueva:
listapro = [1,2,3,4,5]
listanuv = listapro[:]
print ("Lista nuv:",listanuv)

#Tambien sirve para copiar elementos entre rangos mi_lista(inicio-final)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

#RESUMEN
#Si deseas copiar una lista o parte de la lista, puedes hacerlo haciendo uso de rebanadas:
colors = ['rojo', 'verde', 'naranja']
 
copy_whole_colors = colors[:]  # copia la lista entera
copy_part_colors = colors[0:2]  # copia parte de la lista


#También puede utilizar índices negativos para hacer uso de rebanadas. Por ejemplo:
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # output: ['C', 'D']

# Los parámetros start y end son opcionales al partir en rebanadas una lista: list[start:end], por ejemplo:
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # output: [3, 4, 5]
print(slice_two)  # output: [1, 2]
print(slice_three)  # output: [4, 5]

#Puedes eliminar rebanadas utilizando la instrucción del:
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # output: [3, 4, 5]
 
del my_list[:]
print(my_list)  # elimina el contenido de la lista, genera: []

#Puedes probar si algunos elementos existen en una lista o no utilizando las palabras clave in y not in, por ejemplo:
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # output: True
print("C" not in my_list)  # output: True
print(2 not in my_list)  # output: False



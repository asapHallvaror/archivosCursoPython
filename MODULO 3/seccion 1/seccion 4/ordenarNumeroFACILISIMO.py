lista = []
num = int(input("Ingresar cuantos números deseas ordenar: "))
for x in range(num):
    val = int(input("Ingresa el número: "))
    lista.append(val)

lista.sort()
print("Lista ordenada:",lista)

#Se puede usar sort también para ordenar alfabeticamente
lst = ["D", "F", "A", "Z"]
lst.sort()
 
print(lst)
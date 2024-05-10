# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Paso 2:", beatles)

# paso 3
for x in range(2):
    nuevo = input("Agrega a Stu Sutcliffe y luego a Pete Best: ")
    beatles.append(nuevo)
print("Paso 3:", beatles)

# paso 4
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0,"Ringo Star")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))



blocks = int(input("Ingresa el número de bloques: "))


altura = 0
bloques_utilizados = 0

while bloques_utilizados <= blocks:
    altura += 1
    bloques_utilizados += altura
    if bloques_utilizados > blocks:
        altura -= 1
        break

print("La altura de la pirámide que se puede construir es:", altura)

#
# Escribe tu código aquí.
#	




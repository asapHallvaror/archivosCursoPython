c0 = int(input("Ingrese un número entero positivo distinto de cero: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1

print("Se alcanzó el valor 1 después de", steps, "pasos.")
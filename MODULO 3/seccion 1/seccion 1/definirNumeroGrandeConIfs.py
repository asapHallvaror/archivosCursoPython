num1= int(input("Ingresa el primer número: "))
num2= int(input("Ingresa el segundo número: "))
num3= int(input("Ingresa el  tercer número: "))

numero_grande = num1

if num2>numero_grande:
    numero_grande=num2
    
if num3>numero_grande:
    numero_grande=num3

print("El número más grande es:", numero_grande)
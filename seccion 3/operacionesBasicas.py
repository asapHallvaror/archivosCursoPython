import os
os.system('cls')

print(1+1)      #Suma
print(-2-15)
print(15 - -15)
#--------------------------------------------------------------------------------
print(5-3)      #Resta
#--------------------------------------------------------------------------------
print(10*10)    #Multiplicación
#--------------------------------------------------------------------------------
print(10/5)     #División
print(10//5)    #División con resultado entero
#--------------------------------------------------------------------------------
print(5**2)     #Exponenciación     
print(2 ** 2 ** 3)
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

print(5**2.)    #Exponenciación con decimal
#--------------------------------------------------------------------------------
print(14%4)     #Resto - Esta operación muestra lo que sobra de una división
print(12 % 4.5) #12 // 4.5 da 2.0 / 2.0 * 4.5 da 9.0 / 12 - 9.0 da 3.0 
#--------------------------------------------------------------------------------
print(2 * 3 % 5)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

x = int(input())
y = int(input())
 
x = x % y
x = x % y
y = y % x
 
print(y)

x = input()
y = int(input())
 
print(x * y)

z = y = x = 1
print(x, y, z, sep='*')

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)
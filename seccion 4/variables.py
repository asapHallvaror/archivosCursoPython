import os
os.system('cls')

var = 1

client_balance = 4000000000

client_name = 'Kanye West'

client_balance+=10000000

client_balance*=2

print ('ID CLIENT:',var,'\nCLIENT BALANCE:',client_balance,'\nCLIENT NAME:',client_name,'\n')
#-------------------------------------------------------------------------------------------
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
#-------------------------------------------------------------------------------------------
#Abreviaciones de operaciones con variables
ahorros=100000
#Digamos que deposité $15.000 en una cuenta de ahorro, se puede hacer lo siguiente:
ahorros += 15000
print('Ahorros actuales:',ahorros)
#Ahora digamos que te pusiste compulsivo y gastaste la mitad de tus ahorros un un juego ultra super deluxe:
ahorros //= 2
print('Ahorros actuales:',ahorros)
#Ahora aumentaste tus ahorros! El banco se dio cuenta que eres un genio y te exponenció los ahorros por 2!!
ahorros **= 2
print('Ahorros actuales:',ahorros)

import os
os.system('cls')

#Hay que considerar que una milla equivale a 1.61 kilometros aproximadamente
kilometros = 12.25
millas = 7.38
kmbase = 1.61

millas_a_km = millas * kmbase 
km_a_millas = kilometros / kmbase
print('---------- Super convertidor ----------\n')
print(millas, 'millas equivalen a:', round(millas_a_km,2),'kilometros')
print(kilometros, 'kilometros equivalen a:', round(km_a_millas,2),'millas')
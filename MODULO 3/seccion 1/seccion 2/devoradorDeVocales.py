# Pedir al usuario que ingrese una palabra
user_word = input("Por favor, ingresa una palabra: ")

# Convertir la palabra ingresada a mayúsculas
user_word = user_word.upper()

# Devorar las vocales y imprimir las letras no consumidas
for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        print(letter)


#Ahora lo mismo pero más bonito
word_without_vowels = ""

user_word = input("Ingresa una palabra: ")

user_word = user_word.upper()

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.


for letter in user_word:
    if letter in ['A','E','I','O','U']:
        continue
    else:
        word_without_vowels += letter
    
    # Completa el cuerpo del bucle.

# Imprimir la palabra asignada a word_without_vowels.
print("Palabra sin vocales:", word_without_vowels)

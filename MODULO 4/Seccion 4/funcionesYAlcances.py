#Una función es capaz de reconocer una variable que se crea luego (var)

def my_function():
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)


#De todas formas, respeta el orden de las variables
def my_function():
    var = 2
    print("¿Conozco a la variable?", var)
 
 
var = 1
my_function()
print(var)

#En python hay un comando llamado "global", el cual da la instruccion a una variable para que mantenga el mismo valor tanto dentro como fuera de una función
def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)
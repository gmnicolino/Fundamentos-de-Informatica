# Función Local

def funcion1():
    variable1 = "Variable dentro de la funcion"
    print(variable1)

    def funcion2():
        variable1 = "He cambiado el valor de la funcion"
        print(variable1)

    funcion2()

funcion1()

# Función Global

variable1 = "Variable fuera de la funcion"

def funcion1():
    print(variable1)
funcion1()

#Mix entre función global y local
variable1 = "Variable fuera de la funcion"

def funcion1():
    variable1 = "Variable dentro de la funcion"
    print(variable1)
funcion1()

print(variable1)

#Transformar una variable local en global

def funcion1():
    global num1
    num1 = 10

funcion1()
print(num1)

#Caso de dos variables globales pero una era local y la converti

num1 = 50

def funcion1():
    global num1
    num1 = 10

funcion1()
print(num1)

# Es lo mismo que:
num1 = 50
num1 = 10


def funcion1():
   global num1
   num1 = 10


funcion1()
print(num1)
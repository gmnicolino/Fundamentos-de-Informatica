#Errores que impiden que Python ejecute el codigo

#                   SyntaxError : error de escritura, no cerrar parentesis
#EJEMPLO

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d)/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

#                   Excepciones
#                   NameError: te dice que nombre tiene el error
#                   TypeError: te dice el tipo de error
#                   ZeroDivisionError: una division con 0


# Para continuar con algo ignorando el error hago uso del try (como si fuera un if)


def eneavo(numero):
    try:
        print(1/numero)
    except ZeroDivisionError:
        print("No se puede dividir ese numero", numero)
    except TypeError:
        print("El", numero, "es un string")

    print(numero)

eneavo("9")
eneavo(0)

#OTRO CASO
def check_int_type():
  if type(x)  != int:
    raise TypeError("Only integers are allowed") 
    
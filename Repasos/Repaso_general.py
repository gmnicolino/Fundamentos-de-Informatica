#Definir una función llamada Division Entera que reciba por parametro 3 numeros, A , B y C. Esta función debe sumar A y B y a ese resultado dividirlo de forma entera con C. Este resultado sera retornado y utilizado en la función principal. En el programa principal se pedira esos 3 numeros e  imprimira True si el resultado de la función Division Entera es PAR o NO

# def division_entera(numeroA, numeroB, numeroC):
#     numeroA = int(input("ingrese un numero: "))
#     numeroB = int(input("ingrese un numero: "))
#     numeroC = int(input("ingrese un numero: "))
#     return (numeroA + numeroB) / numeroC %2 == 0

# print(division_entera)

# numeroA = int(input("ingrese un numero: "))
# numeroB = int(input("ingrese un numero: "))
# numeroC = int(input("ingrese un numero: "))
# resultado = (numeroA + numeroB) / numeroC
# def division_entera(numeroA, numeroB, numeroC):
#     return resultado %2 == 0

# print(division_entera(numeroA, numeroB, numeroC))

#En el programa principal, pedir el ingreso de dos floats, sumarlos entre si y dividirlos por 2. Si el resultado es par, se imprime el resultado, sino False.
# numero1 = float(input("ingrese un entero: "))
# numero2 = float(input("ingrese un entero: "))
# cuenta = (numero1 + numero2)/2
# if cuenta %2 == 0:
#     print(cuenta)
# else: 
#     print("False")

#En el programa principal,  pedir el ingreso de dos floats, llamar a una función auxiliar que los recibe por parametros, redondea cada uno de esos numeros y retorna la potencia de la suma entre los dos numeros redondeados. En el programa principal sólo se muestra en pantalla el resultado de esa función auxiliar.
num1 = float(input("ingrese un num: "))
num2 = float(input("ingrese un num: "))
redondeo_num1= round(num1)
redondeo_num2 = round(num2)
def numeros_redondeados(redondeo_num1, redondeo_num2):
    return pow(redondeo_num1 + redondeo_num2, 2)

print(numeros_redondeados(redondeo_num1,redondeo_num2))


#este ultimo me da error cuando pongo dos numeros enteros y tambien si pongo con coma

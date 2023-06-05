# celulares = ["Xiaomi", "Iphone", "Samsung", "Huawei"]

# print(celulares[-2])



# tupla = ("rojo", "amarillo", "azul", "verde")
# lista = list(tupla)

# print(lista)

# celulares = ["Xiaomi", "Iphone", "Samsung", "Huawei"]
# tupla = tuple(celulares)
# print(tupla)

# num1 = 10
# num2 = 20

# if num1 == num2:
#     print(True)
# else:
#     print(False)

# if num1 != num2:
#     print(True)
# else:
#     print(False)

#Otro ejemplo
# entrada = input("introduzca un navegador: \n")

# navegadores = ["chrome", "firefox"]

# if entrada in navegadores:
#     print("esta")
# else:
#     print("no esta")

frase = "Lo que escribas, lo repito: "
frase += "\nIntroduce `salir´ para terminar \n"

mensaje = " "

while mensaje != "salir":
    mensaje = input(frase)
    print(mensaje)
print("Se ha salido del Bucle")
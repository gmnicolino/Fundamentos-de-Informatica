def es_simbolo(x):
    return x in 'abcdefghijklmnñopqrstuwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789, "'

def es_entero(x):
    try:
        i = int(x)
        return True
    except ValueError:
        return False

def str_es_simbolo(texto):
    for s in texto:
        if not es_simbolo(s):
            return False
    return True

def pedir_registro():
    calle = input("Ingrese nombre y número de la calle: ")
    while not str_es_simbolo(calle) or len(calle) < 2 or not es_entero(calle.split()[-1]):
        print("El formato de la calle es inválido.")
        calle = input("Ingrese nombre y número de la calle nuevamente: ")
    return calle

calle = pedir_registro()

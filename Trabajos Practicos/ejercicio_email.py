import re 

def verificar_mail(mail):
    if re.search(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", mail):
         print("La cuenta de correo electronico es valida.")
    else:
         print("La cuenta de correo electronico no es valida")

mail = input("Introduce un mail: ")

(verificar_mail(mail))


#otra forma

def mail_correcto(string):
    return bool(re.search("^\w+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$", string))

mail_correcto("salva-burgos@gmail.com")
mail_correcto("salva-&burgos@gmail.com")

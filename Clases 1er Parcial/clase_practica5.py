#Anexo expresiones regulares

# "\n" --> salto de linea
# r"\n" --> raw string (de esta forma Python va a ver dos caracteres "\" y "n")

#[a-zA-Z]  --> para buscar todos los caracteres del abecedario en mayuscula o minuscula

import re

texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = r"\bipsum\b"

print(re.sub(patron, "lapsus", texto))
# RESPUESTA: "Lorem lapsus dolor sit amet, consectetur lapsus elit. Amet sit amet."
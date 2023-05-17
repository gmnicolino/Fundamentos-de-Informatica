import os, glob

def primeras_lineas(path_a_txt, path_resultado, salida):
    os.chdir(path_a_txt)
    textos = glob.glob("*.txt")
    primer_linea = []
    for txt in textos:
       with open(txt, "r") as texto:
           primer_linea.append(texto.readline())
    
    os.chdir("../../")
    os.mkdir(path_resultado)
    os.chdir(path_resultado)
   with open(salida, "a") as final_txt:
       for linea in primer_linea:
           final_txt.write(linea)

primeras_lineas("datos/marzo", "resultado", "salida.txt")
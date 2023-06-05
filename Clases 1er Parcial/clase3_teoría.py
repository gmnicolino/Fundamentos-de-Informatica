#os.path --> para manipular path
#os.path.exists --> para corroborar que el archivo existe (repasar como se usa)

#with.open --> nos ayuda a que el archivo quede abierto solo mientras lo uso y se cierra para no cargar la memoria de la computadora
#open(path, mode) --> read
#open(path, mode) --> write
#open(path, mode) --> appear
#primero abro el archivo y en un segundo paso le pido a python si quiero:read, write or appear

#sys --> dialoga con el sistema operativo, nos sirve para tomar parametros desde la terminal

arch = open("clase3_teorica.txt", "r")
print(arch)
print(arch.read())

#read lee de una todo el archivo
#readlines() --> lee linea a linea el archivo

arch = open("clase3_teorica.txt", "r")
print(arch)
print(arch.readlines())

#"home/user/documents/clase3_teorica.txt" es lo mismo que "~/documents/clase3_teorica.txt" 
#en user es tu nombre --> el usuario depende de cada computadora en la que estoy

#con cd.. me muevo para acceder a otra carpeta

#Fundamentos_de_informatica/Control_de_versiones/  --> para encontrar cosas que tenemos que instalar 

#Fundamentos_de_informatica/Control_de_versiones/[1]Git_GitHub_Intro.md
#Control de versiones

#para GIT decir commit es "sacar la foto"
#en el index agregas cosas
#git add : vas agregando cosas
#git commit : cuando lo usas todo lo que agregaste anteriormente se pasa definitivo al otro archivo
#cuando hago git commit siempre se le debe asociar un mensaje.
#en la terminal: git commit -m "xxxxx" --> en xxxx puede ir "add script"
#git pull: me sirve para bajar lo guardado en el repositorio para trabajar en la computadora que estoy en ese momento, siempre lo hago antes de arrancar.
#git push: antes de cerrar la computadora, siempre tengo que tocar git push para asi se guarda la ultima version


#Fundamentos_de_informatica/Intro_Linux_Bash/Intro_linux.md
#En la terminal, nos dice el path en ~
#pongo pwd
#pongo ls
#pongo cd y el doc que quiero entrar

#para volver para atras pongo cd..

#las palabras reservadas o nombres de bibliotecas nunca pueden ser nombres de un archivo (ej:print, pandas)


#git clone : para clonar un doc en mi computadora, cuando lo bajo por primera vez



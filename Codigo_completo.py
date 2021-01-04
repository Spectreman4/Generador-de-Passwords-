import random 

#Generador de contraseñas simple 

#Banner
print("Generador de contraseñas")
print("By Spectreman4")
print("         .'----------`.                          ")    
print("         | .--------. |                          ")   
print("         | |########| |       __________         ")     
print("         | |########| |      /__________\        ")     
print(".--------| `--------' |------|    --=-- |-------------.")
print("|       ______|_|_______     |__________|             |") 
print("|      /  %%%%%%%%%%%%  \                             |") 
print("|     /  %%%%%%%%%%%%%%  \                            |") 
print("|     ^^^^^^^^^^^^^^^^^^^^                            |") 
print("+-----------------------------------------------------+")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^") 

#variables que representan los caracteres que usara el programa

Mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Minusculas = "abcedfghijklmnopqrstuvwxyz"
Numeros = "1234567890"

Ma, Mi, Num = True, True, True

#variable que representa donde se colocaran los caracteres
Caracteres = ""

#los que pasa si
if Ma:
	Caracteres += Mayusculas

if Mi:
	Caracteres += Minusculas

if Num:
	Caracteres += Numeros


#estas son las variables largo y contraseñas que definira el usuario
Largo = input(print("Inserte el numero de caracteres de la contraseña: \n"))

Largo = int(Largo)





for x in range(1):
	Contraseña = (random.sample(Caracteres, Largo))
	print(Contraseña)

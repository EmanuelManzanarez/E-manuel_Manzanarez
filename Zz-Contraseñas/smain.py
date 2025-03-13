import os
import random

def menu():
	os.system ('cls')
	print ("--Menú para encirptar y desencriptar contraseñas--")
	print ("1 - Generar una contraseña random encriptada")
	print ("2 - Ingresa una contraseña tuya para encriptarla")
	print ("3 - Desencriptar la contraseña")
	print ("9 - salir")

def randpass():
	password = []
	passwordS = ""
	mayus = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
	minus = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
	symbol = ["!","@","#","$","%","*","+","=", "_", ""]
	number = ["1","2","3","4","5","6","7","8","9","0"]

	#Generar longitud de contrasena
	rand = random.randint(12,17) #secrets.randbelow(16)

	#Rellenar espacios de contrasena
	for n in range(rand):
		password += "-"

	for n in range(3):
		while True:
			randsy = random.randint(0,(len(symbol) - 1))
			randp = random.randint(0,(len(password) - 1))
			if password[randp] == "-":
				password[randp] = symbol[randsy]
				break

	for n in range(3):
		while True:
			randnu = random.randint(0,(len(number) - 1))
			randp = random.randint(0,(len(password) - 1))
			if password[randp] == "-":
				password[randp] = number[randnu]
				break

	for n in range(100):
		randmay = random.randint(0,(len(mayus) - 1))
		randmin = random.randint(0,(len(minus) - 1))

		randp = random.randint(0,(len(password) - 1))
		if password[randp] == "-":
			password[randp] = mayus[randmay]

		randp = random.randint(0,(len(password) - 1))
		if password[randp] == "-":
			password[randp] = minus[randmin]

	key = passwordS.join(password)

	return key

def CifradoCesar_Contra():
    appname = input("Ingresa el nombre de la aplicación: ")
    clave = input('Ingresa tu palabra clave para cifrar: ')
    preg = input("Desea cambiar la ruta, 1.Si \n 2.No")
    contra = randpass()
    espacios = 1
    while espacios > 0:
            espacios = clave.count(' ')
            if clave.isalpha() == False:
                    espacios += 1
    key = len(clave)
	SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.@'
	translated = ''

	for symbol in contra:
	    if symbol in SYMBOLS:
	        symbolIndex = SYMBOLS.find(symbol)
	        translatedIndex = symbolIndex + key
	        
	        if translatedIndex >= len(SYMBOLS):
	            translatedIndex = translatedIndex - len(SYMBOLS)
	   
	        elif translatedIndex < 0:
	            translatedIndex = translatedIndex + len(SYMBOLS)

	        translated = translated + SYMBOLS[translatedIndex]
	    else:
	        translated = translated + symbol
	print("Contraseña sin cifrar " + contra)
	print("Contraseña cifrada " + translated)
	if preg == "2":
                fc = open("contras.txt","a")
                fc.write(appname + ": ")
                fc.write(translated + "\n")
        if preg == "1":
                ruta = input("¿Cual seria su ruta? (Ingreselo con //)")
                fc = open(ruta + "contras.txt","a")
                fc.write(appname + ": ")
                fc.write(translated + "\n")


#appname = input("Ingresa el nombre de la aplicación: ")
#clave = input('Ingresa tu palabra clave para cifrar: ')
#CifradoCesar_Contra(appname,clave)

def CifradoCesar_TuContra():
	appname = input("Ingresa el nombre de la aplicación: ")
	contra = input("Ingrese su contraseña >> ")
	clave = input('Ingresa tu palabra clave para cifrar: ')
	espacios = 1
	while espacios > 0:
	    espacios = clave.count(' ')
	    if clave.isalpha() == False:
	        espacios += 1
	key = len(clave)
	SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.@'
	translated = ''

	for symbol in contra:
	    if symbol in SYMBOLS:
	        symbolIndex = SYMBOLS.find(symbol)
	        translatedIndex = symbolIndex + key
	        
	        if translatedIndex >= len(SYMBOLS):
	            translatedIndex = translatedIndex - len(SYMBOLS)
	   
	        elif translatedIndex < 0:
	            translatedIndex = translatedIndex + len(SYMBOLS)

	        translated = translated + SYMBOLS[translatedIndex]
	    else:
	        translated = translated + symbol

	print(translated)
	fc = open("contras.txt","a")
	fc.write(appname + ": ")
	fc.write(translated + "\n")

#appname = input("Ingresa el nombre de la aplicación: ")
#contra = input("Ingrese su contraseña >> ")
#clave = input('Ingresa tu palabra clave para cifrar: ')
#CifradoCesar_TuContra(appname,clave)


def DesifradoCesar_Contra():
	contra = input('Ingresa la contraseña: ')
	clave = input('Ingresa tu palabra clave para cifrar: ')
	espacios = 1
	while espacios > 0:
	    espacios = clave.count(' ')
	    if clave.isalpha() == False:
	        espacios += 1

	SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.@'

	translated = ''

	for symbol in contra:
	    if symbol in SYMBOLS:
	        symbolIndex = SYMBOLS.find(symbol)
	        translatedIndex = symbolIndex - key
	        
	        if translatedIndex >= len(SYMBOLS):
	            translatedIndex = translatedIndex - len(SYMBOLS)
	        elif translatedIndex < 0:
	            translatedIndex = translatedIndex + len(SYMBOLS)

	        translated = translated + SYMBOLS[translatedIndex]
	    else:
	        translated = translated + symbol

	print("Tu contraseña es: " + translated)

#contra = input('Ingresa la contraseña: ')
#clave = input('Ingresa tu palabra clave para cifrar: ')
#DesifradoCesar_Contra(contra,clave)

while True:
	menu()
	opcionMenu = input("Seleccione una opción >> ")
	if opcionMenu == "1":
		print ("")
		CifradoCesar_Contra()
		input("Pulsa enter para continuar")
	elif opcionMenu == "2":
		print ("")
		CifradoCesar_TuContra()
		input("Pulsa enter para continuar")
	elif opcionMenu == "3":
		print ("")
		DesifradoCesar_Contra()
		input("Pulsa enter para continuar")
	elif opcionMenu == "9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa enter para continuar")

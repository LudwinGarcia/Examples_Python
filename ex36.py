# -*- coding: utf-8 -*-
from sys import exit

def matematica():
	print"\n"
	print "*" * 76
	print "\n++++++ HAS LLEGADO A LA ULTIMA PRUEBA!!!!++++++"
	print "\nEn una jaula hay conejos y palomas, pueden contarse 35 cabezas y 94 patas."
	print "Cuántos animales hay de cada clase? "
	print "\t 1) 14 conejos y 21 palomas"
	print "\t 2) 12 conejos y 23 palomas"
	print "\t 3) 17 conejos y 18 palomas"

	while True:
		respuesta = raw_input("\t> ")
		try:
			respuesta = int(respuesta)
			break
		except ValueError:
			pass

	if respuesta == 2:
		print "\n"
		print "#" * 78
		print "\n\t\t ERES EL NUMERO UNO!!!! "
		print """
		_______________+88 
		_______________+880 
		_______________++880 
		_______________++880 
		________________+880 
		________________+8880 
		________________++880 
		________________++888_____+++88 
		________________++8888__+++8880++88 
		________________+++8888+++8880++8888 
		_________________++888++8888+++888888++8888 
		_________________++88++8888++8888888++888888 
		_________________++++++888888888888888888_+88 
		__________________++++++88888888888888888_++8 
		__________________++++++++000888888888888+88 
		___________________+++++++000088888888888_88 
		____________________+++++++00088888888888 
		_____________________+++++++088888888888 
		_____________________+++++++088888888888 
		______________________+++++++8888888888 
		______________________+++++++0088888888 
		______________________++++++0088888888 
		______________________++++++00888888
		"""
		print"\n\t\t PASASTE LA PRUEBA CON EXITO"
		print "#" * 78
		print "\n"
	elif respuesta == 1 or respuesta == 3:
		print "\n"
		print "#" * 74
		print "no lograste encontrar la respuesta y moriste encerrado en la habitacion!!!"
		print "#" * 74
		print "\n"
	else:
		print ("\n************* ERROR *************")
		print ("Solo puedes elegir del 1 al 3...")
		print ("*********************************\n")
		matematica()

def logica():
	print"\n"
	print "*" * 76
	print "\nEn esta habitacion encuentras una adivinanza en la pared que dice: "
	print "\nDe tanto pensar te volveras loco, la suegra de la mujer de tu hermano,"
	print "Que parentesco le corresponde? si no contestas correctamente moriras aqui..."
	print "\t 1) Tu esposa"
	print "\t 2) Tu mama"
	print "\t 3) Ninguno"

	while True:
		respuesta = raw_input("\t> ")
		try:
			respuesta = int(respuesta)
			break
		except ValueError:
			pass

	if respuesta == 2:
		print "\n"
		print "#" * 78
		print "Excelente!, has probado tu inteligencia decifraste correctamente la pregunta!!"
		print "#" * 78
		print "\n"
		matematica()
	elif respuesta == 1 or respuesta == 3:
		print "\n"
		print "#" * 74
		print "Escogiste el parentezco incorrecto y moriste encerrado en la habitacion!!!"
		print "#" * 74
		print "\n"
	else:
		print ("\n************* ERROR *************")
		print ("Solo puedes elegir del 1 al 3...")
		print ("*********************************\n")
		logica()

def ciclope():
	print"\n"
	print "*" * 76
	print "+++Has escogido la habitacion de la derecha+++"
	print "\nEn esta habitacion encuentras un ciclope y enseguida te ataca,"
	print "Tu corres para poder escapar de sus ataques y te das cuenta que es torpe,"
	print "Te propones atacarlo pero ten encuenta que solo pudes hacerlo una vez,"
	print "En que lugar enfocarias el ataque para ven"
	print "\t 1) Realizas tu ataque en el cuello..."
	print "\t 2) Realizas tu ataque en su ojo..."
	print "\t 3) Realizas tu atque en el estomago..."

	while True:
		respuesta = raw_input("\t> ")
		try:
			respuesta = int(respuesta)
			break
		except ValueError:
			pass

	if respuesta == 1:
		print "\n"
		print "#" * 61
		print "Moriste!, sus reflejos fueron superiorey y te aplasto!!"
		print "#" * 61
		print "\n"
	elif respuesta == 3:
		print "\n"
		print "#" * 61
		print "Moriste!, te mando a volar con la fuerza de su cuerpo!!"
		print "#" * 61
		print "\n"
	elif respuesta == 2:
		print "\n"
		print "#" * 70
		print "Excelente!, has probado tu inteligencia atacaste su punto debil!!"
		print "#" * 70
		print "\n"
		logica()
	else:
		print ("\n************* ERROR *************")
		print ("Solo puedes elegir del 1 al 3...")
		print ("*********************************\n")
		ciclope()

def acertijo():
	print"\n"
	print "*" * 76
	print "\nTe encuentras en una nueva habitacion, tienes una mesa frente a ti,"
	print "Veras que sobre ella hay 6 vasos que se encuentran ordenados de forma"
	print "Horizontal 3 vasos tiene agua y los otros 3 estan vacios, los vasos se"
	print "encuentran ordenados de la siguiente manera: "
	print """
	\t Pocicion 1 = vaso vacio
	\t Pocicion 2 = vaso lleno
	\t Pocicion 3 = vaso lleno
	\t Pocicion 4 = vaso lleno
	\t Pocicion 5 = vaso vacio
	\t Pocicion 6 = vaso vacio
	"""
	print "\nLo que tienes que hacer buscar la menera de que queden intercaldos"
	print "Es decir, mantener una linea y  que junto a cada vaso lleno este uno vacio."
	print "\nTodo esto debe realizarce moviendo un solo vaso, elege que vaso utlizarias"
	print "Para poder cumplir con el obejtivo: 1, 2, 3, 4, 5, 6"

	while True:
		respuesta = raw_input("\t> ")
		try:
			respuesta = int(respuesta)
			break
		except ValueError:
			pass

	if respuesta == 3:
		print "\n"
		print "#" * 73
		print "Excelente!, has probado tu inteligencia escogiste el vaso correctamente!!"
		print "#" * 73
		print "\n"
		matematica()
	elif respuesta == 1 or respuesta == 2 or respuesta == 4 or respuesta == 5 or respuesta == 6:
		print "\n"
		print "#" * 71
		print "Escogiste el vaso incorrecto y te quedaste encerrado hasta la muerte!!!"
		print "#" * 71
		print "\n"
	else:
		print ("\n************* ERROR *************")
		print ("Solo puedes elegir del 1 al 6...")
		print ("*********************************\n")
		acertijo()

def copas():
		print"\n"
		print "*" * 76
		print "+++Has escogido la habitacion de la izquierda+++"
		print "\nEn esta habitacion encuentras un mayordomo y te dice:"
		print '\nFrente a mi como puedes observar tengo una mesa, en esta mesa'
		print 'Tengo dos copas de vino una con veneno y otra sin veneno, Que eliges?'
		print "\t 1) Eliges la copa de la izquierda y bebes de ella..."
		print "\t 2) Eliges la copa de la derecha y bebes de ella..."
		print "\t 3) No bebes de ninguna copa..."

		while True:
			respuesta = raw_input("\t> ")
			try:
				respuesta = int(respuesta)
				break
			except ValueError:
				pass

		if respuesta == 1:
			print "\n"
			print "#" * 61
			print "Moriste!, La copa de la izquierda se encontraba envenenada!!"
			print "#" * 61
			print "\n"
		elif respuesta == 2:
			print "\n"
			print "#" * 61
			print "Moriste!, La copa de la derecha se encontraba envenenada!!"
			print "#" * 61
			print "\n"
		elif respuesta == 3:
			print "\n"
			print "#" * 70
			print "Excelente!, has probado tu inteligencia las dos copas tenian veneno!!"
			print "#" * 70
			print "\n"
			acertijo()
		else:
			print ("\n************* ERROR *************")
			print ("Solo puedes elegir del 1 al 3...")
			print ("*********************************\n")
			copas()

def puertas():
	print"\n"
	print "*" * 76
	print "\nTomaste una sabia decicion, ahora te encuentras en una habitacion,"
	print "frente a ti hay dos puertas cual escojeras"
	print "\t 1) Izquierda"
	print "\t 2) Derecha"

	while True:
		respuesta = raw_input("\t> ")
		try:
			respuesta = int(respuesta)
			break
		except ValueError:
			pass

	if respuesta == 1:
		copas()
	elif respuesta == 2:
		ciclope()
	else:
		print ("\n********** ERROR **********")
		print ("Solo puedes elegir 1 o 2...")
		print ("***************************\n")
		puertas()

def start():
	print "*" * 76
	print "\nTE ENCUENTRAS EN UNA PRUEBA, Y TE DEJAN EN LA CIMA DE UNA TORRE"
	print "\nLo que tienes que realizar en la prueba es buscar la manera"
	print "De llegar hasta abajo, la torre es cilindrica, esta hecha de"
	print "Cuadros de priedra en todo su exterior y esta totalmente sellada."
	print "\nTen encuenta que puedes encontrarte con trampas, por ello, "
	print "tienes que analizar tus acciones para no morir en el intento"
	print "\nYa que comprendes la situacion que opcion elegirias:"
	print "\t1) Tratar de bajar la torre por el costado utilizando las piedras..."
	print "\t2) Buscarias un entrada a la torre en el piso..."

	while True:
		respuesta = raw_input("\t> ")
		try:
			respuesta = int(respuesta)
			break
		except ValueError:
			pass

	if respuesta == 2:
		puertas()
	elif respuesta == 1:
		print "\n"
		print "#" * 61
		print "Moriste!, No Tomaste en cuenta que las piedras se contraen..."
		print "#" * 61
		print "\n"
	else:
		print ("\n********** ERROR **********")
		print ("Solo puedes elegir 1 o 2...")
		print ("***************************\n")
		start()

start()

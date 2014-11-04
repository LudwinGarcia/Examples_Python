i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "\nThe numbers: "
for num in numbers:
	print num

print "\n\n"


def Guardar():
	x = 0
	lista = []

	print "Ingrese un numero"
	save = int(raw_input("> "))

	print "\n\n"

	while x < save:
		print "At the top i is %d" % x
		lista.append(x)
		x += 1
		print "Numbers now: ", lista
		print "At the bottom i is %d" % x

	print "\nThe numbers: "
	for num in lista:
		print num

Guardar()


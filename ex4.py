cars = 100 #Guardamos el numro 100 en la variable cars
space_in_a_car = 4.0 #Guardamos el numero 4.0 en la variable space_in_a_car
drivers = 30 #Guardamos el numero 30 en la variable drivers
passengers = 90 #Guardamos el numero 90 en la variable passengers
cars_not_driven = cars - drivers #Realizamos la operacion resta casa(100) - drivers(30) = 70 
cars_driven = drivers #Guardamos el valor que tiene la variable driver en Cars_driven
carpool_capacity = cars_driven * space_in_a_car #Operamos cars_driven(30) * space_in_a_car(4.0) = 120 
average_passengers_per_car = passengers / cars_driven #Dividimos passengers(90) / cars_driven(30) = 3

#Mostramos los resoltados guardaos en las variables anteriores
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

''' STUDY DRILLS
Traceback (most recent call last):
File "ex4.py", line 8, in <module>
average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined

*** RESPUESTA ***
El motivo de que este error pase es que la variable utilizada fue mal
escrita ya que el nombre correcto es "carpool_capacity" 
'''

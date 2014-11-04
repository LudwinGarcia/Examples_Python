print ''' 
+++++++++++++++++++++++++ EJERCICIO MANUALMENTE ++++++++++++++++++++++++++
True and True \t\t\t\t\t\t\t R= TRUE
False and True \t\t\t\t\t\t\t R= FALSE
1 == 1 and 2 == 1 \t\t\t\t\t\t R= FALSE
"test" == "test" \t\t\t\t\t\t R= TRUE
1 == 1 or 2 != 1 \t\t\t\t\t\t R= TRUE
True and 1 == 1 \t\t\t\t\t\t R= TRUE
False and 0 != 0 \t\t\t\t\t\t R= FALSE
True or 1 == 1 \t\t\t\t\t\t\t R= TRUE
"test" == "testing" \t\t\t\t\t\t R= FALSE
1 != 0 and 2 == 1 \t\t\t\t\t\t R= FALSE
"test" != "testing" \t\t\t\t\t\t R= TRUE
"test" == 1 \t\t\t\t\t\t\t R= FALSE
not (True and False) \t\t\t\t\t\t R= TRUE
not (1 == 1 and 0 != 1) \t\t\t\t\t R= FALSE
not (10 == 1 or 1000 == 1000) \t\t\t\t\t R= FALSE
not (1 != 10 or 3 == 4) \t\t\t\t\t R= FALSE
not ("testing" == "testing" and "Zed" == "Cool Guy") \t\t R= TRUE
1 == 1 and not ("testing" == 1 or 1 == 0)\t\t\t R= TRUE
"chunky" == "bacon" and not (3 == 4 or 3 == 3) \t\t\t R= FALSE
3 == 3 and not ("testing" == "testing" or "Python" == "Fun") \t R= FALSE
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

'''
uno = (True and True)
dos = (False and True)
tres = (1 == 1 and 2 == 1)
cuatro = ("test" == "test")
cinco = (1 == 1 or 2 != 1)
seis = (True and 1 == 1)
siete = (False and 0 != 0)
ocho = (True or 1 == 1)
nueve = ("test" == "testing")
dies = (1 != 0 and 2 == 1)
once = ("test" != "testing")
doce = ("test" == 1)
trece = (not (True and False))
catorce = (not (1 == 1 and 0 != 1))
quince = (not (10 == 1 or 1000 == 1000))
diesYseis = (not (1 != 10 or 3 == 4))
diesYsiete = (not ("testing" == "testing" and "Zed" == "Cool Guy"))
diesYocho = (1 == 1 and not ("testing" == 1 or 1 == 0))
diesYnueve = ("chunky" == "bacon" and not (3 == 4 or 3 == 3))
veinte = (3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))

print '++++++++++++++++++++++++++ EJERCICIO CON PYTHON ++++++++++++++++++++++++++'
print "True and True \t\t\t\t\t\t\t R= %s" %uno 
print "False and True \t\t\t\t\t\t\t R= %s" %dos
print "1 == 1 and 2 == 1 \t\t\t\t\t\t R= %s" %tres
print '"test" == "test" \t\t\t\t\t\t R= %s' %cuatro
print "1 == 1 or 2 != 1 \t\t\t\t\t\t R= %s" %cinco
print "True and 1 == 1 \t\t\t\t\t\t R= %s" %seis
print "False and 0 != 0 \t\t\t\t\t\t R= %s" %siete
print "True or 1 == 1 \t\t\t\t\t\t\t R= %s" %ocho
print '"test" == "testing" \t\t\t\t\t\t R= %s' %nueve
print "1 != 0 and 2 == 1 \t\t\t\t\t\t R= %s" %dies
print '"test" != "testing" \t\t\t\t\t\t R= %s' %once
print '"test" == 1 \t\t\t\t\t\t\t R= %s' %doce
print "not (True and False) \t\t\t\t\t\t R= %s" %trece
print "not (1 == 1 and 0 != 1) \t\t\t\t\t R= %s" %catorce
print "not (10 == 1 or 1000 == 1000) \t\t\t\t\t R= %s" %quince
print "not (1 != 10 or 3 == 4) \t\t\t\t\t R= %s" %diesYseis
print 'not ("testing" == "testing" and "Zed" == "Cool Guy") \t\t R= %s' %diesYsiete
print '1 == 1 and not ("testing" == 1 or 1 == 0)\t\t\t R= %s' %diesYocho
print '"chunky" == "bacon" and not (3 == 4 or 3 == 3) \t\t\t R= %s' %diesYnueve
print '3 == 3 and not ("testing" == "testing" or "Python" == "Fun") \t R= %s' %veinte
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
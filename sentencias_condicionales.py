nombre = input("Para comenzar, Cual es tu nombre?: ")
matematicas = int(input(nombre + ", cual es tu calificacion en matematicas?: "))
quimica = int(input(nombre + ", cual es tu calificacion en quimica?: "))
biologia = int(input(nombre + ", cual es tu calificacion en biologia?: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 70:
    print('Felicidades ' + nombre + ', "aprobaste" con un promedio de: ' + str(promedio))
else:
    print('Lo siento ' + nombre + ', "reprobaste" con un promedio de: ' + str(promedio))
print("fin.")
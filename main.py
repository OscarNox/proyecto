#esto es una asignacion
print("-----Asignacion-----")
mensaje="hola"
mensaje += " " 
mensaje += "jose oscar"
print(mensaje)

#esto es una concatenacion
print("-----Concatenacion-----")
mensaje="Hola"
espacio=" "
nombre="Jose Oscar"
print(mensaje + espacio + nombre)

#concatenacion con numeros
print("-----Concatenacion con numeros-----")   
numero_uno=5
numero_dos=10
resultado= numero_uno + numero_dos
resultado=str(resultado)
print("El resultado de la suma es: " + resultado) 

print("-----Busqueda-----")
#esto es una busqueda
mensaje="Hola Jose Oscar"
buscar_subcadena=mensaje.find("Oscar")
print(buscar_subcadena)


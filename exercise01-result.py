#Creación de la lista
listaDic = []

#Declaración de variables a utilizar
confirmacion = True
sumaCosto = 0.0
i = 0

print("Este programa permite grabar registros de clientes y obtener su reporte de costos")

#Bucle para introducir diccionarios a la lista
while confirmacion:
    nombre = input("Introduzca el nombre del cliente: ")
    producto = input("Introduzca el producto: ")
    costo = input("Introduzca el costo ($ 0.00): ")

    registro = {"name": nombre, "product": producto, "cost": costo}
    listaDic.append(registro)

    print("¿Desea agregar otro cliente?")
    confirmacion = "" == input("(Presione 'Enter' si desea agregar otro cliente, de lo contrario, introduzca un caracter cualquiera) ")

print("Se han registrado "+str(len(listaDic))+" clientes")
#print(listaDic)

#Bucle para calcular el costo total
while i < len(listaDic):
    sumaCosto += float(listaDic[i]["cost"])
    i += 1

print("El costo total es: $ "+str(sumaCosto))


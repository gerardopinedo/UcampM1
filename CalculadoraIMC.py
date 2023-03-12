# Solicitud de datos
while True:
    nombre = input("Teclea tu nombre: ")
    if nombre != "":
        break
    else:
        print("Error: debes ingresar el nombre.")

while True:
    apellido_paterno = input("Teclea tu apellido paterno: ")
    if apellido_paterno != "":
        break
    else:
        print("Error: debes ingresar eñ apellido paterno.")

while True:
    apellido_materno = input("Teclea tu apellido materno: ")
    if apellido_materno != "":
        break
    else:
        print("Error: debes ingresar el apellido materno.")

while True:
    try:
        edad = int(input("Teclea tu edad: "))
        peso = float(input("Teclea tu peso en kg: "))
        estatura = float(input("Teclea tu estatura en metros: "))
        break
    except ValueError:
        print("Error: asegúrate de ingresar una cifra en edad, peso y estatura.")

# Calculo de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Despliega de datos y el IMC en pantalla
print("Nombre completo:", nombre, apellido_paterno, apellido_materno)
print("Edad:", edad, "años")
print("Peso:", peso, "kg")
  print("Estatura:", estatura, "metros")
print("IMC:", imc)

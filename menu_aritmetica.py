#Ejercicio menu calculadora
import os # Importar librerias del sistema

os.system("cls")
print("Menú principal")
print ("1. sumar números")
print ("2. restar números")
print ("3. multiplicar números")
print ("4. dividir números")
print (".:::digite su opcion")

num1= int(input("ingrese el primer numero"))
num2= int(input("ingrese el segundo numero"))
opc= int(input ("digite la operación a realizar:"))
if opc== 1. :
		suma=num1 + num2
		print("La suma es:",suma)
elif opc == 2:
	resta=num1 - num2
	print("La resta es:",resta)
elif opc == 3:
	multiplicar=num1*num2
	print("El producto es:",multiplicar)
elif opc ==4:
	dividir=num1/num2
	print("El cociente es:",dividir)
else:
	print("ingresar numero valido")			
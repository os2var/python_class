#Algoritmo numero_mayor
n1=0
n2=0
n1=int(input ("Ingrese el primer numero:"))
n2=int(input("Ingrese el segundo numero:"))
if n1>n2 :
	print ("el numero mayor es:" ,n1)
else:
	if n2>n1:
		print ("el numero mayor es:",n2)
	else:
		print ("los numeros ingresados son iguales")

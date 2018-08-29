print("operaciones aritmeticas")

num1=int(input("ingrese el primer numero"))
num2=int(input("ingrese el segundo numero"))

print("1. suamar numeros")
print("2. restar numeros")
print("3. multiplicar numeros")
print("4. dividir numeros")
opc=int(input("digite la operación a realizar:"))

if opc == 1 :
	print("el resultado es: ",num1 + num2)
elif opc == 2 :
	print("el resultado es:", num1 - num2)
elif opc == 3:
	print("el resultado es:",num1*num2)
elif opc == 4:
	print("el resultado es:",num1/num2)
else :
	print("ha ingresado una opción incorrecta")			
			


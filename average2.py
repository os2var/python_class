i=1
suma_edades=0
max_personas=int(input("ingrese cantidad de personas:.."))
while i<=max_personas:
	edad=int(input("ingrese la edad"))
	i = i+1
	suma_edades=suma_edades + edad

promedio_edades = suma_edades/max_personas
print(float(promedio_edades))	




cant=int(input("ingresar cantidad de personas"))
c=1
gmujer=0
ghombre=0
edusuario=0
edmujer=0
edhombre=0
while c<=cant:
    edad=float(input("ingrese su edad"))
    genero=input("ingrese su genero")
    edusuario=edusuario+edad
    c=c+1
    promedio=edusuario/cant
    if genero=="m":
        ghombre=ghombre+1
        edhombre=edhombre+edad
    elif genero=="f":
         gmujer=gmujer+1
         edmujer=edmujer+edad
        
promehom=edhombre/ghombre
promujer=edmujer/gmujer                      
print("MENU PRINCIPAL")
print("1.promedio de todas las edades",promedio)
print("2.numero total de mujeres",gmujeres)
print("3.numero total de hombres",ghombres)
print("4.promedio de edades de mujeres",promediomuj)
print("5.promedio de edades de hombres",promediohom)
print("numero total de personas ingresadas en el sistema",cant)

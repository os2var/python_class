#funcion para operaciones aritmeticas
def MENU ():
    print(":::MENU ARITMETIO:::")
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")
    print("5.Raiz cuadrada")
def operaciones():   
    if opc==1:
        print("El resultado es:",a+b)
    elif opc==2:
        print("el resultado es:",a-b)
    elif opc==3:
        print("el resultado es:",a*b)
    elif opc==4:
        print("la resultado es:",a/b)        
    if opc==5:
        print("la raiz cuadrada de a es:",a**(0.5))
        print("la raiz cuadrada de b es:",b**(0.5))
def DATOS ():
    global a,b
    a=int(input("Digite a:"))
    b=int(input("Digite b:"))
    
     
DATOS()
MENU()
opc=int(input("Digite su opcion:"))
operaciones()

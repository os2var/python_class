      
                          
                
                          
                          
                           
                           
print("UNCENTAVOMAS")            
print("bienvenido a un centavomas:")
clave1='1770'
intentos=3
i=1
saldo=3500000
while i<=intentos :
    clave2=input("digite clave:")
    if clave1==clave2:
        print("menu transaccional:")
        print("1. cambiar clave:")
        print("2. mostrar saldo:")
        print("3. realizar retiro:")
        print("4. salir:")
    else:
        if i<intentos:
            print("clave incorrecta.Digite nuevamente")
        else:
            print ("usted no tiene mas intentos. Su tarjeta fue bloqueada")
        i=i+1
    opc=int(input("digite opcion"))
    if opc==1 :
        print("cambiar clave:")
    elif opc==2 :
        print("saldo de la cuenta",saldo)
    elif opc==3 :
        print("valor a retirar")
        print("1. $10.000")
        print("2. $20.000")
        print("3. $50.000")
        print("4. $100.000")
        print("5. $200.000")
        print("6. $400.000")
        print("7. $600.000")
        print("8. $1.000.000")
        sub=int(input("digite opcion:"))
        if sub==1:
            saldonew=saldo-10000
            print("valor extraido $10.000")
            print("saldo total es",saldonew)
            if saldonew<0:
                print("no cuenta con el suficiente dinero")
        elif sub==2:
            saldonew2=saldo-20000
            print("valor extraido $20.000 ")
            print("saldo total es",saldonnew2)
            if saldonew2<0:
                print("no cuenta con el suficiente dinero")
        elif sub==3:
            saldonew3=saldo-50000
            print("valor extraido $50.000")
            print("saldo total es",saldonew3)
            if saldonew3<0:
                print("no cuenta con el suficiente dinero")
        elif sub==4:
            saldonew4=saldo-100000
            print ("valor extraido $100.000")
            print ("saldo total es: ",saldonew4)
        elif sub==5:
            saldonew5=saldo-200000
            print("valor extraido $200.000 ")
            print("saldo total es",saldonew5)
            if saldonew5<0:
                print("no cuenta con el suficiente dinero")
        elif sub==6:
            saldonew6=saldo-400000
            print("valor extraido $400.000 ")
            print("saldo total es",saldonew6)
            if saldonew6<0:
                print("no cuenta con el suficiente dinero")
        elif sub==7:
            saldonew7=saldo-600000
            print("valor extraido $600.000 ")
            print("saldo total es",saldonew7)
            if saldonew7<0:
                print("no cuenta con el suficiente dinero")
        elif sub==8:
            saldonew8=saldo-1000000
            print("valor extraido $1.000.000 ")
            print("saldo total es",saldonew8)
            if saldonew8<0:
                print("no cuenta con el suficiente dinero")
        break

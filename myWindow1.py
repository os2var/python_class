#Importar librerarias para GUI
from tkinter import *
import tkinter

#VENTANA
#crear la primer ventana
root=tkinter.Tk()

#dimension de la ventana (W=ancho x H=altura)
root.geometry("400x400")

#nombre
root.title("Mi Calculadora")

#para permitir o no ampliar la ventana V=TRUE o F=FALSE 
root.resizable(FALSE,FALSE)

#COLOR
root.configure(background="#31475A")

def btnClick(valor):
    global operador
    operador=operador + str(valor)
    #str=string__cadena y este concatena lo del operador mas el valor
    input_text.set(operador)

def clear():
    global operador
    operador=("")
    input_text.set(operador)

def operacion():
    global operador
    try:
        opera=str(eval(operador))
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera)    
######################################################################################    
    
input_text=StringVar()
operador=""#limpia y comienza en cero


#PANTALLA    

Display=Entry(root,font=('arial',20,'bold'),width=22, bd=15,insertwidth=4, bg="#33A2FF", justify="right",textvariable=input_text).place(x=30,y=10)#este se llama input_text


Boton1=Button(root, text = "1", width = 4, height = 2, command=lambda:btnClick(1)).place(x=30,y=100)
Boton2=Button(root, text = "2", width = 4, height = 2, command=lambda:btnClick(2)).place(x=90,y=100)
Boton3=Button(root, text = "3", width = 4, height = 2, command=lambda:btnClick(3)).place(x=150,y=100)
Boton4=Button(root, text = "4", width = 4, height = 2, command=lambda:btnClick(4)).place(x=30,y=150)
Boton5=Button(root, text = "5", width = 4, height = 2, command=lambda:btnClick(5)).place(x=90,y=150)
Boton6=Button(root, text = "6", width = 4, height = 2, command=lambda:btnClick(6)).place(x=150,y=150)
Boton7=Button(root, text = "7", width = 4, height = 2, command=lambda:btnClick(7)).place(x=30,y=200)
Boton8=Button(root, text = "8", width = 4, height = 2, command=lambda:btnClick(8)).place(x=90,y=200)
Boton9=Button(root, text = "9", width = 4, height = 2, command=lambda:btnClick(9)).place(x=150,y=200)
Boton10=Button(root, text = "0", width = 4, height = 2, command=lambda:btnClick(0)).place(x=30,y=250)
Boton11=Button(root, text = "clear", width = 4, height = 2, command=lambda:clear()).place(x=90,y=250)
Boton12=Button(root, text = "=", width = 4, height = 2, command=operacion).place(x=150,y=250)
Boton13=Button(root, text = "+", width = 4, height = 2, command=lambda:btnClick("+")).place(x=200,y=100)
Boton14=Button(root, text = "-", width = 4, height = 2, command=lambda:btnClick("-")).place(x=200,y=150)
Boton15=Button(root, text = "*", width = 4, height = 2, command=lambda:btnClick("*")).place(x=200,y=200)
Boton16=Button(root, text = "/", width = 4, height = 2, command=lambda:btnClick("/")).place(x=200,y=250)
#Abrir ventana o la libera
root.mainloop()

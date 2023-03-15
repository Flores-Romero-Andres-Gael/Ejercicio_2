#Flores Romero Andres Gael
#09/03/2023

from tkinter import *
from tkinter import ttk
import tkinter as ttk

#--------------------BASE FRAME--------------------
root = Tk()

root.geometry("660x530")
root.configure(background="gray40")

#imagen
image1 = PhotoImage(file="Compras.png")
imagenCarrito = ttk.Label(root, background="gray40")
imagenCarrito.grid(column=0, row=0, sticky=(W))
imagenCarrito['image'] = image1

#Label
ttk.Label(root, text="Product Management ", font=("verdana", 30, "bold"), foreground="white", background="gray40").grid(column=0, row=0, sticky=(W), padx=80)

#-----------------------FRAMES-----------------------

#--------------------PRIMER FRAME--------------------
Frame1 = ttk.Frame(root, background="gray2")
Frame1.grid(column=0, row=1, sticky=(W))

#--------------------SEGUNDO FRAME--------------------
Frame2 = ttk.Frame(Frame1, background="#482525")
Frame2.grid(column=0, row=0, padx=35, pady=10)

#--------------------TERCER FRAME--------------------
Frame3 = ttk.Frame(Frame2, background="#482525")
Frame3.grid(column=0, row=0, padx=35)
#Labels
ttk.Label(Frame3, background="#482525", text="Id product: ", foreground="white", font=("arial", 12, "bold" )).grid(column=0, row=1, sticky=(W), padx=10, pady=2)
ttk.Label(Frame3, background="#482525", text="Name: ", foreground="white", font=("arial", 12,"bold")).grid(column=0, row=2, sticky=(N, W), padx=10, pady=10)
ttk.Label(Frame3, background="#482525", text="Description: ", foreground="white", font=("arial", 12,"bold" )).grid(column=0, row=3, sticky=(N, W), padx=10, pady=10)
ttk.Label(Frame3, background="#482525", text="Quantity: ", foreground="white", font=("arial", 12 ,"bold")).grid(column=0, row=4, sticky=(N, W), padx=10, pady=10)
ttk.Label(Frame3, background="#482525", text="Price: ", foreground="white", font=("arial", 12,"bold")).grid(column=0, row=5, sticky=(N, W), padx=10, pady=10)
ttk.Label(Frame3, background="#482525", text="Back", foreground="SlateBlue",font=("verdana", 12, "bold")).grid(column=2, row=0, sticky=(N, E), padx=100, pady=2)

#Entrys
IDDato = IntVar()
NameDato = StringVar()
DescDato = StringVar()
QuantDato = IntVar()
PriceDato = float()

ttk.Label(Frame3, text="_________________________", background="#482525",foreground="white").grid(column=1, row=1, padx=5, pady=2, sticky=(W))
IDEntry = ttk.Entry(Frame3, background="#482525", textvariable=IDDato, width=20, justify="center")
IDEntry.grid(column=1, row=1, padx=5, sticky=(W,N))
IDEntry.configure(borderwidth=0)

ttk.Label(Frame3, text="_________________________", background="#482525",foreground="white").grid(column=1, row=2, padx=5, pady=2, sticky=(W))
NameDatoEntry= ttk.Entry(Frame3, background="#482525", textvariable=NameDato, width=20,justify="center")
NameDatoEntry.grid(column=1, row=2, padx=5,  pady=2, sticky=(W,N))
NameDatoEntry.configure(borderwidth=0)

ttk.Label(Frame3, text="_________________________", background="#482525",foreground="white").grid(column=1, row=3, padx=5, pady=2, sticky=(W))
DescDatoEntry = ttk.Entry(Frame3, background="#482525", textvariable=DescDato, width=20,justify="center")
DescDatoEntry.grid(column=1, row=3, padx=5,  pady=2, sticky=(W,N))
DescDatoEntry.configure(borderwidth=0)

ttk.Label(Frame3, text="_________________________", background="#482525",foreground="white").grid(column=1, row=4, padx=5, pady=2, sticky=(W))
QuantDatoEntry = ttk.Entry(Frame3, background="#482525", textvariable=QuantDato, width=20,justify="center")
QuantDatoEntry.grid(column=1, row=4, padx=5,  pady=2, sticky=(W,N))
QuantDatoEntry.configure(borderwidth=0)

ttk.Label(Frame3, text="_________________________", background="#482525",foreground="white").grid(column=1, row=5, padx=5, pady=2, sticky=(W))
PriceDatoEntry = ttk.Entry(Frame3, background="#482525", textvariable=PriceDato, width=20,justify="center")
PriceDatoEntry.grid(column=1, row=5, padx=5,  pady=2, sticky=(W,N))
PriceDatoEntry.configure(borderwidth=0)


#Botones Imagenes
image2 = PhotoImage(file="Lupa.png")

Boton1 = ttk.Button(Frame3,  background="#482525", activebackground="#482525")
Boton1.grid(column=2, row=0, padx=20, pady=10, sticky=(N, W))
Boton1['image'] = image2

image3 = PhotoImage(file="Limpiar.png")

Boton2 = ttk.Button(Frame3,  background="#482525", activebackground="#482525")
Boton2.grid(column=2, row=0, padx=60, pady=10 ,sticky=(N, W))
Boton2['image'] = image3

#Botones

Boton3 = ttk.Button(Frame3, background="Green4", text="Save",foreground="White", font=("verdana", 14, "bold"), anchor="center", width=12, activebackground="darkgreen").grid(column=2, row=2, sticky=(N, W), padx=10, pady=2)
Boton4 = ttk.Button(Frame3, background="red", text="Delete",foreground="White", font=("verdana", 14, "bold"), anchor="center", width=12 ,activebackground="red4").grid(column=2, row=3, sticky=(N, W), padx=10, pady=2)
Boton5 = ttk.Button(Frame3, background="darkOrange", text="Update",foreground="White", font=("verdana", 14, "bold"), anchor="center", width=12, activebackground="orange3").grid(column=2, row=4, sticky=(N, W), padx=10, pady=2)
Boton6 = ttk.Button(Frame3, background="#482525", text="Back", foreground="SlateBlue",font=("verdana", 12, "bold"), anchor="center",  activebackground="#482525", activeforeground="SlateBlue").grid(column=2, row=0, sticky=(N, E), padx=100, pady=5)

#--------------------CUARTO FRAME--------------------

#Definicion del frame que contendra la tabla
Frame4 = ttk.Frame(Frame2, background="#482525")
Frame4.grid(column=0, row=1, pady=10, padx=5)


# Crear encabezado de la tabla
ttk.Label(Frame4, text="idproduit", width=10, fg="gray30", bg="gray70").grid(row=0, column=0)
ttk.Label(Frame4, text="namep", width=20, fg="gray30",  bg="gray70").grid(row=0, column=1)
ttk.Label(Frame4, text="description", width=30, fg="gray30",  bg="gray70").grid(row=0, column=2)
ttk.Label(Frame4, text="quantity", width=10, fg="gray30",  bg="gray70").grid(row=0, column=3)
ttk.Label(Frame4, text="unite_price", width=10, fg="gray30", bg="gray70").grid(row=0, column=4)

# Crear datos de la tabla
data = [
    ("1", "Condia", "lait", "24", "100.0"),
    ("2", "la vache quirit", "fromage", "200", "300.0"),
    ("3", "bamoud boualam", "boisson gaseuse", "98", "90.0"),
    ("4", "Mina", "Chocolat","80","50.0"),
    ("5", "Aroma", "cafe","60","80.0"),
    ("6", "Facto", "Facto","7000","600.0")
]

# Mostrar datos en la tabla
for i, row in enumerate(data):
    for j, item in enumerate(row):
        ttk.Label(Frame4, text=item, width=10 if j == 0 else 20 if j == 1 else 30 if j == 2 else 10 if j == 3 else 10, bg="white").grid(row=i+1, column=j, sticky=(W))

root.mainloop()
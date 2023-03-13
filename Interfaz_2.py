from tkinter import *
import tkinter as ttk

#--------------------BASE FRAME--------------------
root = Tk()
root.geometry("600x440")
root.configure(background="gray40")

#imagen
image1 = PhotoImage(file="Compras.png")
imagenCarrito = ttk.Label(root, background="gray40")
imagenCarrito.grid(column=0, row=0, sticky=(W))
imagenCarrito['image'] = image1

#Label
ttk.Label(root, text="Product Management ", font=("verdana", 25, "bold"), foreground="white", background="gray40").grid(column=0, row=0, sticky=(W), padx=80)

#--------------------FRAMES--------------------

#--------------------PRIMER FRAME--------------------
Frame1 = ttk.Frame(root, background="gray2")
Frame1.grid(column=0, row=1)

#--------------------SEGUNDO FRAME--------------------
Frame2 = ttk.Frame(Frame1, background="#482525")
Frame2.grid(column=0, row=0, padx=50, pady=20)

#Labels
ttk.Label(Frame2, background="#482525", text="Id product: ", foreground="white", font=("arial", 12, "bold" )).grid(column=0, row=1, sticky=(W), padx=10, pady=2)
ttk.Label(Frame2, background="#482525", text="Name: ", foreground="white", font=("arial", 12,"bold")).grid(column=0, row=2, sticky=(N, W), padx=10, pady=2)
ttk.Label(Frame2, background="#482525", text="Description: ", foreground="white", font=("arial", 12,"bold" )).grid(column=0, row=3, sticky=(N, W), padx=10, pady=2)
ttk.Label(Frame2, background="#482525", text="Quantity: ", foreground="white", font=("arial", 12 ,"bold")).grid(column=0, row=4, sticky=(N, W), padx=10, pady=2)
ttk.Label(Frame2, background="#482525", text="Price: ", foreground="white", font=("arial", 12,"bold")).grid(column=0, row=5, sticky=(N, W), padx=10, pady=2)
ttk.Label(Frame2, background="#482525", text="Back", foreground="SlateBlue",font=("verdana", 12, "bold")).grid(column=2, row=0, sticky=(N, E), padx=100, pady=2)

#Entrys
IDDato = IntVar()
NameDato = StringVar()
DescDato = StringVar()
QuantDato = IntVar()
PriceDato = float()

IDEntry = ttk.Entry(Frame2, background="#482525", textvariable=IDDato, width=20).grid(column=1, row=1, padx=5, pady=2)
IDEntry = ttk.Entry(Frame2, background="#482525", textvariable=NameDato, width=20).grid(column=1, row=2, padx=5,  pady=2)
IDEntry = ttk.Entry(Frame2, background="#482525", textvariable=DescDato, width=20).grid(column=1, row=3, padx=5,  pady=2)
IDEntry = ttk.Entry(Frame2, background="#482525", textvariable=QuantDato, width=20).grid(column=1, row=4, padx=5,  pady=2)
IDEntry = ttk.Entry(Frame2, background="#482525", textvariable=PriceDato, width=20).grid(column=1, row=5, padx=5,  pady=2)


#Botones Imagenes
image2 = PhotoImage(file="Lupa.png")

Boton1 = ttk.Button(Frame2,  background="#482525", )
Boton1.grid(column=2, row=0, padx=20, pady=10, sticky=(N, W))
Boton1['image'] = image2

image3 = PhotoImage(file="Limpiar.png")

Boton2 = ttk.Button(Frame2,  background="#482525")
Boton2.grid(column=2, row=0, padx=60, pady=10 ,sticky=(N, W))
Boton2['image'] = image3

#Botones

Boton3 = ttk.Button(Frame2, background="Green4", text="Save",foreground="White", font=("verdana", 14, "bold"), anchor="center", width=12).grid(column=2, row=1, sticky=(N, W), padx=10, pady=5)
Boton4 = ttk.Button(Frame2, background="red", text="Delete",foreground="White", font=("verdana", 14, "bold"), anchor="center", width=12 ).grid(column=2, row=2, sticky=(N, W), padx=10, pady=5)
Boton5 = ttk.Button(Frame2, background="darkOrange", text="Update",foreground="White", font=("verdana", 14, "bold"), anchor="center", width=12 ).grid(column=2, row=3, sticky=(N, W), padx=10, pady=5)



#--------------------CUARTO FRAME--------------------

Frame3 = ttk.Frame(Frame2)
Frame3.grid(column=0 , row=6, sticky=(S), pady=30)

'''
#Definicion de la tabla
table = ttk.Treeview(Frame3)
table.grid(column=0, row=0)

#Tamaño del tupla
table["columns"] = ("ID","Name","Desc","Quan","Price")

#Columnas
table.column("#0", width=0, stretch=NO)
table.column("ID", width=120, anchor=W)
table.column("Name", width=120, anchor=W)
table.column("Desc", width=120, anchor=W)
table.column("Quan", width=120, anchor=W)
table.column("Price", width=120, anchor=W)

#Nombres de las cabeceras de las columnas 
table.heading("#0",text="")
table.heading("ID",text="idprodult")
table.heading("Name",text="namep")
table.heading("Desc",text="description")
table.heading("Quan",text="quantity")
table.heading("Price",text="unite_price")

#Agregar datos a las columnas
table.insert("", "end", text="1", values=("1", "Condia", "lait", "24", "100.0"))
table.insert("", "end", text="2", values=("2", "la vache quirit", "fromage", "200", "300.0"))
table.insert("", "end", text="3", values=("3", "bamound boualam", "boisson", "98", "90.0"))
table.insert("", "end", text="4", values=("4", "Mina", "Chocolat", "80", "50.0"))
table.insert("", "end", text="5", values=("5", "Aroma", "cafe", "60", "80.0"))
table.insert("", "end", text="6", values=("6", "Facto", "Facto", "7000", "600.0"))
'''

root.mainloop()
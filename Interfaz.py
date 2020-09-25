from tkinter import *
from tkinter import messagebox
import os 
import quest

resultado2 = False






#Fuciones
def crear_ventana(ventana):



		
	
	if ventana=="ver_productos":			#Crea la tabla de los productos

		ventana_productos = Toplevel()
		ventana_productos.title("Productos")
		ventana_productos.geometry("680x325")
		ventana_productos.iconbitmap(r"C:/Users/Programas Miguel/Desktop/Programas/Curso Python/Proyecto base de datos/icono.ico")

		Label_ID=Label(ventana_productos, text="ID").grid(row=0, column=0, sticky=W)
		Label_nombre=Label(ventana_productos, text="Nombre").grid(row=0, column=1, sticky=W)
		Label_precio=Label(ventana_productos, text="Precio").grid(row=0, column=2, sticky=W)
		Label_seccion=Label(ventana_productos, text="Sección").grid(row=0, column=3, sticky=W)
		Label_procendcia=Label(ventana_productos, text="Procedencia").grid(row=0, column=4, sticky=W)


		

		

		height = quest.contador_productos
		width = 5
		print(height)
		
		texto = StringVar()
		
		if height==0:
			entry = Entry(ventana_productos).grid(row=1, column=0)
			entry = Entry(ventana_productos).grid(row=1, column=1)
			entry = Entry(ventana_productos).grid(row=1, column=2)
			entry = Entry(ventana_productos).grid(row=1, column=3)
			entry = Entry(ventana_productos).grid(row=1, column=4)
			
		boton_borrar=Button(ventana_productos, text="Borrar").grid(row=1,column=5)
		for i in range(height): #Rows

			ID=None
			Nombre=None
			Precio=None
			Seccion=None
			Lugar=None
			ID, Nombre, Precio, Seccion, Lugar = quest.info_productos[i]

			print(ID,Nombre,Precio,Seccion,Lugar)

			for j in range(width): #Columns

				if j==0:
					texto=ID

				if j==1:
					texto=Nombre

				if j==2:
					texto=Precio

				if j==3:
					texto=Seccion

				if j==4:
					texto=Lugar

				entry = Entry(ventana_productos, textvariable=texto)
				entry.delete(0, END)
				entry.grid(row=i+1, column=j)
				entry.insert(0, texto)
				
			boton_borrar=Button(ventana_productos, text="Borrar").grid(row=i+1,column=6)

			
	
			


	if ventana=="ver_productos_pedidos":		#Crea la tabla de productos pedidos

		ventana_productos_pedidos = Toplevel()
		ventana_productos_pedidos.title("Productos pedidos")
		ventana_productos_pedidos.geometry("725x325")
		ventana_productos_pedidos.iconbitmap(r"C:/Users/Programas Miguel/Desktop/Programas/Curso Python/Proyecto base de datos/icono.ico")

	if ventana=="ver_clientes":			#Crea la tabla de los clientes

		ventana_clientes = Toplevel()
		ventana_clientes.title("Clientes")
		ventana_clientes.geometry("725x325")
		ventana_clientes.iconbitmap(r"C:/Users/Programas Miguel/Desktop/Programas/Curso Python/Proyecto base de datos/icono.ico")

def mensajes(mensaje): #Muestra mensajes llamdos desde quest.py
    global resultado2
    if mensaje=="Creacion":          #Mensaje de creación de base de datos
        messagebox.showinfo("Base de datos","La base de datos se creo exitosamente.")

    elif mensaje=="Ya creada":      #Mensaje de error al crear la base de datso
        messagebox.showerror("Base de datos","La base de datos ya ha sido creada con anterioridad.\nPara crear una nueva base de datos primero debera borrar esta.")

    elif mensaje=="Eliminacion":     #Pregunta de eleiminación de base de datos 
        resultado1=messagebox.askquestion("Base de datos","¿Ha elegido borrar la base de datos esta seguro?")
        if resultado1=="yes":           #Pregunta de eliminación de base de datos
            resultado2=messagebox.askquestion("Base de datos","¿Esta totalmente seguro, se borrrara toda la base de datos?", icon="warning")

    elif mensaje=="No esta":        #Muestra informacion de que no se puede borrar la base de datos porque no existe
        messagebox.showerror("Base de datos","No se puede borrar la base de datos porque no existe.")   

    elif mensaje=="No se creo":     #Muestra un error de que no se puede ver la base de datos porque no se creo
        messagebox.showerror("Base de datos","No se puede ver la base de datos porque no se ha creado")


#Funciones





#Propiedades de la ventana
def window():
	window = Tk()
	window.title("Base de datos")
	window.resizable(False,False)
	window.geometry("280x400")
	window.iconbitmap(r"C:/Users/Programas Miguel/Desktop/Programas/Curso Python/Proyecto base de datos/icono.ico")

	img = PhotoImage(file="C:\\Users\\Programas Miguel\\Desktop\\Programas\\Curso Python\\Proyecto base de datos\\Imagen.png")
	panel = Label(window, image = img)
	panel.pack(side = "bottom", fill = "both", expand = "yes")
	#Menu
	barra_menu=Menu(window)
	window.config(menu=barra_menu)

	ver=Menu(barra_menu, tearoff=0)

	barra_menu.add_cascade(label="Ver", menu=ver)         #Ver
	ver.add_command(label="Productos", command=quest.ver_productos)    #Productos
	ver.add_command(label="Clientes", command=quest.ver_clientes)     #Clientes
	ver.add_command(label="Productos pedidos", command=quest.ver_productos_pedidos)     #Productos pedidos


	base_de_datos=Menu(barra_menu, tearoff=0)

	barra_menu.add_cascade(label="Base de datos", menu=base_de_datos)
	base_de_datos.add_command(label="Crear DB", command=quest.crear_db)     #Crear base de datos
	base_de_datos.add_separator()
	base_de_datos.add_command(label="Eliminar DB", command=quest.borrar_db)     #Borrar base de datos

	Salir=Menu(barra_menu, tearoff=0)

	barra_menu.add_cascade(label="Salir", menu=Salir)          #Eliminar ventana
	Salir.add_command(label="Salir", command=window.quit)


	#Menu

	#Propiedades de la ventana

	window.mainloop()


   
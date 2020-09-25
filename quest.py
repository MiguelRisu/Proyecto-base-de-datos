import sqlite3 as sql
import sys
import os
import Interfaz

info_productos=None
info_productos_pedidos=None
info_clientes=None
contador_productos=0
contador_productos_pedidos=0
contador_clientes=0
ruta=os.path.abspath("DATOS")
existe=os.path.isfile(ruta)
print(existe)



def crear_db():
    global existe

    ruta=os.path.abspath("DATOS")
    existe=os.path.isfile(ruta) #Saber si existe la base de datos
    print(existe)
    if existe==False:
        

        miconexion=sql.connect("DATOS")
        

        mi_cursor=miconexion.cursor()
        #TABLA CLIENTES
        mi_cursor.execute('''CREATE TABLE CLIENTES(
        ID_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(30), 
        APELLIDOS VARCHAR(55), 
        EDAD TINYINT, 
        CORREO VARCHAR(100),
        LOCALIDAD VARCHAR(35))
        ''')
        #TABLA CLIENTES
        #TABLA PRODUCTOS
        mi_cursor.execute('''CREATE TABLE PRODUCTOS(
        ID_PRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE_PRODUCTOS VARCHAR(150),
        PRECIO FLOAT,
        SECCION VARCHAR(35),
        LUGAR_DE_PROCEDENCIA VARCHAR(35)
        )''')
        #TABLA PRODUCTOS
        #TABLA PRODUCTOS_PEDIDOS
        mi_cursor.execute('''CREATE TABLE PRODUCTOS_PEDIDOS(
        ID_PEDIDO INTEGER PRIMARY KEY AUTOINCREMENT,
        NUMERO_DE_PEDIDOS INTEGER
        )''')
        #TABLA PRODUCTOS PEDIDOS

        miconexion.commit()

        miconexion.close()

        Interfaz.mensajes("Creacion")

    else:
        Interfaz.mensajes("Ya creada")

def borrar_db():
   ruta=os.path.abspath("DATOS")
   existe=os.path.isfile(ruta) #Saber si existe la base de datos
   

   if existe==True:  #Si existe borra la base de datos
       Interfaz.mensajes("Eliminacion")
       if Interfaz.resultado2=="yes":
           os.remove(ruta)
   else:                    #Si no esta muestra mensaje de que no esta
        Interfaz.mensajes("No esta")
       

       

def ver_clientes():

    
    if existe:
            
        global info_clientes
        global contador_clientes


        miconexion=sql.connect("DATOS")

        mi_cursor=miconexion.cursor()

        mi_cursor.execute("SELECT * FROM CLIENTES")

        info_clientes=mi_cursor.fetchall()

        miconexion.commit()

        miconexion.close()

        Interfaz.crear_ventana("ver_clientes")

    else:
        Interfaz.mensajes("No se creo")

            


def ver_productos():

    if existe:

        global info_productos
        global contador_productos


        miconexion=sql.connect("DATOS")
        
        mi_cursor=miconexion.cursor()

        mi_cursor.execute("SELECT * FROM PRODUCTOS")

        info_productos=mi_cursor.fetchall()

        miconexion.commit()

        miconexion.close()

        contador_productos=len(info_productos)

        Interfaz.crear_ventana("ver_productos")
        
        print(info_productos)

        print(contador_productos)

    else: 
        Interfaz.mensajes("No se creo")
   


    

def ver_productos_pedidos():

    if existe:

        global info_productos_pedidos
        global contador_productos_pedidos


        miconexion=sql.connect("DATOS")
        
        mi_cursor=miconexion.cursor()

        mi_cursor.execute('''SELECT * FROM PRODDUCTOS_PEDIDOS''')

        info_productos_pedidos=mi_cursor.fetchall()

        miconexion.commit()

        miconexion.close()

        print(info_productos_pedidos)

        Interfaz.crear_ventana("ver_productos_pedidos")

    else:
        Interfaz.mensajes("No se creo")

    

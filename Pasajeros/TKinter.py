import tkinter as tk
from tkinter import ttk
import sqlite3
import sys

def conectar():
    try:
        conexion= sqlite3.connect("pasajeros.sql")
        conexion.row_factory= sqlite3.Row
        return conexion    
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        sys.exit(1)
        
def crear_tabla():
    conexion= conectar()
    cursor= conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pasajeros
    (DNI INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Fecha_nac TEXT NOT NULL,
    Telefono INTEGRER,
    Mail TEXT NOT NULL,
    Paquete INTEGRER TEXT NOT NULL)''')
    conexion.commit()
    conexion.close() 
    print("Tabla 'pasajeros' verificada/creada.")
    
    
class Pasajero():
    def __init__(self, DNI, nombre, fecha_nac, telefono, mail, paquete):
        self.DNI= DNI
        self.nombre= nombre
        self.fecha_nac= fecha_nac
        self.telefono= telefono
        self.mail= mail
        self.paquete= paquete
    
def guardar(pasajero):
    conexion= conectar()
    cursor= conexion.cursor()
    try:
        cursor.execute("INSERT INTO pasajeros (DNI, Nombre, Fecha_nac, Telefono, Mail, Paquete) VALUES (?, ?, ?, ?, ?, ?)",
        (pasajero.DNI, pasajero.nombre, pasajero.fecha_nac, pasajero.telefono,pasajero.mail, pasajero.paquete))
        conexion.commit()
        print(f"Pasajero '{nombre}' agregado con éxito.")           
    except sqlite3.Error as e:
        print(f"Error al agregar pasajero: {e}")
    finally:
        conexion.close()
        
def listar():
    conexion= conectar()
    cursor= conexion.cursor()
    lista_pasajeros= []
    try:
        cursor.execute("SELECT * FROM pasajeros")
        lista_pasajeros= cursor.fetchall()
        conexion.close()
    except:
        print("La tabla no existe.")
    return lista_pasajeros

def modificar(pasajero, DNI):
    conexion= conectar()
    cursor= conexion.cursor()
    sql= f"""UPDATE pasajeros SET Nombre= '{pasajero.nombre}', Fecha_nac= '{pasajero.fecha_nac}', Telefono= '{pasajero.telefono}', 
        Mail= '{pasajero.mail}, Paquete= '{pasajero.paquete}' WHERE DNI= '{DNI}'"""
    
    try:
        cursor.execute(sql)            
        conexion.commit()
        conexion.close()
    except:
        print("No se pudo editar el registro.")
       
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Base de datos pasajeros")
        self.geometry("500x500")
        self.datos()
        self.habilitar()
        self.deshabilitar()
        self.guardar()
        self.tabla_pasajeros()
        self.editar()

    def datos(self):
        #Etiquetas        
        self.etiqueta1= tk.Label(self, text= "DNI: ")
        self.etiqueta1.grid(row= 0, column= 0, padx= 10, pady= 5)
        self.etiqueta2= tk.Label(self, text= "Nombre: ")
        self.etiqueta2.grid(row= 1, column= 0, padx= 5, pady= 5)
        self.etiqueta3= tk.Label(self, text= "Fecha de nacimiento: ")
        self.etiqueta3.grid(row= 2, column= 0, padx= 10, pady= 5)
        self.etiqueta4= tk.Label(self, text= "Teléfono: ")
        self.etiqueta4.grid(row= 3, column= 0, padx= 5, pady= 5)
        self.etiqueta5= tk.Label(self, text= "Mail: ")
        self.etiqueta5.grid(row= 4, column= 0, padx= 5, pady= 5)
        self.etiqueta6= tk.Label(self, text= "Paquete: ")
        self.etiqueta6.grid(row= 5, column= 0, padx= 5, pady= 5)       
                
        #Entrys
        self.dni= tk.StringVar()
        self.texto1= tk.Entry(self, textvariable= self.dni)
        self.texto1.grid(row= 0, column= 1, padx= 5, pady= 5)
        self.nombre= tk.StringVar()
        self.texto2= tk.Entry(self, textvariable= self.nombre)
        self.texto2.grid(row= 1, column= 1, padx= 5, pady= 5)
        self.fecha= tk.StringVar()
        self.texto3= tk.Entry(self, textvariable= self.fecha)
        self.texto3.grid(row= 2, column= 1, padx= 5, pady= 5)
        self.telefono= tk.StringVar()
        self.texto4= tk.Entry(self, textvariable= self.telefono)
        self.texto4.grid(row= 3, column= 1, padx= 5, pady= 5)
        self.mail= tk.StringVar()    
        self.texto5= tk.Entry(self, textvariable= self.mail)
        self.texto5.grid(row= 4, column= 1, padx= 5, pady= 5)
        self.paquete= tk.StringVar()
        self.texto6= tk.Entry(self, textvariable= self.paquete)
        self.texto6.grid(row= 5, column= 1, padx= 5, pady= 5)
        
        #Botones
        self.boton1= tk.Button(self, text= "Agregar pasajero", command= self.habilitar)
        self.boton1.grid(row= 6, column= 0)
        self.boton2= tk.Button(self, text= "Modificar pasajero", command= self.editar)
        self.boton2.grid(row= 6, column= 1)
        self.boton3= tk.Button(self, text= "Eliminar pasajero")
        self.boton3.grid(row= 6, column= 2)
        self.boton6= tk.Button(self, text= "Salir")
        self.boton6.grid(row= 8, column= 2)
        
    def habilitar(self):
        self.texto1.config(state= 'normal')
        self.texto2.config(state= 'normal')
        self.texto3.config(state= 'normal')
        self.texto4.config(state= 'normal')
        self.texto5.config(state= 'normal')
        self.texto6.config(state= 'normal')
        
        self.boton1.config(state= 'normal')
        self.boton2.config(state= 'normal')
        self.boton3.config(state= 'normal')
        self.boton4.config(state= 'normal')
        self.boton5.config(state= 'normal')
        
    def deshabilitar(self):
        self.dni.set('')
        self.nombre.set('')
        self.fecha.set('')
        self.telefono.set('')
        self.mail.set('')
        self.paquete.set('')
        
        self.texto1.config(state= 'disabled')
        self.texto2.config(state= 'disabled')
        self.texto3.config(state= 'disabled')
        self.texto4.config(state= 'disabled')
        self.texto5.config(state= 'disabled')
        self.texto6.config(state= 'disabled')
        
        self.boton4.config(state= 'disabled')
        self.boton5.config(state= 'disabled')
        
    def guardar(self):
        pasajero= Pasajero(
            self.dni.get(),
            self.nombre.get(),
            self.fecha.get(),
            self.telefono.get(),
            self.mail.get(),
            self.paquete.get(),)
        guardar(pasajero)
        self.tabla_pasajeros()
        self.deshabilitar()

    def tabla_pasajeros(self):
        self.lista_pasajeros= listar()
        self.lista_pasajeros.reverse()
        self.tabla= ttk.Treeview(self, column= ('DNI', 'Nombre', 'Fecha de nacimiento', 'Telefono', 'Mail', 'Paquete'))
        self.tabla.grid(row= 7, column= 0, columnspan= 6, padx= 10, pady= 10)
        self.tabla.heading('#0', text= 'DNI')
        self.tabla.heading('#1', text= 'Nombre')
        self.tabla.heading('#2', text= 'Fecha de nacimiento')
        self.tabla.heading('#3', text= 'Telefono')
        self.tabla.heading('#4', text= 'Mail')
        self.tabla.heading('#5', text= 'Paquete')
        
        for p in self.lista_pasajeros:
            self.tabla.insert('', 0, text= p[0],
            values= (p[1], p[2], p[3], p[4], p[5]))
            
    def editar(self):
        try:
            self.dni= self.tabla.item(self.tabla_pasajeros.selection())['text']
            self.nombre= self.tabla.item(self.tabla_pasajeros.selection())['values'][1]
            self.fecha= self.tabla.item(self.tabla_pasajeros.selection())['values'][2]
            self.telefono= self.tabla.item(self.tabla_pasajeros.selection())['values'][3]
            self.mail= self.tabla.item(self.tabla_pasajeros.selection())['values'][4]
            self.paquete= self.tabla.item(self.tabla_pasajeros.selection())['values'][5]
            self.habilitar()
            
            self.texto1.insert(0, self.dni)
            self.texto2.insert(1, self.nombre)
            self.texto3.insert(2, self.fecha)
            self.texto4.insert(3, self.telefono)
            self.texto5.insert(4, self.mail)
            self.texto6.insert(5, self.paquete)
        except:
            print("No ha seleccionado ningún registro.")
    
if __name__ == "__main__":
    app= Aplicacion()
    app.mainloop()
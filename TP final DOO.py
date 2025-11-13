import sqlite3
import sys
import tkinter as tk
from tkinter import ttk

#1. Conexión a la base de datos
def conectar():
    try:
        conexion= sqlite3.connect("pasajeros.sql")
        conexion.row_factory= sqlite3.Row
        return conexion    
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        sys.exit(1)

#2. Creamos la tabla
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
    
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Base de datos pasajeros")
        self.geometry("500x500")
        
        #Creación y disposición de widgets
        self.boton1= ttk.Button(self, text= "Alta pasajero", command= self.alta)
        self.boton1.pack(pady= 10)
        self.boton2= ttk.Button(self, text= "Listar pasajeros", command= self.lista)
        self.boton2.pack(pady= 10)
        self.boton3= ttk.Button(self, text= "Modificar datos", command= self.modificar)
        self.boton3.pack(pady= 10)
        self.boton4= ttk.Button(self, text= "Baja pasajero", command= self.baja)
        self.boton4.pack(pady= 10)
        self.boton5= ttk.Button(self, text= "Salir", command= self.salir)
        self.boton5.pack(pady= 10)    
        
#---Funciones ABM---
#3. Alta de pasajero:
    def alta(self):
        crear_tabla()
        try:
            DNI= int(input("Ingrese el DNI del pasajero: "))
        except ValueError:
            print("Debe ingresar un número de hasta 8 cifras.")
            return
        nombre= input("Ingrese nombre y apellido del pasajero: ")
        fecha_nac= input("Ingrese fecha de nacimiento del pasajero: ")
        try:
            telefono= int(input("Ingrese el teléfono del pasajero: "))
        except ValueError:
            print("Debe ingresar un número de 10 cifras.")
            return
        mail= input("Ingrese el mail del pasajero: ")
        try:
            paquete= int(input("Ingrese el ID del paquete elegido por el pasajero: "))
        except ValueError:
            print("Debe ingresar un número del 1 al 6.")
            return
        conexion= conectar()
        cursor= conexion.cursor()

        try:
            cursor.execute("INSERT INTO pasajeros (DNI, Nombre, Fecha_nac, Telefono, Mail, Paquete) VALUES (?, ?, ?, ?, ?, ?)",
            (DNI, nombre, fecha_nac, telefono, mail, paquete))
            conexion.commit()
            print(f"Pasajero '{nombre}' agregado con éxito.")        
        except sqlite3.Error as e:
            print(f"Error al agregar empleado: {e}")
        finally:
            conexion.close()
            
    #4. Lista de pasajeros
    def lista(self):
        crear_tabla()
        conexion= conectar()
        cursor= conexion.cursor()
        cursor.execute("SELECT * FROM pasajeros")
        pasajeros= cursor.fetchall()
        conexion.close()
            
        if not pasajeros:
            print("No hay pasajeros registrados.")
            return
            
        print("\n---Lista de pasajeros ---")
        for pax in pasajeros:
            print(f"DNI: {pax['DNI']} | Nombre: {pax['nombre']} | Fecha de nacimiento: {pax['fecha_nac']} | Telefono: {pax['telefono']} | Mail: {pax['mail']} | Paquete: {pax['paquete']}")
        print("---------------------------\n")

    #5. Modificación de datos
    def modificar_telefono(self):
        crear_tabla()
        self.lista()
        pax_id= input("Ingrese DNI del pasajero a modificar: ")
        conexion= conectar()
        cursor= conexion.cursor()
        cursor.execute("SELECT * FROM pasajeros WHERE DNI= ?", (pax_id,))
            
        pasajero_existente= cursor.fetchone()
        if not pasajero_existente:
            print(f"No se encontró un pasajero con DNI {pax_id}.")
            conexion.close()
            return

        try:
            nuevo_telefono= int(input(f"Ingrese el nuevo telefono de {pasajero_existente['nombre']} (actual: {pasajero_existente['telefono']}): "))
        except ValueError:
            print("Debe ser un número de 10 cifras.")
            conexion.close()
            return
            
        try:
            cursor.execute("UPDATE pasajeros SET Telefono= ? WHERE DNI= ?", (nuevo_telefono, pax_id))
            conexion.commit()
            print("Telefono actualizado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al modificar telefono: {e}")
        finally:
            conexion.close()
            
    def modificar_mail(self):
        crear_tabla()
        self.lista()
        pax_id= input("Ingrese DNI del pasajero a modificar: ")
        conexion= conectar()
        cursor= conexion.cursor()
        cursor.execute("SELECT * FROM pasajeros WHERE DNI= ?", (pax_id,))
            
        pasajero_existente= cursor.fetchone()
        if not pasajero_existente:
            print(f"No se encontró un pasajero con DNI {pax_id}.")
            conexion.close()
            return

        nuevo_mail= (input(f"Ingrese el nuevo mail de {pasajero_existente['nombre']} (actual: {pasajero_existente['mail']}): "))
        try:
            cursor.execute("UPDATE pasajeros SET Mail= ? WHERE DNI= ?", (nuevo_mail, pax_id))
            conexion.commit()
            print("Mail actualizado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al modificar mail: {e}")
        finally:
            conexion.close()
                
    def modificar(self):
        crear_tabla()
        while True:
            print("a. Modificar teléfono")
            print("b. Modificar mail")
                   
            opcion2= input("Seleccione una opción: ")
            if opcion2 == 'a':
                self.modificar_telefono()
            elif opcion2 == 'b':
                self.modificar_mail()
                break
            else:
                 print("Opción incorrecta.")
    
    #6. Baja de pasajeros
    def baja(self):
        crear_tabla()
        self.lista()
        pax_id = input("Ingrese el DNI del pasajero a eliminar: ")
        conexion= conectar()
        cursor= conexion.cursor()

        try:
            cursor.execute("DELETE FROM pasajeros WHERE DNI= ?", (pax_id,))
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"Pasajero con DNI {pax_id} eliminado correctamente.")
            else:
                print(f"No se encontró un pasajero con DNI {pax_id}.")
        except sqlite3.Error as e:
            print(f"Error al eliminar pasajero: {e}")
        finally:
            conexion.close()
            
    #7. Salir
    def salir(self):
        print("¡Hasta luego!")
        
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
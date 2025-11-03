import sqlite3
import sys

#1. Conexión a la base de datos
def get_connection():
    try:
        conexion= sqlite3.connect("pasajeros.sql")
        conexion.row_factory = sqlite3.Row
        return conexion
    
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        sys.exit(1)

#2. Creamos la tabla
def crear_tabla():
    conexion= get_connection()
    cursor= conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pasajeros
    (DNI INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Fecha_nac TEXT NOT NULL,
    Telefono INTEGRER,
    Mail TEXT NOT NULL,
    Paquete INTEGRER)''')    
    conexion.commit()
    conexion.close()
    print("Tabla 'pasajeros' verificada/creada.")

#---Funciones ABM---
class Pasajeros:
    def __init__(self):
        pass
    
    def alta(self):
        try:
            DNI= int(input("Ingrese DNI del pasajero: "))
        except ValueError:
            print("Debe agregar un número.")
            return
        nombre= input("Ingrese nombre y apellido del pasajero: ")
        fecha_nac= input("Ingrese fecha de nacimiento del pasajero: ")
        try:
            telefono= int(input("Ingrese telefono del pasajero: "))
        except ValueError:
            print("Debe agregar un número.")
            return
        mail= input("Ingrese mail del pasajero: ")
        try:
            paquete= int(input("Ingrese código del paquete elegido por el pasajero: "))
        except ValueError:
            print("Debe agregar un número.")
            return
        conexion= get_connection()
        cursor= conexion.cursor()
    
        try:
            cursor.execute("INSERT INTO pasajeros (DNI, Nombre, Fecha_nac, Telefono, Mail, Paquete) VALUES (?, ?, ?, ?, ?, ?)",
            (DNI, nombre, fecha_nac, telefono, mail, paquete))
            conexion.commit()
            print(f"Pasajero '{nombre}' agregado con éxito.")        
        except sqlite3.Error as e:
            print(f"Error al agregar pasajero: {e}")
        finally:
            conexion.close()

    def lista(self):
        conexion= get_connection()
        cursor= conexion.cursor()
        cursor.execute("SELECT * FROM pasajeros")
        pasajeros= cursor.fetchall()
        conexion.close()
        if not pasajeros:
            print("No hay pasajeros registrados.")
            return
    
#Accediendo a los datos por nombre de columna gracias a row_factory
        print("\n---Lista de pasajeros ---")
        for pax in pasajeros:
            print(f"DNI: {pax['DNI']} | Nombre: {pax['nombre']} | Fecha de nacimiento: {pax['fecha_nac']} | Telefono: {pax['telefono']} | Mail: {pax['mail']} | Paquete: {pax['paquete']}")
        print("---------------------------\n")
    
    def modificar_telefono(self):
        self.lista()
        pax_id= input("Ingrese DNI del pasajero a modificar: ")
        conexion= get_connection()
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
            print("Debe ser un número.")
            conexion.close()
            return
        try:
            cursor.execute("UPDATE pasajeros SET Telefono= ? WHERE DNI= ?", (nuevo_telefono, pax_id))
            conexion.commit()
            print("telefono actualizado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al modificar telefono: {e}")
        finally:
            conexion.close()
            
    def modificar_mail(self):
        self.lista()
        pax_id= input("Ingrese DNI del pasajero a modificar: ")
        conexion= get_connection()
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
            print(f"Error al modificar Mail: {e}")
        finally:
            conexion.close()    
        
    def baja(self):
        self.lista()
        pax_id = input("Ingrese el DNI del pasajero a eliminar: ")
        conexion= get_connection()
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

#--- Menú Principal ---
    def menu(self):
        while True:
            print("\n---Sistema ABM Pasajeros ---")
            print("1. Alta pasajero")
            print("2. Listar pasajeros")
            print("3. Modificar datos")
            print("4. Baja pasajero")
            print("5. Salir")
            
            opcion= input("Seleccione una opción: ")
            if opcion== '1':
                self.alta()
            elif opcion== '2':
                self.lista()
            elif opcion== '3':
                while True:
                    print("¿Qué dato desea modificar?")
                    print("a. Teléfono")
                    print("b. Mail")
                    
                    opcion2= input("Seleccione una opción: ")
                    if opcion2== 'a':
                        self.modificar_telefono()
                    elif opcion2== 'b':
                        self.modificar_mail()
                        break
                    else:
                        print("Opción incorrecta.")
            elif opcion== '4':
                self.baja()
            elif opcion== '5':
                print("¡Gracias!")
                break
            else:
                print("Opción incorecta.")

pasajero= Pasajeros()
pasajero.menu()
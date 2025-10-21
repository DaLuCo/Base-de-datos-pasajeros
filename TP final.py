import sqlite3
conexion= None

try:
    conexion= sqlite3.connect("Base de datos pax.db")
    cursor= conexion.cursor()
    cursor.execute("Select SQLite_version()")
    datos= cursor.fetchone()
except sqlite3.Error as e:
    print("Error %s: " %e.args [0])
finally:
    if conexion:
        conexion.close()

class Pasajeros:
    def __init__(self):
        self.nombre= input("Ingrese nombre y apellido del pasajero: ")
        self.DNI= input("Ingrese DNI del pasajero: ")
        self.fecha_nac= input("Ingrese fecha de nacimiento del pasajero: ")
        self.telefono= int(input ("Ingrese número de telefono del pasajero: "))
        self.mail= input("Ingrese mail del pasajero: ")        
        self.paquete= input("Seleccione el paquete que le guste: ")
        
        print(self.nombre)
        print("{};".format(self.DNI))
        print(self.fecha_nac)
        print(self.telefono)
        print(self.mail)
        print(self.paquete)

pasajero= Pasajeros()

conexion= sqlite3.connect("Base de datos pax.db")
with conexion:
    cursor= conexion.cursor()
Lista_pasajeros= []
id_pasajeros= 0
for pasajeros in Lista_pasajeros:
    cursor.execute("Agregar en Pasajeros", (id_pasajeros, Pasajeros.nombre, Pasajeros.DNI, Pasajeros. fecha_nac, Pasajeros.telefono,
    Pasajeros.mail, Pasajeros.paquete))
id_pasajeros+=1
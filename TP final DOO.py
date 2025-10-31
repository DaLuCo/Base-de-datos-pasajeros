import sqlite3
conexion= None

try:
    conexion= sqlite3.connect("Base de datos pax.sql")
    cursor= conexion.cursor()
    
except sqlite3.Error as e:
    print("Error %s:" %e.args [0])

finally:
    if conexion:
        conexion.close()

class Pasajeros:
    def __init__(self):
        self.DNI= int(input("Ingrese DNI del pasajero: "))
        self.nombre= input("Ingrese nombre y apellido del pasajero: ")
        self.fecha_nac= input("Ingrese fecha de nacimiento del pasajero: ")
        self.telefono= int(input ("Ingrese número de telefono del pasajero: "))
        self.mail= input("Ingrese mail del pasajero: ")    
        self.paquete= int(input("Seleccione el paquete que le guste: "))

pasajero= Pasajeros()

conexion= sqlite3.connect("Base de datos pax.sql")
with conexion:
    cursor= conexion.cursor()

#Recuperar registros:
cursor.execute("SELECT * FROM Pasajeros")
lineas= cursor.fetchall()
for linea in lineas:
    print(linea)

#Agregar registros:
cursor.execute("INSERT INTO Pasajeros (DNI, Nombre, Fecha de nacimiento, Telefono, Mail, Paquete) VALUES (?, ?, ?, ?, ?, ?)",
(pasajero.DNI, pasajero.nombre, pasajero.fecha_nac, pasajero.telefono, pasajero.mail, pasajero.paquete))
conexion.commit()
print(Pasajeros)

#Modificar un registro:
cursor.execute("UPDATE Pasajeros SET Mail= daniela.comes@outlook.com WHERE Nombre= Daniela Comes", ("danielacomes.dlc@gmail.com", pasajero.nombre))
conexion.commit()
print("Registro actualizado.")

#Borrar un registro:
cursor.executescript("DELETE FROM Pasajeros WHERE DNI= self.DNI= 33741053")
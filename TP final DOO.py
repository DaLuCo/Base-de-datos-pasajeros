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
        self.nombre= input("Ingrese nombre y apellido del pasajero: ")
        self.DNI= int(input("Ingrese DNI del pasajero: "))
        self.fecha_nac= input("Ingrese fecha de nacimiento del pasajero: ")
        self.telefono= int(input ("Ingrese número de telefono del pasajero: "))
        self.mail= input("Ingrese mail del pasajero: ")        
        self.paquete= input("Seleccione el paquete que le guste: ")                

pasajero= Pasajeros()

conexion= sqlite3.connect("Base de datos pax.sql")
with conexion:
    cursor= conexion.cursor()

#Ejecución del script SQL:
Lista_pax= 0
id_pasajeros= 0
for pasajeros in Lista_pax:
    cursor.execute("INSERT INTO Base de datos pax VALUES()", (id_pasajeros, pasajeros.nombre, pasajeros.DNI, pasajeros. fecha_nac, pasajeros.telefono,
    pasajeros.mail, pasajeros.paquete))
id_pasajeros+= 1

#Recuperar los registros:
cursor.execute ("SELECT * FROM Base de datos pax")
lineas= cursor.fetchall()
for linea in lineas:
    print (linea)

#Modificar un campo:
cursor.execute("UPDATE Base de datos pax SET mail WHERE nombre")
conexion. commit()
print("Numero de lineas actualizadas: %d" % cursor.rowcount)

#Eliminar un registro:
cursor.execute("DELETE FROM Base de datos pax WHERE ID= 2")
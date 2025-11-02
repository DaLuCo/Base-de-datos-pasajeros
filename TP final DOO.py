#1. Conexión a la base de datos
import sqlite3
try:
    conexion= sqlite3.connect('pasajeros.db')
    cursor = conexion.cursor()
    print("Conexión a la base de datos establecida.")
    
#2. Creación de la tabla
    cursor.execute('''CREATE TABLE IF NOT EXISTS pasajeros
                  (DNI INTEGER PRIMARY KEY,
                   Nombre TEXT NOT NULL,
                   Fecha_nac TEXT NOT NULL,
                   Telefono INTEGER NOT NULL,
                   Mail TEXT NOT NULL,
                   Paquete INTEGER)''')
    print("Tabla 'pasajeros' verificada/creada.")
        
    class Pasajeros:
        def __init__(self):
            self.DNI= int(input("Ingrese DNI del pasajero: "))
            self.nombre= input("Ingrese nombre y apellido del pasajero: ")
            self.fecha_nac= input("Ingrese fecha de nacimiento del pasajero: ")
            self.telefono= int(input("Ingrese telefono del pasajero: "))
            self.mail= input("Ingrese mail del pasajero: ")
            self.paquete= int(input("Ingrese código del paquete: "))
        
    pasajero= Pasajeros()
        
#3. Insertar datos        
    cursor.execute("INSERT INTO pasajeros (DNI, Nombre, Fecha_nac, Telefono, Mail, Paquete) VALUES (?, ?, ?, ?, ?, ?)", 
    (pasajero.DNI, pasajero.nombre, pasajero.fecha_nac, pasajero.telefono, pasajero.mail, pasajero.paquete))
        
#4. Consultar y mostrar todos los registros
    print("\n---Base de datos pasajeros---")
    cursor.execute("SELECT DNI, Nombre, Fecha_nac, Telefono, Mail, Paquete FROM pasajeros")
    registros= cursor.fetchall()

    for fila in registros:
        print(f"DNI: {fila[0]}, Nombre: {fila[1]}, Fecha_nac: {fila[2]}, Telefono: {fila[3]}, Mail: {fila[4]}, Paquete: {fila[5]}")

except sqlite3.Error as e:
        print(f"Ocurrió un error con SQLite: {e}")

#5. Cerrar la conexión
finally:
    if conexion:
        conexion.close()
        print("\nConexión a la base de datos cerrada.")
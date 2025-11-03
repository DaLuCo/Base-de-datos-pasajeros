import sqlite3
#1. Conexión a la base de datos
try:
    conexion= sqlite3.connect('pasajeros.sql')
    cursor = conexion.cursor()
    print("Conexión a la base de datos establecida.")
        
#2. Creamos una tabla
    cursor.execute('''CREATE TABLE IF NOT EXISTS paquetes
                  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   Nombre_paq TEXT NOT NULL,
                   Descripcion TEXT NOT NULL,
                   Precio INTEGER)''')
    print("Tabla 'paquetes' verificada/creada.")

#3. Insertar datos
    Lista_paquetes= [
    ('Ushuaia + Calafate', 'Incluye aéreos, alojamiento, traslados y excursiones', "$ {:,}".format(1000000)),
    ('Salta', 'Incluye aéreos, alojamiento, traslados y excursiones', "$ {:,}".format(800000)),
    ('Mendoza', 'Incluye aéreos, alojamiento, traslados y excursiones', "$ {:,}".format(600000)),
    ('Rio de Janeiro', 'Incluye aéreos y alojamiento', "$ {:,}".format(500000)),
    ('Punta del Este', 'Incluye aéreos y alojamiento', "$ {:,}".format(1000000))]
    cursor.executemany("INSERT INTO paquetes (Nombre_paq, Descripcion, Precio) VALUES (?, ?, ?)", Lista_paquetes)
    conexion.commit()
    print("Datos insertados y confirmados.")

#4. Consultar y mostrar todos los registros
    print("\n---Paquetes---")
    cursor.execute("SELECT Nombre_paq, Descripcion, Precio FROM paquetes")
    registros= cursor.fetchall()
    for fila in registros:
       print(f"Nombre_paq: {fila[0]}, Descripcion: {fila[1]}, Precio: {fila[2]}")
    print("Total de viajes: ", len(Lista_paquetes))

except sqlite3.Error as e:
    print(f"Ocurrió un error con SQLite: {e}")
    
#5. Cerrar la conexión
finally:
    if conexion:
        conexion.close()
        print("\nConexión a la base de datos cerrada.")
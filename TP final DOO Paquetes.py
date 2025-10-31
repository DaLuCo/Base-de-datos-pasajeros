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

class Paquetes: 
    def __init__(self,paquete, descripcion, precio):
        self.paquete= paquete
        self.descripcion= descripcion
        self.precio= "${:,}".format(precio)
        
paquete1= Paquetes("Ushuaia + Calafate", "Alojamiento, aéreos, excursiones y traslados", 1000000)
paquete2= Paquetes("Salta", "Alojamiento, aéreos, excursiones y traslados", 500000)
paquete3= Paquetes("Mendoza", "Alojamiento, aéreos, excursiones y traslados", 800000)
paquete4= Paquetes("Rio de Janeiro", "Alojamiento y aéreos", 500000)
paquete5= Paquetes("Punta del Este", "Alojamiento y aéreos", 1000000)

conexion= sqlite3.connect("Base de datos pax.sql")
cursor= conexion.cursor()

#Recorremos la lista de paquetes:
Lista_paquetes= [paquete1, paquete2, paquete3, paquete4, paquete5]
for paquetes in Lista_paquetes:
    cursor.execute("INSERT INTO Paquetes (Paquete, Descripcion, Precio) VALUES (?, ?, ?)",
    (paquetes.paquete, paquetes.descripcion, paquetes.precio))
    
cursor.execute("SELECT * FROM Paquetes")
lineas= cursor.fetchall()

for linea in  lineas:
    print(linea)
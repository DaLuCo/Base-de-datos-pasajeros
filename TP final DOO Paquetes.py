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
    class Paquetes:
        def __init__(self, ID, nombre_paq, descripcion, precio):
            self.ID= ID
            self.nombre_paq= nombre_paq
            self.descripcion= descripcion
            self.precio= precio
            self.cant_ventas= int(input("Ingrese la cantidad de paquetes vendidos: "))
            print(self.ID, "|", self.nombre_paq, "|", self.descripcion, "|", "$ {:,}".format(self.precio), "|", self.cant_ventas)
            
                    
    def total_viajes():
        viajes= paquete1.cant_ventas + paquete2.cant_ventas + paquete3.cant_ventas + paquete4. cant_ventas + paquete5.cant_ventas + paquete6.cant_ventas
        print("Cantidad total de viajes: ", viajes)
        
    def total_ventas():
        venta1= paquete1.cant_ventas * paquete1.precio
        venta2= paquete2.cant_ventas * paquete2.precio
        venta3= paquete3.cant_ventas * paquete3.precio
        venta4= paquete4.cant_ventas * paquete4.precio
        venta5= paquete5.cant_ventas * paquete5.precio
        venta6= paquete6.cant_ventas * paquete6.precio
        ventas= venta1 + venta2 + venta3 + venta4 + venta5 + venta6
        print("\n---Total de ventas---")
        print("Paquete 1: ", "$ {:,}".format(venta1))
        print("Paquete 2: ", "$ {:,}".format(venta2))
        print("Paquete 3: ", "$ {:,}".format(venta3))
        print("Paquete 4: ", "$ {:,}".format(venta4))
        print("Paquete 5: ", "$ {:,}".format(venta5))
        print("Paquete 6: ", "$ {:,}".format(venta6))
        print("Total ventas: ", "$ {:,}".format(ventas))
        
    paquete1= Paquetes(1,'Ushuaia + Calafate', 'Incluye: Aéreos, alojamiento, traslados y excursiones', 1000000)
    paquete2= Paquetes(2, 'Salta', 'Incluye: Aéreos, alojamiento, traslados y excursiones', 800000)
    paquete3= Paquetes(3, 'Mendoza', 'Incluye: Aéreos, alojamiento, traslados y excursiones', 600000)
    paquete4= Paquetes(4, 'Rio de Janeiro', 'Incluye: Aéreos y alojamiento', 500000)
    paquete5= Paquetes(5, 'Punta del Este', 'Incluye: Aéreos y alojamiento', 1000000)
    paquete6= Paquetes(6, 'Lima + Cuzco', 'Incluye: Aéreos, alojamiento, traslados y excursiones', 2000000)
    total_viajes() 
    total_ventas()
    
except sqlite3.Error as e:
    print(f"Ocurrió un error con SQLite: {e}")
    
#5. Cerrar la conexión
finally:
    if conexion:
        conexion.close()
        print("\nConexión a la base de datos cerrada.")
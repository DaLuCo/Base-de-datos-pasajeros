from .ConexionDB import ConexionDB

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
    
class Pasajero()
    def __init__(self, DNI, nombre, fecha_nac, telefono, mail, paquete):
        self.DNI= DNI
        self.nombre= nombre
        self.fecha_nac= fecha_nac
        self.telefono= telefono
        self.mail= mail
        self.paquete= paquete
    
def guardar(pasajero):
    conexion= conexionDB()
    try:
        cursor.execute("INSERT INTO pasajeros (DNI, Nombre, Fecha_nac, Telefono, Mail, Paquete) VALUES (?, ?, ?, ?, ?, ?)",
        (DNI, nombre, fecha_nac, telefono, mail, paquete))
        conexion.commit()
        print(f"Pasajero '{nombre}' agregado con éxito.")        
    except sqlite3.Error as e:
        print(f"Error al agregar pasajero: {e}")
    finally:
        conexion.close()
    
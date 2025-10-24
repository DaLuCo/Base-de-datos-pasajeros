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
        pass

    def __del__(self):
        pass

    def agregar(self):
        self.nombre= input("Ingrese nombre y apellido del pasajero: ")
        self.DNI= int(input("Ingrese DNI del pasajero: "))
        self.fecha_nac= input("Ingrese fecha de nacimiento del pasajero: ")
        self.telefono= int(input ("Ingrese número de telefono del pasajero: "))
        self.mail= input("Ingrese mail del pasajero: ")        
        self.paquete= input("Seleccione el paquete que le guste: ")        
        print(self.nombre)
        print("{:,}".format(self.DNI))
        print(self.fecha_nac)
        print(self.telefono)
        print(self.mail)
        print(self.paquete)
        print("Pasajero agregado.")
        print("1. Sí")
        print("0. No")
        opcion= int(input("¿Desea agregar otro pasajero? "))
        if opcion==1:
            self.agregar()
        elif opcion==0:
            self.menu()
        else:
            print("Opción incorrecta.")

    def eliminar(self):
        self.__del__()
        print("Producto eliminado.")
        print("1. Sí")
        print("0. No")
        opcion= int(input("¿Desea eliminar otro pasajero? "))
        if opcion==1:
            self.eliminar()
        elif opcion==0:
            self.menu()
        else:
            print("Opción incorrecta.")

    def modificar(self):
        self.nombre= input("Ingrese nombre y apellido del pasajero: ")
        self.DNI= int(input("Ingrese DNI del pasajero: "))
        self.fecha_nac= input("Ingrese fecha de nacimiento del pasajero: ")
        self.telefono= int(input ("Ingrese número de telefono del pasajero: "))
        self.mail= input("Ingrese mail del pasajero: ")        
        self.paquete= input("Seleccione el paquete que le guste: ")
        print(self.nombre)
        print("{:,}".format(self.DNI))
        print(self.fecha_nac)
        print(self.telefono)
        print(self.mail)
        print(self.paquete)

    def salir(self):
        print("¡Gracias!")

    def menu(self):
        print("1. Agregar pasajero")
        print("2. Eliminar pasajero")
        print("3. Modificar datos del pasajero")
        print("4. Salir")
        seleccion= int(input("Ingrese una opción: "))
        while True:
            if seleccion==1:
                self.agregar()
                break
            elif seleccion==2:
                self.eliminar()
                break
            elif seleccion==3:
                self.modificar()
                break
            elif seleccion==4:
                self.salir()
                break
            else:
                print("Opción inválida.")
                break
        self.menu()    

pasajero= Pasajeros()
pasajero.menu()
pasajero.agregar()
pasajero.eliminar()
pasajero.modificar()
pasajero.salir()

conexion= sqlite3.connect("Base de datos pax.db")
with conexion:
    cursor= conexion.cursor()
Lista_pasajeros= []
id_pasajeros= 0
for pasajeros in Lista_pasajeros:
    cursor.execute("Agregar en Pasajeros", (id_pasajeros, Pasajeros.nombre, Pasajeros.DNI, Pasajeros. fecha_nac, Pasajeros.telefono,
    Pasajeros.mail, Pasajeros.paquete))
id_pasajeros+=1
import tkinter as tk
from tkinter import ttk

class Pasajero():
    def __init__(self, DNI, nombre, fecha_nac, telefono, mail, paquete):
        self.DNI= DNI
        self.nombre= nombre
        self.fecha_nac= fecha_nac
        self.telefono= telefono
        self.mail= mail
        self.paquete= paquete

def alta(pasajero):
    try:
        DNI= int(input("Ingrese el DNI del pasajero: "))
    except ValueError:
        print("Debe ingresar un número de hasta 8 cifras.")
        return
    nombre= input("Ingrese nombre y apellido del pasajero: ")
    fecha_nac= input("Ingrese fecha de nacimiento del pasajero: ")
    try:
        telefono= int(input("Ingrese el teléfono del pasajero: "))
    except ValueError:
        print("Debe ingresar un número de 10 cifras.")
        return
    mail= input("Ingrese el mail del pasajero: ")
    try:
        paquete= int(input("Ingrese el ID del paquete elegido por el pasajero: "))
    except ValueError:
        print("Debe ingresar un número del 1 al 6.")
        return
    conexion= conectar()
    cursor= conexion.cursor()

    try:
        cursor.execute("INSERT INTO pasajeros (DNI, Nombre, Fecha_nac, Telefono, Mail, Paquete) VALUES (?, ?, ?, ?, ?, ?)",
        (DNI, nombre, fecha_nac, telefono, mail, paquete))
        conexion.commit()
        print(f"Pasajero '{nombre}' agregado con éxito.")        
    except sqlite3.Error as e:
        print(f"Error al agregar empleado: {e}")
    finally:
        conexion.close()

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Base de datos pasajeros")
        self.geometry("500x500")
        self.datos()
        self.habilitar()
        self.deshabilitar()
        self.guardar()
        self.tabla()

    def datos(self):
        #Etiquetas        
        self.etiqueta1= tk.Label(self, text= "DNI: ")
        self.etiqueta1.grid(row= 0, column= 0, padx= 10, pady= 5)
        self.etiqueta2= tk.Label(self, text= "Nombre: ")
        self.etiqueta2.grid(row= 1, column= 0, padx= 5, pady= 5)
        self.etiqueta3= tk.Label(self, text= "Fecha de nacimiento: ")
        self.etiqueta3.grid(row= 2, column= 0, padx= 10, pady= 5)
        self.etiqueta4= tk.Label(self, text= "Teléfono: ")
        self.etiqueta4.grid(row= 3, column= 0, padx= 5, pady= 5)
        self.etiqueta5= tk.Label(self, text= "Mail: ")
        self.etiqueta5.grid(row= 4, column= 0, padx= 5, pady= 5)
        self.etiqueta6= tk.Label(self, text= "Paquete: ")
        self.etiqueta6.grid(row= 5, column= 0, padx= 5, pady= 5)       
                
        #Entrys
        self.dni= tk.StringVar()
        self.texto1= tk.Entry(self, textvariable= self.dni)
        self.texto1.grid(row= 0, column= 1, padx= 5, pady= 5)
        self.nombre= tk.StringVar()
        self.texto2= tk.Entry(self, textvariable= self.nombre)
        self.texto2.grid(row= 1, column= 1, padx= 5, pady= 5)
        self.fecha= tk.StringVar()
        self.texto3= tk.Entry(self, textvariable= self.fecha)
        self.texto3.grid(row= 2, column= 1, padx= 5, pady= 5)
        self.telefono= tk.StringVar()
        self.texto4= tk.Entry(self, textvariable= self.telefono)
        self.texto4.grid(row= 3, column= 1, padx= 5, pady= 5)
        self.mail= tk.StringVar()    
        self.texto5= tk.Entry(self, textvariable= self.mail)
        self.texto5.grid(row= 4, column= 1, padx= 5, pady= 5)
        self.paquete= tk.StringVar()
        self.texto6= tk.Entry(self, textvariable= self.paquete)
        self.texto6.grid(row= 5, column= 1, padx= 5, pady= 5)
        
        #Botones
        self.boton1= tk.Button(self, text= "Agregar pasajero", command= self.habilitar)
        self.boton1.grid(row= 6, column= 0)
        self.boton2= tk.Button(self, text= "Modificar pasajero")
        self.boton2.grid(row= 6, column= 1)
        self.boton3= tk.Button(self, text= "Eliminar pasajero")
        self.boton3.grid(row= 6, column= 2)
        self.boton4= tk.Button(self, text= "Guardar", command= self.guardar)
        self.boton4.grid(row= 8, column= 0)
        self.boton5= tk.Button(self, text= "Cancelar", command= self.deshabilitar)
        self.boton5.grid(row= 8, column= 1)
        self.boton6= tk.Button(self, text= "Salir")
        self.boton6.grid(row= 8, column= 2)
        
    def habilitar(self):
        self.texto1.config(state= 'normal')
        self.texto2.config(state= 'normal')
        self.texto3.config(state= 'normal')
        self.texto4.config(state= 'normal')
        self.texto5.config(state= 'normal')
        self.texto6.config(state= 'normal')
        
        self.boton4.config(state= 'disabled')
        self.boton5.config(state= 'disabled')
        
    def deshabilitar(self):
        self.dni.set('')
        self.nombre.set('')
        self.fecha.set('')
        self.telefono.set('')
        self.mail.set('')
        self.paquete.set('')
        
        self.texto1.config(state= 'disabled')
        self.texto2.config(state= 'disabled')
        self.texto3.config(state= 'disabled')
        self.texto4.config(state= 'disabled')
        self.texto5.config(state= 'disabled')
        self.texto6.config(state= 'disabled')
        
        self.boton4.config(state= 'disabled')
        self.boton5.config(state= 'disabled')
        
    def guardar(self):
        pasajero= Pasajero(
            self.dni.get(),
            self.nombre.get(),
            self.fecha.get(),
            self.telefono.get(),
            self.mail.get(),
            self.paquete.get(),)
        alta(pasajero)
        self.deshabilitar()

    def tabla(self):
        self.tabla= ttk.Treeview(self, column= ('DNI', 'Nombre', 'Fecha de nacimiento', 'Telefono', 'Mail', 'Paquete'))
        self.tabla.grid(row= 7, column= 0, columnspan= 5, padx= 10, pady= 10)
        self.tabla.heading('#0', text= 'DNI')
        self.tabla.heading('#1', text= 'Nombre')
        self.tabla.heading('#2', text= 'Fecha de nacimiento')
        self.tabla.heading('#3', text= 'Telefono')
        self.tabla.heading('#4', text= 'Mail')
        self.tabla.heading('#5', text= 'Paquete')
        
        self.tabla.insert('', 0, text= 33741053,
        values= ('Daniela Comes', '20/06/1988', 1156290262, 'daniela.comes@outlook.com', 1))
    
if __name__ == "__main__":
    app= Aplicacion()
    app.mainloop()
import tkinter as tk
from Pasajeros.TKinter import Aplicacion

def main():
    root= tk.Tk()
    root.title("Base de datos pasajeros")
    app= Aplicacion(root= root)
    app.mainloop()

if __name__ == '__main__':
    main()
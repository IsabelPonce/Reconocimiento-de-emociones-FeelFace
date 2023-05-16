import tkinter as tk
import subprocess
from tkinter import filedialog
from PIL import Image, ImageTk
import os
fondo_entrar = "#1c2120"
fondo_correcto  = "#8b4fc6"
fondo_incorrecto = "#8b4fc6"
fondo_entrada = "#ececec"
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("500x500+500+50")
ventana.resizable(width=False, height=False)
fondo = tk.PhotoImage(file="entrar.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)
#entradas
usuario = tk.StringVar()
password = tk.StringVar()
entrada= tk.Entry(ventana, textvariable= usuario, width= 40, relief= "flat", bg= fondo_entrada)
entrada.place(x =100, y= 260)
entrada2 = tk.Entry(ventana, textvariable=password,show="*" ,width=40, relief="flat", bg=fondo_entrada)
entrada2.place(x=100, y=360)

def login():
    nombre = usuario.get()
    contraseña = password.get()
    if nombre == "Isabel" and contraseña == "22101999" :
        correcto()
    elif nombre == "Andres" and contraseña == "30041998" :
        correcto()
    elif nombre == "Anahi" and contraseña == "18081998":
        correcto()
    elif nombre == "Hugo" and contraseña == "20041965":
        correcto()
    else:
        incorrecto()

def abrir_carpeta():
    ventana.withdraw()

    # Ruta de la carpeta
    folder_path = r'C:/Users/USUARIO/Desktop/Reconocimiento de  Emociones/Emociones Negativas'
    # Abrir el gestor de archivos en la carpeta seleccionada
    if os.path.exists(folder_path):
        os.startfile(folder_path)
    else:
        print("La carpeta no existe: ", folder_path)
def correcto():
    ventana.withdraw()
    window = tk.Toplevel()
    window.title("Bienvenido")
    window.geometry("500x500+500+50")
    window.resizable(width=False, height=False)
    fondo = tk.PhotoImage(file="correcto1.png")
    fondo1 = tk.Label(window, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)
    # botón para ejecutar otro programa
    def ejecutar_programa():
        subprocess.Popen(["python", "reconocimientoEmociones.py"])
        
    boton2 = tk.Button(window, text="Ejecutar programa", cursor="hand2", relief="flat", bg=fondo_correcto, font=("Comic Sans Ms", 12, "bold"), command=ejecutar_programa)
    boton2.place(x=180, y=450)
    def salir():
        window.destroy()
    boton3 = tk.Button(window, text="Salir", cursor="hand2", relief="flat", bg=fondo_correcto, font=("Comic Sans Ms", 12, "bold"), command=salir)
    boton3.place(x=350, y=450)
     #boton para abirir las imagenes
     
    boton4 = tk.Button(window, text="Abrir carpeta", cursor="hand2", relief="flat", bg=fondo_correcto, font=("Comic Sans Ms", 12, "bold"), command=abrir_carpeta)
    boton4.place(x=20, y=450)
    window.mainloop()




def incorrecto():
    ventana.withdraw()
    root = tk.Toplevel()
    root.title("Error")
    root.geometry("500x500+500+50")
    root.resizable(width=False, height=False)
    fondo = tk.PhotoImage(file="error1.png")
    fondo1 = tk.Label(root, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

    def regreso():
        root.withdraw()
        ventana.deiconify()

    boton5 = tk.Button(root, text="regresar", command=regreso, cursor="hand2", relief="flat", bg=fondo_correcto, font=("Comic Sans Ms", 12, "bold"))
    boton5.place(x=400, y=420)
    root.mainloop()




#botones 
boton = tk.Button(ventana, text="Sing Up", command=login , cursor="hand2", bg=fondo_entrar, fg='white', width=19, relief="flat", font=("comic Sans MS", 12, "bold"))
boton.place(x=150, y=450)



ventana.mainloop()
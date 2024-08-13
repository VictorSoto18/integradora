import tkinter
import tkinter.messagebox
# ventanaaaaaaaaa
ventana = tkinter.Tk()
ventana.title("/")
ventana.geometry("500x500")
ventana.resizable(0,0)
# etiquetaaa
cabezera = tkinter.Label(ventana, text = "         Editar     ").pack()
# boton
def saludo():
    tkinter.Label(ventana, text ="FINALIZADO").pack()

def salir():
    ventana.destroy()

boton = tkinter.Button(ventana, text="Aceptar", command=saludo,fg="red")
boton.pack()
boton.place(x=50, y=300, height=75, width=150 )

boton2 = tkinter.Button(ventana, text="Cerrar", command=salir,fg="red")
boton2.pack()
boton2.place(x=300, y=300, height=75, width=150 )


tkinter.messagebox.showinfo("EDITADO","FINALIZADO")

img = tkinter.PhotoImage(file="./static/Styles/sags_fondo.jpg")
lbl_img = tkinter.Label(ventana, imagen = img)
lbl_img.pack()

ventana.mainloop()
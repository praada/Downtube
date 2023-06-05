import os
from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox

#crear la clase descargar
def descargar():
    link = videos.get() #aqui va a obtener el link
    video = YouTube(link) #aqui sera el video a descargar
    descarga = video.streams.get_highest_resolution() #define que siempre seran en high quality
    

    #ruta para guardar en la carpeta Descargas
    ruta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")

    #nombre del video
    vidtitulo = video.title
    vidname = f"{vidtitulo}.mp4"

    #problemas con signos en el nombre del vid
    # Reemplazar caracteres no válidos en el nombre del archivo
    vidname = vidname.replace("/", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace("\"", "_").replace("<", "_").replace(">", "_").replace("|", "_")
   
    #finalizacion de descarga
    ruta_guardado = os.path.join(ruta_descargas, vidname)
    descarga.download(filename=ruta_guardado)
    MessageBox.showinfo("Descarga completada", "¡Video descargado en su Maxima Calidad!")
    boton.config(state=NORMAL)



#crear la clase que hace accion al precionar lo del submenu del menu
def popup():
    MessageBox.showinfo("Mi Twitter", "Sigueme en TWITTER https://twitter.com/kelvinemontilla !")

    

#PARTE GRAFICA
#creacion de ventana
root = Tk() #Tk clase para crear ventana
root.config(bd=16)  #el ancho de la ventana en pixeles
root.title("DownTube") #titulo de la ventana

imagen_link = PhotoImage(file="practicas/downtube/logo.png") #clase que sirve para cargar y mostrar img
factor_scale = 2 #para achicar la img
conv_img = imagen_link.subsample(factor_scale)

foto = Label(root,image=conv_img, bd=0)
foto.grid(row=0,column=0)

#creacion de un minimenu
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar,tearoff=0) #este es el submenu dentro de menubar

menubar.add_cascade(label="Contactos", menu=helpmenu) #acciones y lo que contenga ese menubar
helpmenu.add_command(label="Twitter", command=popup) #del submenu lleva command por que al tocarlo tendra una accion por ejecutar que se guarda en la variable popup

titulo = Label(root,text="Obtén el videos en calidad máxima\n")
titulo.grid(row=0,column=1)


#Donde el usuario coloca el link
videos = Entry(root)
videos.grid(row=1,column=1)

#boton de descargar
boton = Button(root, text="Descargar", command=descargar)
boton.grid(row=2,column=1)

root.mainloop() #esto es para cerrar la parte grafica

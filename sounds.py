from tkinter import Button,Listbox,filedialog,ttk
import tkinter as tk
import pygame
import os

show = tk.Tk()
pygame.init()

show.title("Music player")
show.geometry("800x490")
show.configure(background="lightGray")

#loading audio file
def loadfile():
    global loadf
    loadf = tk.filedialog.askopenfilename(title ='amapiyano.ogg')

    if loadf:
        file_path,file_name = os.path.split(loadf)
        lit_box.insert(tk.END, file_name)
        print(f'ogg filename: {file_name}')
        print(f'file location: {file_path}')

def playfile():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(loadf)
        pygame.mixer.music.play(-1)
    except pygame.error:
        print("could not load file")
    except NameError:
        print("file cannot be found, plese load a track first")
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

#listbox
lit_box =Listbox(show,bg='skyblue',font= "helvetice 12")
lit_box.pack()

#Buttons
btn_load = Button(show,text="Load SONG", command=loadfile)
btn_load.place(x=50,y=250)

btn_play = Button(show,text="PLAY", command=playfile)
btn_play.place(x=180,y=250)

btn_pause= Button(show,text="PAUSE", command=pause)
btn_pause.place(x=290,y=250)

btn_unpause= Button(show,text="RESUME", command=unpause)
btn_unpause.place(x=400,y=250)

btn_stop = Button(show,text="STOP", command=stop)
btn_stop.place(x=500,y=250)

show.mainloop()

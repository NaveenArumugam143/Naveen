import pygame
import tkinter as tk
from tkinter import filedialog
main=tk.Tk()
main.title("Music Player")
main.geometry("300x400")

#file="E:\song\Collecations/alunguren.mp3"
def play(a):
    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(a)
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
def select_choice():
    filename =  filedialog.askopenfile(initialdir = "/",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    play(filename)

im=tk.PhotoImage(file="mob.png")
label=tk.Label(main,image=im)
label.place(x=0, y=0, relwidth=1, relheight=1)

open_button=tk.Button(main,text="Select Mp3 to Play", command=select_choice,pady=10)
open_button.pack(fill="both")

button_1=tk.Button(main,text="Play",command=play,pady=10)
button_1.pack(fill="both")

button_2=tk.Button(main,text="Stop",command=stop,pady=10)
button_2.pack(fill="both")

main.mainloop()

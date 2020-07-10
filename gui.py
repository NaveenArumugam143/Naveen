import tkinter as tk 
import wikipedia
from tkinter import scrolledtext 
window=tk.Tk()
window.title("My Apps")
window.geometry('1080x720')
label_1=tk.Label(window,text="Enter Text You Want To Search",font=("ArialBold",10),pady=10)
label_1.grid(column=0,row=0)
txt=tk.Entry(window,width=10)
txt.grid(column=1,row=0)
label_2=tk.Label(window,text="Click To Search",pady=10)
label_2.grid(column=0,row=1)
def search():
    
    if txt.get()!="":
        label_2.configure(text="Searching Content")
        wikisearch()
        
    else:
        return

button_1=tk.Button(text="Search",bg="red",fg="white",command=search)
button_1.grid(column=1,row=1)
#check box
'''
chkstate=tk.BooleanVar() # tkinter variable
chkstate.set(False)
combo_1=tk.Checkbutton(window,text="Yes",var=chkstate)
combo_1.grid(column=1,row=2)
'''

#radiobutton
'''
radio_1=tk.Radiobutton(window,text="Student",value=1)
radio_2=tk.Radiobutton(window,text="Faculty",value=2)
radio_3=tk.Radiobutton(window,text="Principal",value=3)
radio_1.grid(column=1,row=2)
radio_2.grid(column=2,row=2)
radio_3.grid(column=3,row=2)
'''


    
scroledtext=scrolledtext.ScrolledText(window,width=100,height=50)
def wikisearch():
    w=wikipedia.summary(txt.get())
    scroledtext.insert('2.0',w)
scroledtext.grid(column=0,row=10)


window.mainloop()


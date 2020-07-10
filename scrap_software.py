import tkinter as tk
from selenium import webdriver as wd
from tkinter import scrolledtext as st
from tkinter import messagebox
obj=tk.Tk()
obj.title("Web Scraping")
obj.geometry('1300x700')

label=tk.Label(obj,text="Enter the URL")
label.grid(column=0,row=2)
text=tk.Entry(obj,width=50)
text.grid(column=1,row=2)
variable=tk.StringVar(obj)

match={"class":"class_name","id":"id","xpath":"xpath","tag_name":"Tag_name","css_selector":"CSS_Selector","full_link":"Link","partial_link":"Partial Link"}
s=match
option=["xpath","class","id","tag_name","css_selector","full_link","partial_link"]
variable.set(option[0])
def dropdown(self):
       for i in match:
            if variable.get()==i:
                label_2.configure(text=i)
                #scrolledtext.insert("1.0",s[str(variable.get())])
               
       
         
w=tk.OptionMenu(obj,variable,*option,command=dropdown)
w.grid(column=1,row=4)

label_2=tk.Label(obj,text="Enter the Xpath")
label_2.grid(column=0,row=6)
text1=tk.Entry(obj,width=50)
text1.grid(column=1,row=6)
def find(self,value):
   # driver.find_elements_by_id
   pass
def click():

   if text.get()!="" and text1.get()!="":
       driver=wd.Chrome("chromedriver.exe")
       url=text.get()
       choice=text1.get()
       driver.get(url)
       if variable.get()=="class":
           for i in driver.find_elements_by_class_name(str(choice)):
               scrolledtext.insert("1.0",i.text)
       if variable.get()=="id":
           for i in driver.find_elements_by_id(str(choice)):
               scrolledtext.insert("1.0",i.text)
       if variable.get()=="xpath":
           for i in driver.find_elements_by_xpath(str(choice)):
               scrolledtext.insert("1.0",i.text)
       if variable.get()=="tag_name":
           for i in driver.find_elements_by_tag_name(str(choice)):
               scrolledtext.insert("1.0",i.text) 
       if variable.get()=="css_selector":
           for i in driver.find_elements_by_css_selector(str(choice)):
               scrolledtext.insert("1.0",i.text) 
       if variable.get()=="full_link":
            for i in driver.find_elements_by_link_text(str(choice)):
               scrolledtext.insert("1.0",i.text) 
       if variable.get()=="partial_link":
            for i in driver.find_elements_by_partial_link_text(str(choice)):
               scrolledtext.insert("1.0",i.text) 
   else:
       messagebox.showinfo(message="Please Kindly Check Input")
       return False

button=tk.Button(obj,text="Click",command=click)
button.grid(column=1,row=5,pady=10)
scrolledtext=st.ScrolledText(obj,width=150,height=50)
scrolledtext.grid(column=1,row=12)
tk.Pack()
obj.mainloop()

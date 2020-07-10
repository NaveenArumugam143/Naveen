import pandas as pd
from matplotlib import pyplot as mp
from selenium import webdriver as wd
import os

url="https://www.mygov.in/corona-data/covid19-statewise-status"

driver=wd.Chrome("chromedriver.exe")
driver.get(url)

ls=[]
'''
for i in driver.find_elements_by_class_name("field-items"):
    m=i.text
    file.write(m)
    ls.append(m)
'''
driver.find_elements_by_class_name("field-items")
label=[]
file=open("Naveen.txt","w+")

for i in driver.find_elements_by_class_name("div.field-label"):
    print(i.text)
    label.append(i.text)
    file.write(i.text)


'''
for i in driver.find_elements_by_class_name("field-items"):
    if i!="":
        
        m=str(i.text)
        print(str(m))
        file.write(m+"\t")
        ls.append(m)
        
file.close()
print(len(ls))
'''
f=open("Naveen.txt","r")
for i in f.read():
    print(i)
f.close()
'''
'''



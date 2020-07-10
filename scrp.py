import lxml
import re
import numpy
import urllib3
import  pandas as pd
import matplotlib
#from urllib import urlopen
import urllib.request as urllib2
import bs4 as bs
url="https://www.mohfw.gov.in/"
html=urllib2.urlopen(url).read()
soup=bs.BeautifulSoup(html,'lxml')
file=open("naveen.txt","w+")
table=soup.find('div',class_="data-table table-responsive")
labels=[]
data=[]
rows = table.find_all('tr')

for row in rows:
    if(row.text!=""):
        regex=re.compile("\n") 
        m=row.text
        final=regex.sub("\t",m)
        s=re.compile("\t")
        write=s.sub("\n",final)
        print(final)
        if write!="":
            data.append(write)
            
    
for i in data:
    x=0
    n=re.compile("\n")
    res=n.sub("\t",i)
    #print(res)
    if x%6==0:
        #print("\n")
        file.write("\n")
    x+=1
    file.write(res)
file.close()
file_open=open("Naveen.txt","r")
print(file_open)

import requests
import os
import re
import numpy
import pandas as pd
from bs4  import BeautifulSoup
a=requests.get("https://www.mohfw.gov.in/")
con=a.content
soup=BeautifulSoup(con,"html.parser")
text=[soup.find_all('li',class_="bg-green"),soup.find_all('li',class_="bg-green"),soup.find_all('li',class_="bg-red"),soup.find_all('li',class_="bg-orange")]
#print(soup.find_all('li',class_="bg-green"))
#print(soup.find_all('li',class_="bg-green"))
#print(soup.find_all('li',class_="bg-red"))
#print(soup.find_all('li',class_="bg-orange"))
print(text)

table=soup.find('div',class_="data-table table-responsive")
print(table)


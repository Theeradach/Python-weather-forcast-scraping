#!/usr/bin/python3
# coding: utf-8

import os
import sys, urllib
import csv
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.jma.go.jp/jp/yoho/332.html"   
data = requests.get(url)                       
soup = BeautifulSoup(data.text,'html.parser')   

table=soup.find("table",{"class":"forecast"})
list_of_rows=[]      
for row in table.findAll(["table",{"class":"rain"},"table",{"class":"temp"}]):    
    list_of_cells=[]
    rain_word = ""
    for cell in row.findAll('td'):              
        rain_word += re.sub(r'\s','',cell.text) + " "
    # list_of_rows.append(list_of_cells)       
    print(rain_word)  




# outfile = open('./forcasting.csv','w', encoding='CP932', errors='replace' ,newline='')
# writer=csv.writer(outfile)
# writer.writerows(list_of_rows)                  # write each data 
# print(os.getcwd())   
# print(list_of_rows)        
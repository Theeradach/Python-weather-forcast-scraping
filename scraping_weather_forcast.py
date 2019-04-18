#!/usr/bin/python3
# coding: utf-8

import os
import sys, urllib
import csv
import requests
import re
from bs4 import BeautifulSoup

# ====================   FUNCTIONS  ======================== #

# chuck data 
def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

# transpose a matrix : convert row to column 
def transpose_data(chuck_data):
    rows = []
    rez = [[chuck_data[j][i] for j in range(len(chuck_data))] for i in range(len(chuck_data[0]))] 
    print("\n") 
    for row in rez: 
        rows.append(row)
    return rows
    
# ====================   FUNCTIONS  ======================== #


# ====================   MAIN PROGRAM ======================== #

url = "https://www.jma.go.jp/jp/yoho/332.html"                  # website url
data = requests.get(url)                                        # get data from website
soup = BeautifulSoup(data.text,'html.parser')                   # parse data


table = soup.find("table",{"id":"forecasttablefont"})           # get table from id 
list_of_weather=[]                                      
list_of_info=[]
list_of_rain=[]
list_of_temp=[]

for row in table.findAll("th",{"class":"weather"}):   
    list_of_weather.append(re.sub(r'\s',' ',row.text))
for row in table.findAll("td",{"class":"info"}):     
    list_of_info.append(re.sub(r'\s',' ',row.text))
for row in table.findAll("td",{"class":"rain"}): 
    list_of_rain.append(re.sub(r'\s',' ',row.text))
for row in table.findAll("td",{"class":"temp"}):        
    list_of_temp.append(re.sub(r'\s',' ',row.text))

# merge all list 
mergedArray = list_of_weather + list_of_info + list_of_rain + list_of_temp
n = 6    # chuck size 
chuck_data = list(divide_chunks(mergedArray, n)) 

list_data_rows = list(transpose_data(chuck_data)) 
print(f' DATA FROM FUNCTION : \n {list_data_rows}')

outfile = open('./scarping_weather_forcast.csv','w', encoding='CP932', errors='replace' ,newline='')
writer=csv.writer(outfile)
writer.writerows(list_data_rows)
print(os.getcwd())           

# ====================   MAIN PROGRAM ======================== #
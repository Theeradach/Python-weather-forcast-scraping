#!/usr/bin/python3
# coding: utf-8

import os
import sys, urllib
import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.jma.go.jp/jp/amedas_h/today-63331.html?areaCode=000&groupCode=46"       # website url
data = requests.get(url)                        # get data from website
soup = BeautifulSoup(data.text,'html.parser')   # parse data

table=soup.find("table",{"id":"tbl_list"})      # get table from id 
list_of_rows=[]                                 # declare array to store each row data
for row in table.findAll('tr'):                 # loop every tr data in table tag
    list_of_cells=[]
    for cell in row.findAll('td'):              # loop every td data in tr tag
        if cell.text == '\xa0':                 # if data in cell is empty,  
            list_of_cells.append('')            # append empty ''
        else:
            list_of_cells.append(cell.text)     # append data
    list_of_rows.append(list_of_cells)          # append data in each row
outfile = open('./forcasting.csv','w', encoding='CP932', errors='replace' ,newline='')
writer=csv.writer(outfile)
writer.writerows(list_of_rows)                  # write each data 
print(os.getcwd())                              # where file is stored

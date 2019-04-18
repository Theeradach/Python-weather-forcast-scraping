#!/usr/bin/python3
# coding: utf-8

import os
import sys, urllib
import csv
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.jma.go.jp/jp/week/331.html"  # website url
data = requests.get(url)                        # get data from website
soup = BeautifulSoup(data.text,'html.parser')   # parse data

table=soup.find("table",{"id":"infotablefont"}) # get table from id 
list_of_rows=[]                                 # declare array to store each row data
for row in table.findAll('tr'):                 # loop every tr data in table tag
    list_of_cells=[]
    for cell in row.findAll(['td','th'] , limit=8):  # loop every td data in tr tag
        if cell.has_attr('rowspan'):            # if found rowspan, then skip 
            continue
        else:
            data = re.sub(r'\s','',cell.text)   # terminate \n\t 
            list_of_cells.append(data)          # append data
    list_of_rows.append(list_of_cells)          # append data in each row
outfile = open('./forcasting_2.csv','w', encoding='CP932', errors='replace' ,newline='')
writer=csv.writer(outfile)
writer.writerows(list_of_rows)                  # write each data 
print(os.getcwd())                              # where file is stored

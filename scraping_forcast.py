#!/usr/bin/python3
# coding: utf-8

import os
import sys, urllib
import csv
import requests
import re
import datetime
from bs4 import BeautifulSoup

# ====================   FUNCTIONS  ======================== #
# TODO: function for scraping data from website
#       fuken_code : int 
def scraping_data(fuken_code):
    url = "https://www.jma.go.jp/jp/week/" + fuken_code + ".html"   # website url
    data = requests.get(url)                                        # get data from website
    soup = BeautifulSoup(data.text,'html.parser')                   # parse data

    table = soup.find("table",{"id":"infotablefont"})               # get table from id 
    list_of_rows=[]                                                 # declare array to store each row data
    for row in table.findAll('tr'):                                 # loop every tr data in table tag
        list_of_cells=[]
        for cell in row.findAll(['td','th'] , limit=8):             # loop every td data in tr tag
            if cell.has_attr('rowspan'):                            # if found rowspan, then skip 
                continue
            else:
                data = re.sub(r'\s','',cell.text)                   # terminate \n\t 
                list_of_cells.append(data)                          # append data
        list_of_rows.append(list_of_cells)                          # append data in each row
    return list_of_rows

# TODO: function for writing files 
#       filename : string 
#       list_of_rows : list 
def writefile(filename , list_of_rows):
    file_export = open(filename ,'w', encoding='CP932', errors='replace' ,newline='')
    writer=csv.writer(file_export)                                  # create file but not writing
    writer.writerows(list_of_rows)                                  # write each data in file 

# ====================   FUNCTIONS  ======================== #


# ====================   MAIN PROGRAM ======================== #

print(os.getcwd())                                                  # file location
date = datetime.datetime.now()                                      # get execute date ex.2014-09-26 16:34:40.278298
current_date = date.strftime("%Y%m%d%H%M%S")                        # format date time
with open('fukenlist.csv') as csv_file:                             # open csv file ex. fukelist.csv
    csv_reader = csv.reader(csv_file, delimiter=',')                # read csv file
    line_count = 0                                                  # count line
    for row in csv_reader:                                          # loop each line 
        if line_count == 0:                             
            #print(f'{" , ".join(row)}')                            # in case of header
            line_count += 1
        else:
            list_of_rows = list()
            # print(f'{row[0]} , {row[1]}')                         # see data from csv file
            filename = './exports/'+ row[1] + '_' 
            filename += current_date + '.csv'                       # file path & name
            list_of_rows = scraping_data(row[0])                    # get data from each fuken code
            writefile(filename , list_of_rows)                      # create each file and write data 
            line_count += 1 
    print(f'Processed {line_count} files.')

# ====================   MAIN PROGRAM ======================== #

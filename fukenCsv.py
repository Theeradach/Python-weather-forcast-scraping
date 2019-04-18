#!/usr/bin/python3
# coding: utf-8

import os
import sys, urllib
import csv
import requests
import re
import datetime
from bs4 import BeautifulSoup

print(os.getcwd())                                      # where file is stored
date = datetime.datetime.now()                          # get execute date ex.2014-09-26 16:34:40.278298
current_date = date.strftime("%Y%m%d%H%M%S")            # format date time
with open('fukenlist.csv') as csv_file:                 # open csv file ex. fukelist.csv
    csv_reader = csv.reader(csv_file, delimiter=',')    # read csv file
    line_count = 0                                      # count line
    for row in csv_reader:                              # loop each line 
        if line_count == 0:                             
            #print(f'{" , ".join(row)}')                # in case of header
            line_count += 1
        else:
            #print(f'{row[0]} , {row[1]}')              # see data from csv file
            filename = './exports/'+ row[1] + '_' +current_date + '.csv'    # file path & name
            print(f'{filename}')                        # write each file
            file_export = open(filename ,'w', encoding='CP932', errors='replace' ,newline='')
            writer=csv.writer(file_export)              # create file but not writing
            line_count += 1 
    print(f'Processed {line_count} files.')



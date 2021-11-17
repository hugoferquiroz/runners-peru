# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:32:36 2021

@author: Hugo Fernandez
"""

import os
import pandas as pd
from selenium import webdriver
import time

# Set working directory
working_directory = 'D:\\Proyectos personales\\runners-peru'
os.chdir(working_directory)

# Set scraping
web = 'https://pacifictiming.com/result-wizard/?prefix=190519_lima42k' #you can choose any other league
path = 'D://Temp//chromedriver_win32//chromedriver.exe' #introduce your file's path inside '...'
driver = webdriver.Chrome(path)
driver.get(web)

time.sleep(10) #add implicit wait, if necessary
accept = driver.find_element_by_xpath('//*[@id="search_panel"]/form/input[4]')
accept.click()

time.sleep(180) #add implicit wait, if necessary
rows = driver.find_elements_by_class_name('result_cell')
for row in rows:
    print(row.text)
    
number_runner = []  
for i in range(0,len(rows),11):
    print(rows[i].text)
    number_runner.append(rows[i].text)
    
last_name = [] 
for i in range(1,len(rows),11):
    print(rows[i].text)
    last_name.append(rows[i].text)

name = [] 
for i in range(2,len(rows),11):
    print(rows[i].text)
    name.append(rows[i].text)

gender = []
for i in range(3,len(rows),11):
    print(rows[i].text)
    gender.append(rows[i].text)

age = []
for i in range(4,len(rows),11):
    print(rows[i].text)
    age.append(rows[i].text)

category = []
for i in range(5,len(rows),11):
    print(rows[i].text)
    category.append(rows[i].text)
    
official_time = []
for i in range(6,len(rows),11):
    print(rows[i].text)
    official_time.append(rows[i].text)
    
chip_time = []
for i in range(7,len(rows),11):
    print(rows[i].text)
    chip_time.append(rows[i].text)
       
ranking = []
for i in range(8,len(rows),11):
    print(rows[i].text)
    ranking.append(rows[i].text)

dic = {'number_runner': number_runner,
       'last_name': last_name,
       'name': name,
       'gender': gender,
       'age': age,
       'category':category ,
       'official_time': official_time,
       'chip_time':chip_time ,
       'ranking':ranking ,
       } 

lima2019 = pd.DataFrame(dic)  
lima2019
lima2019.to_csv('Data/2019.csv')

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:32:36 2021

@author: @hugoferq
"""

import os
import pandas as pd
from selenium import webdriver
import time

# Set working directory
working_directory = 'D:\\Proyectos personales\\runners-peru\\data\\raw'
os.chdir(working_directory)

def webscraping_running_peru(output_name,url,path_chromedriver):
    '''
    
    Function for webs craping the results of running race in the page 
    https://pacifictiming.com/resultados/

    Parameters
    ----------
    
    output_name : str
        Name of the output running race.
    
    url : str
        String with the url of the running race.
        
    path_chromedriver : str
        Path where save the last version of chromedriver. 
        Example: 'D//Temp//chromedriver_win32//chromedriver.exe'
        
    Returns
    -------
    A CSV with the data of a running race and encoded with utf-8.
    A data frame with the results of running race. 
    Example: 
        adidas_run = webscraping_running_peru(output_name,url,path_chromedriver)

    '''

    # Set scraping
    web = url # URl with the race running results
    path = path_chromedriver #introduce your file's path
    driver = webdriver.Chrome(path)
    driver.get(web)
    
    time.sleep(10) #add implicit wait, if necessary
    accept = driver.find_element_by_xpath('//*[@id="search_panel"]/form/input[4]')
    accept.click()
    
    time.sleep(180) #add implicit wait, if necessary
    rows = driver.find_elements_by_class_name('result_cell')
    # for row in rows:
    #     print(row.text)
        
    number_runner = []  
    for i in range(0,len(rows),11):
        # print(rows[i].text)
        number_runner.append(rows[i].text)
        
    last_name = [] 
    for i in range(1,len(rows),11):
        # print(rows[i].text)
        last_name.append(rows[i].text)
    
    name = [] 
    for i in range(2,len(rows),11):
        # print(rows[i].text)
        name.append(rows[i].text)
    
    gender = []
    for i in range(3,len(rows),11):
        # print(rows[i].text)
        gender.append(rows[i].text)
    
    age = []
    for i in range(4,len(rows),11):
        # print(rows[i].text)
        age.append(rows[i].text)
    
    category = []
    for i in range(5,len(rows),11):
        # print(rows[i].text)
        category.append(rows[i].text)
        
    official_time = []
    for i in range(6,len(rows),11):
        # print(rows[i].text)
        official_time.append(rows[i].text)
        
    chip_time = []
    for i in range(7,len(rows),11):
        # print(rows[i].text)
        chip_time.append(rows[i].text)
           
    ranking = []
    for i in range(8,len(rows),11):
        # print(rows[i].text)
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
    
    df = pd.DataFrame(dic)
    df.to_csv(f'{output_name}.csv', sep = ',', index=False, encoding = 'utf-8')
    return running_race 


# Example: Collect data from Marathon in Lima 2017-2019
marathons = {'lima42k_2017':'https://pacifictiming.com/result-wizard/?prefix=170521_lima42k',
             'lima42k_2018':'https://pacifictiming.com/result-wizard/?prefix=170521_lima42k',
             'lima42k_2019':'https://pacifictiming.com/result-wizard/?prefix=190519_lima42k'
             }

dfs = {}
for running_race, link in marathons.items():
    print(running_race, '->', link)
    dfs[f'{running_race}'] = webscraping_running_peru(running_race,link,'D://Temp//chromedriver_win32//chromedriver.exe')
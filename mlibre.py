# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:24:35 2021

@author: Emanuel Caceres
"""

import requests
import json
import csv
import datetime
import numpy as np 


#response = requests.get('http://google.com',auth=('user', 'password')) 



url = 'https://jsonplaceholder.typicode.com/posts'
args = { 'userId': '8'}

response = requests.get(url, params=args)

print(response.status_code)

if response.status_code == 200:

    response_json = json.loads(response.text)
#    print(response_json)
#    print(type(response_json))
    
    
#### Formateo de fecha para archivo de salida ####
fecha= datetime.datetime.now().strftime("%Y%m%d%H%M%S")

name = "log"
filename = "logfile.%s.csv"  % fecha
print (filename)

header = ['ID Item', ';', 'Title del Item', ';' 'Category ID', ';' 'Name Category']
print (header)

lista=[]   
for d  in response_json:  
    lista.append(d["userId"])
    lista.append(d["title"])

print ("La lista....")
print (lista[3])

for n in lista:
     print (n)
     

#### dos formas de escritura numpy y with open####
np.savetxt("numpy_test.csv", lista, delimiter =",",fmt ='% s')


#### cambiar las xxxxxxx por el user donde se quiere dejar el archivo
with open('C:/Users/xxxxxxx/Desktop/python/' + filename, 'w', newline='') as csvfile:
 writer = csv.writer(csvfile, delimiter=' ')
 writer.writerow(header)
 
 for element in lista:
     writer.writerow(lista)
     


import requests
import pandas as pd
import zipfile
import os

# interesują nas dane od 2017.01 do 2019.11 (inne są chyba w nie tym formacie)
url = 'https://s3.amazonaws.com/tripdata/'
for month in range(12):
    data_file_name = '2017'
    if month+1<10:
        data_file_name += '0'
    data_file_name += str(month+1)+'-citibike-tripdata.csv.zip'
    
    myfile = requests.get(os.path.join(url,data_file_name))
    open(os.path.join(os.getcwd(),data_file_name), 'wb').write(myfile.content)
for month in range(12):
    data_file_name = '2018'
    if month+1<10:
        data_file_name += '0'
    data_file_name += str(month+1)+'-citibike-tripdata.csv.zip'
    
    myfile = requests.get(os.path.join(url,data_file_name))
    open(os.path.join(os.getcwd(),data_file_name), 'wb').write(myfile.content)
for month in range(11):
    data_file_name = '2019'
    if month+1<10:
        data_file_name += '0'
    data_file_name += str(month+1)+'-citibike-tripdata.csv.zip'
    
    myfile = requests.get(os.path.join(url,data_file_name))
    open(os.path.join(os.getcwd(),data_file_name), 'wb').write(myfile.content)

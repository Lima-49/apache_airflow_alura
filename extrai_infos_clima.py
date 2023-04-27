'''
This code is using the datetime, os, and pandas libraries to retrieve weather data for the city of
Boston from an API.
'''

from datetime import datetime, timedelta
import os
import pandas as pd

# date range
start_date = datetime.today()
end_date = start_date + timedelta(days=7)

# Formating date
start_date = start_date.strftime('%Y-%m-%d')
end_date = end_date.strftime('%Y-%m-%d')

# Inicializating API variables
CITY = 'SaoPaulo'
API_KEY = 'A2TA7636P5NUXA5RL69PDE4AK'
api_url = ("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" +
            f"{CITY}/{start_date}/{end_date}" + "?unitGroup=metric&include=days" +
            f"&key={API_KEY}&contentType=csv")

#Read the csv file from api
data = pd.read_csv(api_url)

#Create a folder of the date range extracted
file_path = f"C:/Users/Vitor Augusto/Documents/Programas/apache_airflow_alura/files/{start_date}/"
os.mkdir(file_path)

#Saving all the API data
data.to_csv(file_path+'api_data.csv', index=False, sep=',')

#Temperature data
data[['datetime', 'tempmin', 'tempmax']].to_csv(file_path+'temperature.csv', index=False, sep=',')

#Conditions data
data[['datetime', 'description', 'icon']].to_csv(file_path+'conditions.csv', index=False, sep=',')

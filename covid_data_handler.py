#----------------------------------------------------------------
'''
Importing all the modules needed for this project
'''
import pandas as pd
import csv
import json
from uk_covid19 import Cov19API
import logging_code as log
#----------------------------------------------------------------
#The first function that reads data from a csv file'''
csv_filename = 'nation_2021-10-28.csv'

def parse_csv_data(csv_filename:str) -> list:
    '''
    A function that takes an argument called csv_filename 
    '''
    #This logs the execution of the function into the logging file named
    #'logging_file.log'
    log.logger.info('The function parse_csv_data has been executed')
    #Opens the file named: 'nation_2021-10-28.csv' in read only mode
    with open(csv_filename, 'r') as csvRead:
        #Reads the file 
        csv_read_data = csv.reader(csvRead)
        covid_csv_data = list(csv_read_data)
        #Returns out every row in the file
        return(covid_csv_data)

#----------------------------------------------------------------
def process_covid_csv_data() -> int:
    '''process_covid_data function
    This function processes the data and returns 3 variables which
    are the last7days_cases, current_hospitalcases and total_deaths
    '''
    #This logs the execution of the function into the logging file named
    #'logging_file.log'
    log.logger.info('The function process_covid_csv_data has been executed')
    #Reads the file using pandas
    cells = pd.read_csv('nation_2021-10-28.csv')
    #Selects the cells in column 6 from 1,6 to 8,6 and adds them together
    last7days_cases = cells.iloc[2:9, 6].sum()
    #Selects the cell located in row 0, column 5
    current_hospital_cases = cells.iloc[0,5]
    #Selects the cell located in row 4, column 14
    total_deaths = cells.iloc[13,4]
    #Prints out the covid_csv_data 
    print(last7days_cases, current_hospital_cases, total_deaths)
#----------------------------------------------------------------
#API request that returns up to date covid data
#The API request that provides up to date covid data in the form 
#of a dictionary

#opens the file named 'config.json'
cf = open('config.json')
#loads the file
cf_load = json.load(cf)
#closes the file
cf.close()

def covid_API_request(location: str = "Exeter", location_type: str = "ltla") -> dict:
    '''
    The default values for this function is "Exeter" and "ltla"
    '''
    #This logs the execution of the function into the logging file named
    #'logging_file.log'
    log.logger.info('The funciton covid_API_request has been executed')
    #'Area' is the filters parameter
    Area = [
        f'areaName={location}',
        f'areaType={location_type}'
    ]
        #'information' is the structure of the information returned
    information = {
        "areaCode": "areaCode",
        "areaName": "areaName",
        "areaType": "areaType",
        "date": "date",
        "newCasesByPublishDateRollingSum": "newCasesByPublishDateRollingSum",
        "hospitalCases": "hospitalCases",
        "cumDeaths":"cumDeaths28DaysByDeathDate"
    }
    #'api' is the iniitialisation of Cov19API 
    api = Cov19API(filters = Area,
                    structure = information)
    #'data' is the extraction of the data using get_json()
    data = api.get_json()
    #Returns 'data'
    return(data)
#----------------------------------------------------------------
#Imports all the modules needed
from flask import Flask
from flask import render_template
import covid_news_handling as covNews
import covid_data_handler as covData
import logging_code as log
#----------------------------------------------------------------
#The Covid Data user interface 

#This is the user interface for this coursework and will be using a
#template called "index.html" to project the covid-19 data onto a web
#page

#gets functions from the other modules and callss the functions
news = covNews.news_API_request(covid_terms = "Covid-19 OR Coronavirus OR Covid")
covid_data_location_exe = covData.covid_API_request()
covid_data_location_eng = covData.covid_API_request('England','Nation')
#creates a flask instance
main = Flask(__name__)
#this binds a URL to a function
@main.route('/')
def index():
    #This logs the execution of the function into the logging file named
    #'logging_file.log'
    log.logger.info('The function index has been executed')
    #renders the content files

    return render_template("index.html",
        image = 'nhs.gif',
        title = 'Daily Covid Updates',
        location = covid_data_location_exe['data'][0]['areaName'],
        nation_location = covid_data_location_eng['data'][0]['areaName'],
        local_7day_infections = covid_data_location_exe['data'][0]['newCasesByPublishDateRollingSum'],
        national_7day_infections = covid_data_location_eng['data'][0]['newCasesByPublishDateRollingSum'],
        hospital_cases = 'Hospital Cases: ' + str(covid_data_location_eng['data'][0]['hospitalCases']),
        deaths_total = 'Total Deaths: ' + str(covid_data_location_eng['data'][0]['cumDeaths']),
        news_articles = news['articles']
        )
#If the variable name is equal to 'main' it will run the program with the debug off
if __name__ == '__main__':
    main.run(debug = False)
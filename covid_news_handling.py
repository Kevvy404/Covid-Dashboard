#Imports the modules needed
from newsapi import NewsApiClient
import json
from pprint import pprint
import logging_code as log

#opens the file named 'config.json'
cf = open('config.json')
#loads the file
cf_load = json.load(cf)
#closes the file
cf.close()

#News API request function
#This is where the information from news articles will be 
#sourced

def news_API_request(covid_terms: str = 'Covid-19 OR Coronavirus OR Covid') -> dict:
    '''
    This variable used the "NewsApiClient" which gets my personal api 
    key which allows information about the news articles from different
    sources
    '''
    #This logs the execution of the function into the logging file named
    #'logging_file.log'
    log.logger.info('This has executed the news_API_request function')
    #This is where I have used the newsapi module and have imported my api key
    #from the config file
    newsapi = NewsApiClient(api_key = cf_load['api_key'])
    #all_covid_articles gets all the articles based on covid using the queries 
    all_covid_articles = newsapi.get_everything(
        q=covid_terms,
        language='en',
        sort_by='publishedAt',
        page_size= 12)
    #Returns the articles
    return(all_covid_articles)

news_API_request()
#Imports the modules required
from covid_data_handler import *
import covid_news_handling
import logging_code as log

def test_parse_csv_data():
    '''
    tests if the data returns the correct information
    by checking the length of the file when using the 
    function
    '''
    data = parse_csv_data('nation_2021-10-28.csv')
    assert len(data) == 639
    if len(data) == 639:
        log.logger.debug('Test Successful')
    else:
        log.logger.error('Test Failed')
test_parse_csv_data()

def test_process_csv_data():
    '''
    tests if the data returned has the same values as the
    ones given
    '''
    last7days_cases, current_hospital_cases, total_deaths = process_covid_csv_data(parse_csv_data('nation_2021-10-28.csv'))
    assert last7days_cases == 240_299
    assert current_hospital_cases ==7_019
    assert total_deaths ==141_544
test_process_csv_data()

def test_covid_API_request():
    '''
    tests whether the data returned is the specified type 
    '''
    test = covid_API_request()
    assert isinstance(test, dict)
    if test == dict:
        log.logger.debug('Test Successful')
    else:
        log.logger.error('Test Failed')
test_covid_API_request()

def test_news_API_request():
    test = covid_news_handling.news_API_request()
    assert test
    assert covid_news_handling.news_API_request('Covid-19 OR Coronavirus OR Covid') == test
    if covid_news_handling.news_API_request('Covid-19 OR Coronavirus OR Covid') == test:
        log.logger.debug('Test Successful')
    else:
        log.logger.error('Test Failed')
test_news_API_request()

def test_get_from_config():
    '''
    tests whether the code reads and returns the correct data
    from the config file
    '''
    test = covid_news_handling.cf_load['areaName']
    assert test == 'England'
    if test == 'England':
        log.logger.debug('Test Successful')
    else:
        log.logger.error('Test Failure')
test_get_from_config()
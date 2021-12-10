#----------------------------------------------------------------

                    Contents of this File

    - Title
    - Introduction
    - Requirements
    - Installation
    - Running The Program
    - Configuration
    - Developer Details

#----------------------------------------------------------------

            Programming Project: 'Covid API Dashboard'

#----------------------------------------------------------------

This program is used to display the information about the recent
updates of the covid pandemic. The latest data will be displayed
on a web page (http://127.0.0.1:5000/). This will include the
latest news articles which are covid related; latest 7 day infection 
rate in the locally and nationally; hospital cases nationally
and also total deaths nationally. I have 

#----------------------------------------------------------------

To use the program, you'll need to install the modules on your
personal device. The modules that will need to be installed are
as listed:
    - newsapi
    - pandas
    - uk_covid19
    - flask

#----------------------------------------------------------------

For Windows:

To install the modules, you'll have to go to your Command Prompt
(cmd) and run it as admin. Then type into the console:
                            "pip install replaceWithPackageName"
Then hit enter and the package should install. The console should 
display "successfully installed"

For Mac:

To install the modules, you'll have to go to your terminal
and run it as admin. Then type into the console:
                            "pip install replaceWithPackageName"
Then hit enter and the package should install. The console should 
display "successfully installed"

You will also have to input your personal API key which can be found
on https://newsapi.org/ after you have registered an account on the
website. The API key is free but has a limited amount of requests
per day. After you have registered an account, you ca get your API
key and then be able to insert it into the config file. Replace 
"INSERT_YOUR_API_KEY_HERE" with your API key and then you should
be all good to go.

#---------------------------------------------------------------

To run the program, you'll have to open the module called 
'userInterface.py' and run the code. The URL (http://127.0.0.1:5000/)
of the web page should appear either in the terminal or the file 
named 'logging_file.log'. You'll be able to see the data displayed
on the Covid-19 dashboard.

#---------------------------------------------------------------

To configure the program, you'll have to open the 'config.json'
file and manually change the data in the dictionary. To change
the location, you'll have to change the 'areaName' and 'areaType'
to your desired locations. For example, you could change the areaName
to Wales instead of England.
        "areaName": "someLocationName"
        "areaType": "theLocationType"

#---------------------------------------------------------------

 - covid_data_handler.py : gets data from the publichealthengland API
 - covid_news_handling.py : gets articles from newsapi.org
 - userInterface.py : the file where the code is executed
 - logging_code.py : sets up the logging system to be used for functions
 - tests.py : tests the functions from the previous modules 
 - nation_2021-10-28.csv : a csv file that contains Covid-19 data 
 - logging_file.log : a log file where all the logging data is stored
 - config.json : a json file that contains sensitive information
 - templates/index.html : a folder containing a html file that has the
                          template for the Covid-19 Dashboard
 - static/images/nhs.gif : a folder containing a gif that has been 
                           rendered onto the dashboard

#---------------------------------------------------------------
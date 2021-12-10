#imports the logging module as log 
import logging as log

#creates a streamhandler with a default formatter
log.basicConfig(filename = 'logging_file.log',
                #This will be the format the logger 
                format = '%(asctime)s -- %(levelname)s -- %(funcName)s -- %(message)s',
                #The fule is opened in write mode
                filemode = 'w')
#The logger hierarchy must be defined explicitly in the logger name
logger = log.getLogger()
#specifies the lowest severity 
logger.setLevel(log.DEBUG)

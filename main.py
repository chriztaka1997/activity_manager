import json
from os import path
from datetime import date
from datetime import datetime as dt
import time

DATE_FORMAT = "%Y-%m-%d"

def printing_all(long_term, targets, today_activity):
    '''
    printing all current today related stuff

    :param long_term: set
    :param targets: set
    :param today_activity: set
    :return: none
    '''
    today_date = date.today()

    print("Long Term Targets: ")
    for i in long_term:
        #TODO: print in the format of "1. activity_name  type(proj/gym)  proggress/Des
        print(str(i)+". "+str(long_term[i]))


    print("Todays target: ")
    key = today_date.strftime(DATE_FORMAT)
    if key in targets:
        today_target = targets[key]
        for i in today_target:
            #TODO: print in the format of "1. activity_name  status
            print(str(i)+". "+str(today_target[i]))
    else: print("NONE")






def main():
    '''
    This is where all the user input going to be coded

    :return: None
    '''
    # Ask for user input
    # assuming the user input is always valid


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
    This is the main fucntion where the code going to be called
    all loads and dumps happens here

    :return: None
    '''

    ### Names for database ####
    long_term_path = "./Database/long_term_target.json"
    targets_path = "./Database/targets.json"
    today_activity_path = "./Database/today_activity.json"
    summary_path = "./Database/summary.json"
    weekly_summary_path = "./Database/weekly_summary.json"

    ## This is loading the database ###
    if (path.exists(long_term_path)): long_term_target = json.load(open(long_term_path,"r"))
    else: long_term_target = {}

    if (path.exists(targets_path)): targets = json.load(open(targets_path,"r"))
    else: targets = {}

    if (path.exists(today_activity_path)): today_activity = json.load(open(today_activity_path,"r"))
    else: today_activity = {}

    if(path.exists(summary_path)): summary = json.load(open(summary_path,"r"))
    else: summary = {}

    if (path.exists(weekly_summary_path)): weekly_summary = json.load(open(weekly_summary_path,"r"))
    else: weekly_summary = {}

    # Ask for user input
    # assuming the user input is always valid


    ## This json dump, loading back the data#####
    json.dump(long_term_target, open(long_term_path, 'w'))
    json.dump(targets, open(targets_path, 'w'))
    json.dump(today_activity, open(today_activity_path, 'w'))
    json.dump(summary, open(summary_path, 'w'))
    json.dump(weekly_summary, open(weekly_summary_path, 'w'))

# main()

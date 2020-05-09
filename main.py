import json
from os import path
import time


def printing_all(long_term, targets, today_activity):
    '''
    printing all current today related stuff

    :param long_term: set
    :param targets: set
    :param today_activity: set
    :return: none
    '''
    print("Long Term Targets: ")
    for i in long_term:
        print("")



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
    if (path.exists(long_term_path)): long_term_target = json.loads(open(long_term_path,"r"))
    else: long_term_target = {}

    if (path.exists(targets_path)): targets = json.loads(open(targets_path,"r"))
    else: targets = {}

    if (path.exists(today_activity_path)): today_activity = json.loads(open(today_activity_path,"r"))
    else: today_activity = {}

    if(path.exists(summary_path)): summary = json.loads(open(summary_path,"r"))
    else: summary = {}

    if (path.exists(weekly_summary_path)): weekly_summary = json.loads(open(weekly_summary_path,"r"))
    else: weekly_summary = {}

    # Ask for user input
    # assuming the user input is always valid



    # TODO: json dumps

# main()
print(time.localtime())
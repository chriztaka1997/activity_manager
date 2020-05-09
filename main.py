import json
from os import path


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
    if (path.exists(long_term_path)): long_term_target = json.loads(open(long_term_path))
    else: long_term_target = {}

    if (path.exists(targets_path)): targets = json.loads(open(targets_path))
    else: targets = {}

    if (path.exists(today_activity_path)): today_activity = json.loads(open(today_activity_path))
    else: today_activity = {}

    if(path.exists(summary_path)): summary = json.loads(open(summary_path))
    else: summary = {}

    if (path.exists(weekly_summary_path)): weekly_summary = json.loads(open(weekly_summary_path))
    else: weekly_summary = {}





    print("Hello World")
    print("Testing shortcut")
    for x in long_term_target:
        print(str(x)+". "+long_term_target[x])

    # TODO: json dumps

main()
from os import path
import json
from datetime import date
from datetime import datetime as dt

DATE_FORMAT = "%Y-%m-%d"

# This is the path to the database
long_term_path = "./Database/long_term_target.json"
targets_path = "./Database/targets.json"
today_activity_path = "./Database/today_activity.json"
summary_path = "./Database/summary.json"
weekly_summary_path = "./Database/weekly_summary.json"

attributes = {'an' :"activity_name", 'des': 'description','st':'start_time','pr':'productive_rate','eg':'exercise_goal',
              'tg':'time_on_game','ts':'time_on_ssn','w':'weight'}

class Journal:

    def __init__(self):
        ## This is loading the database ###
        if (path.exists(long_term_path)): self.long_term_target = json.load(open(long_term_path, "r"))
        else: self.long_term_target = {}

        if (path.exists(targets_path)): self.targets = json.load(open(targets_path, "r"))
        else: self.targets = {}

        if (path.exists(today_activity_path)): self.today_activity = json.load(open(today_activity_path, "r"))
        else: self.today_activity = {}

        if (path.exists(summary_path)): self.summary = json.load(open(summary_path, "r"))
        else: self.summary = {}

        if (path.exists(weekly_summary_path)): self.weekly_summary = json.load(open(weekly_summary_path, "r"))
        else: self.weekly_summary = {}

    def get_long_term(self):
        '''
        Get the information in the long term project
        :return: A set
        '''
        return self.long_term_target

    def append_long_term(self, activity, des):
        '''
        append an info to the long term database
        :param activity: str
        :param des: str
        :return: none
        '''
        length = len(self.long_term_target)
        self.long_term_target[length+1] = {attributes['an']:activity,attributes['des']:des}

    def update_long_term(self,num,activity, des):
        self.long_term_target[num]= {attributes['an']:activity,attributes['des']:des}

    def get_target(self,date):
        return self.targets[date]

    def append_target_on_date(self, date, target_name, des):
        target_date = self.targets[date]
        length = len(target_date)
        target_date[length+1] = {attributes['an']:target_name,attributes['des']:des}

    def update_target_on_date(self,date, num, target_name, des):
        target_date = self.targets[date]
        target_date[num] = {attributes['an']:target_name,attributes['des']:des}

    def get_today_activity(self,date):
        return self.today_activity[date]

    def append_today_activity(self,date, activity_name, time):
        today_act = self.today_activity[date]
        length = len(today_act)
        today_act[length+1] = {attributes['an']:activity_name,attributes['st']:time}

    def update_today_activity(self, date, num,activity_name, time ):
        today_act = self.today_activity[date]
        today_act[num] = {attributes['an']:activity_name,attributes['st']:time}

    def get_summary(self, date):
        return self.summary[date]

    def append_summary(self,date, productive_rate, exercise_goal, time_on_game, time_on_sm,weight):
        self.summary[date] = {attributes['pr']: productive_rate, attributes['eg']: exercise_goal,
                              attributes['tg']: time_on_game, attributes['ts']: time_on_sm, attributes['w']:weight}

    def update_summary(self,date, productive_rate, exercise_goal, time_on_game, time_on_sm,weight):
        self.summary[date] = {attributes['pr']: productive_rate, attributes['eg']: exercise_goal,
                              attributes['tg']: time_on_game, attributes['ts']: time_on_sm, attributes['w']:weight}

    def get_weekly_summary(self, date):
        return self.summary[date]

    def append_weekly_summary(self, date, productive_rate, exercise_goal, time_on_game, time_on_sm, weight):
        self.weekly_summary[date] = {attributes['pr']: productive_rate, attributes['eg']: exercise_goal,
                              attributes['tg']: time_on_game, attributes['ts']: time_on_sm, attributes['w']:weight}

    def update_weekly_summary(self, date, productive_rate, exercise_goal, time_on_game, time_on_sm, weight):
        self.weekly_summary[date] = {attributes['pr']: productive_rate, attributes['eg']: exercise_goal,
                              attributes['tg']: time_on_game, attributes['ts']: time_on_sm, attributes['w']:weight}


    def store_data(self):
        ## This json dump, loading back the data#####
        json.dump(self.long_term_target, open(long_term_path, 'w'))
        json.dump(self.targets, open(targets_path, 'w'))
        json.dump(self.today_activity, open(today_activity_path, 'w'))
        json.dump(self.summary, open(summary_path, 'w'))
        json.dump(self.weekly_summary, open(weekly_summary_path, 'w'))

    def display_today(self):
        '''
        printing all current today related stuff

        :param long_term: set
        :param targets: set
        :param today_activity: set
        :return: none
        '''
        key= date.today()

        print("Long Term Targets: ")
        if self.long_term_target == {}: print("None")
        else:
            for i in self.long_term_target:
                print(str(i) + ". " + str(self.long_term_target[i][attributes['an']]) + "   "+
                      str(self.long_term_target[i][attributes['des']]))

        print("\n")
        print("Today's target: ")
        if key in self.targets:
            today_target = self.targets[key]
            if today_target == {}:print("None")
            else:
                for num_target in today_target:
                    print(str(num_target) + ". " + str(today_target[num_target][attributes['an']])+ "  "+
                          str(today_target[num_target][attributes['des']]))
        else:
            print("None")

        print("\n")
        print("Today's activity: ")
        if key in self.today_activity:
            today_activity = self.today_activity[key]
            if today_activity == {}:print("None")
            else:
                for num_activity in today_activity:
                    print(str(num_activity) + ". " + str(today_activity[num_activity][attributes['an']]) + "  " +
                          str(today_activity[num_activity][attributes['st']]))
        else:
            print("None")

        print("\n")
        print("Summary of the day: ")
        if self.summary[key] == {}: print("None")
        else:
            print("Productive rate: ", self.summary[key][attributes['pr']])
            print("Excercise goal: ", self.summary[key][attributes['eg']])
            print("Time on game: ", self.summary[key][attributes['tg']])
            print("Time on Social Media: ", self.summary[key][attributes['ts']])
            print("Weight today: ", self.summary[key][attributes['w']])

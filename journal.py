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

        self.attributes = {'an': "activity_name", 'des': 'description', 'st': 'start_time', 'pr': 'productive_rate',
                      'eg': 'exercise_goal',
                      'tg': 'time_on_game', 'ts': 'time_on_ssn', 'w': 'weight', 'sd': "start_date", 'ed': "end_date"}

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
        self.long_term_target[str(length+1)] = {self.attributes['an']:activity,self.attributes['des']:des}

    def update_long_term(self,num,activity, des):
        self.long_term_target[num]= {self.attributes['an']:activity,self.attributes['des']:des}

    def del_long_term(self, num):
        length = len(self.long_term_target)
        if num == str(length): del self.long_term_target[num]
        else:
            for i in range(int(num), length):
                self.long_term_target[str(i)] = self.long_term_target[str(i+1)]
            del self.long_term_target[str(length)]


    def get_target_on_date(self,d):
        return self.targets[d]

    def append_target_on_date(self, d, target_name, des):
        try:
            target_date = self.targets[d]
            length = len(target_date)
        except KeyError:
            self.targets[d] = {}
            target_date = self.targets[d]
            length = 0
        target_date[str(length+1)] = {self.attributes['an']:target_name,self.attributes['des']:des}

    def update_target_on_date(self,d, num, target_name, des):
        target_date = self.targets[d]
        target_date[num] = {self.attributes['an']:target_name,self.attributes['des']:des}

    def del_target_on_date(self,d,num):
        target_date = self.targets[d]
        length = len(target_date)
        if int(num) == length:
            del target_date[num]
        else:
            for i in range(int(num), length):
                target_date[str(i)] = target_date[str(i + 1)]
            del target_date[str(length)]


    def get_today_activity(self,d):
        return self.today_activity[d]

    def append_today_activity(self,d, activity_name, time):
        try:
            today_act = self.today_activity[d]
            length = len(today_act)
        except KeyError:
            self.today_activity[d] = {}
            today_act = self.today_activity[d]
            length = 0

        today_act[str(length+1)] = {self.attributes['an']:activity_name,self.attributes['st']:time}

    def update_today_activity(self, d, num,activity_name, time ):
        today_act = self.today_activity[d]
        today_act[num] = {self.attributes['an']:activity_name,self.attributes['st']:time}

    def del_today_activity(self,d, num):
        activity_date = self.today_activity[d]
        length = len(activity_date)
        if int(num) == length:
            del activity_date[num]
        else:
            for i in range(int(num), length):
                activity_date[str(i)] = activity_date[str(i + 1)]
            del activity_date[str(length)]

    def get_summary(self, d):
        return self.summary[d]

    def append_summary(self,d, productive_rate, exercise_goal, time_on_game, time_on_sm,weight):
        self.summary[d] = {self.attributes['pr']: productive_rate, self.attributes['eg']: exercise_goal,
                              self.attributes['tg']: time_on_game, self.attributes['ts']: time_on_sm,
                           self.attributes['w']:weight}

    def update_summary(self,d, productive_rate, exercise_goal, time_on_game, time_on_sm,weight):
        self.summary[d] = {self.attributes['pr']: productive_rate, self.attributes['eg']: exercise_goal,
                              self.attributes['tg']: time_on_game, self.attributes['ts']: time_on_sm, self.attributes['w']:weight}

    def get_weekly_summary(self, d):
        return self.summary[d]

    def append_weekly_summary(self, d, star_date, end_date,productive_rate, exercise_goal, time_on_game, time_on_sm, weight):
        self.weekly_summary[d] = {self.attributes['st']:star_date,self.attributes['ed']:end_date,self.attributes['pr']: productive_rate,
                                  self.attributes['eg']: exercise_goal,
                              self.attributes['tg']: time_on_game, self.attributes['ts']: time_on_sm, self.attributes['w']:weight}

    def update_weekly_summary(self, d, star_date, end_date, productive_rate, exercise_goal, time_on_game, time_on_sm, weight):
        self.weekly_summary[d] = {self.attributes['st']:star_date,self.attributes['ed']:end_date,self.attributes['pr']: productive_rate,
                                  self.attributes['eg']: exercise_goal,
                              self.attributes['tg']: time_on_game, self.attributes['ts']: time_on_sm, self.attributes['w']:weight}




    def display_today(self):
        '''
        printing all current today related stuff

        :param long_term: set
        :param targets: set
        :param today_activity: set
        :return: none
        '''
        key= date.today().strftime(DATE_FORMAT)

        print("Long Term Targets: ")
        if self.long_term_target == {}: print("None")
        else:
            for i in self.long_term_target:
                print(str(i) + ". " + str(self.long_term_target[i][self.attributes['an']]) + "   "+
                      str(self.long_term_target[i][self.attributes['des']]))

        print("\n")
        print("Today's target: ")
        if key in self.targets:
            today_target = self.targets[key]
            if today_target == {}:print("None")
            else:
                for num_target in today_target:
                    print(str(num_target) + ". " + str(today_target[num_target][self.attributes['an']])+ "  "+
                          str(today_target[num_target][self.attributes['des']]))
        else:
            print("None")

        print("\n")
        print("Today's activity: ")
        if key in self.today_activity:
            today_activity = self.today_activity[key]
            if today_activity == {}:print("None")
            else:
                for num_activity in today_activity:
                    print(str(num_activity) + ". " + str(today_activity[num_activity][self.attributes['an']]) + "  " +
                          str(today_activity[num_activity][self.attributes['st']]))
        else:
            print("None")

        print("\n")
        print("Summary of the day: ")
        try:
            check = (self.summary[key] == {})
        except KeyError:
            check = True

        if check:
            print("None")
        else:
            print("Productive rate: ", self.summary[key][self.attributes['pr']])
            print("Excercise goal: ", self.summary[key][self.attributes['eg']])
            print("Time on game: ", self.summary[key][self.attributes['tg']])
            print("Time on Social Media: ", self.summary[key][self.attributes['ts']])
            print("Weight today: ", self.summary[key][self.attributes['w']])

    def display_long_term(self):
        print("Long Term Targets: ")
        if self.long_term_target == {}:
            print("None")
        else:
            for i in self.long_term_target:
                print(str(i) + ". " + str(self.long_term_target[i][self.attributes['an']]) + "   " +
                      str(self.long_term_target[i][self.attributes['des']]))

    def display_target(self,key):
        print("\n")
        print(key+" target : ")
        if key in self.targets:
            today_target = self.targets[key]
            if today_target == {}:
                print("None")
            else:
                for num_activity in today_target:
                    print(str(num_activity) + ". " + str(today_target[num_activity][self.attributes['an']]) + "  " +
                          str(today_target[num_activity][self.attributes['des']]))
        else:
            print("None")

    def display_activity(self,key):
        print("\n")
        print(key+" activity: ")
        if key in self.today_activity:
            today_activity = self.today_activity[key]
            if today_activity == {}:
                print("None")
            else:
                for num_activity in today_activity:
                    print(str(num_activity) + ". " + str(today_activity[num_activity][self.attributes['an']]) + "  " +
                          str(today_activity[num_activity][self.attributes['st']]))
        else:
            print("None")

    def display_summary(self,key):
        print("\n")
        print("Summary of the "+key+": ")
        if not(key in self.summary):
            print("None")
        else:
            print("Productive rate: ", self.summary[key][self.attributes['pr']])
            print("Excercise goal: ", self.summary[key][self.attributes['eg']])
            print("Time on game: ", self.summary[key][self.attributes['tg']])
            print("Time on Social Media: ", self.summary[key][self.attributes['ts']])
            print("Weight today: ", self.summary[key][self.attributes['w']])

    def display_weekly_summary(self,key):
        print("\n")
        print("Weekly summary of "+key+": ")
        for week in self.weekly_summary:
            if self.weekly_summary[week][self.attributes['sd']] < key < self.weekly_summary[week][self.attributes['ed']]:
                print("Productive rate: ", self.weekly_summary[week][self.attributes['pr']])
                print("Excercise goal: ", self.weekly_summary[week][self.attributes['eg']])
                print("Time on game: ", self.weekly_summary[week][self.attributes['tg']])
                print("Time on Social Media: ", self.weekly_summary[week][self.attributes['ts']])
                print("Weight today: ", self.weekly_summary[week][self.attributes['w']])
                return
        print("None")

    def generate_weekly_summary(self):
        print("Generating weekly summary")


    def store_data(self):
        ## This json dump, loading back the data#####
        json.dump(self.long_term_target, open(long_term_path, 'w'))
        json.dump(self.targets, open(targets_path, 'w'))
        json.dump(self.today_activity, open(today_activity_path, 'w'))
        json.dump(self.summary, open(summary_path, 'w'))
        json.dump(self.weekly_summary, open(weekly_summary_path, 'w'))


    def end(self):
        self.store_data()
        print("Data is stored")



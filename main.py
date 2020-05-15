import json
from os import path
from datetime import date
from datetime import datetime as dt
import time
from journal import Journal

DATE_FORMAT = "%Y-%m-%d"


def add_input(journal):
    print("\n")
    print("What to add: ")
    print("1. An activity")
    print("2. Long term target")
    print("3. Target for a specific date")
    print("4. A summary")
    option = input("Which option: ")
    print()
    #assumming that the user input is never wrong
    if(option ==1):
        print("Adding an activity for today")
        today_date = date.today()
        start_time = input("What is the start time: ")
        activity_name = input("What is the activity name: ")
        journal.append_today_activity(today_date, activity_name, start_time)
        print("Activity is added\n")
    elif(option == 2):
        print("Adding a long term target")
        activity_name = input("What is the activity name: ")
        activity_des = input("What is the description to this activity: ")
        journal.append_long_term(activity_name,activity_des)
        print("Long term target is added\n")
    elif(option == 3):
        print("Which day do you want to add the target: ")
        print("1. today")
        print("2. Specific day")
        respond = input("Enter your responds: ")
        print()
        if (respond == 1):
            print("Adding a target for today")
            today_date = date.today()
            activity_name = input("What is the activity name: ")
            activity_des = input("What is the description to this activity: ")
            journal.append_target_on_date(today_date, activity_name,activity_des)

        elif(respond ==2):
            print("Adding a target for today")
            today_date = input("What is the date in format(YYYY-mm-dd): ")
            activity_name = input("What is the activity name: ")
            activity_des = input("What is the description to this activity: ")
            journal.append_target_on_date(today_date, activity_name, activity_des)
        print("Target is added\n")

    elif(option == 4):
        time_now = dt.today()
        today_8pm  = time_now.replace(hour= 19, minute=0, second=0)
        if(time_now> today_8pm):print("The time is not appropriate to make a summary.")
        else:
            print("Adding summary")
            productive_rate = input("what is the productive rate today: ")
            exercise_goal = input("Is the exercise goal achieved: ")
            time_on_game = input("Time spent on game: ")
            time_on_sm = input("Time spend on social media: ")
            weight = input("What is the current weight today: ")
            journal.append_summary(time_now.date(), productive_rate, exercise_goal,time_on_game,time_on_sm,weight)
            print("Summary is added\n")




def update_input(journal):
    print()

def delete_input(journal):
    print()

def user_input(journal):
    print("\n")
    print("Option to choose from: ")
    print("1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. Show today detail")
    print("5. quit")
    #assumming that the user input is never wrong
    option = input("which option: ")
    if(option == 1): add_input(journal)
    elif (option == 2): update_input(journal)
    elif (option == 3): delete_input(journal)
    elif(option == 4): journal.display_today()
    else: return False
    return True




def main():
    '''
    This is where all the user input going to be coded

    :return: None
    '''
    # Ask for user input
    # assuming the user input is always valid

    journal = Journal()
    journal.display_today()

    loop = True
    while loop:
        loop = user_input(journal)

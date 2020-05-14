import json
from os import path
from datetime import date
from datetime import datetime as dt
import time
from journal import Journal

DATE_FORMAT = "%Y-%m-%d"


def user_input():
    print("\n")
    print("Option to choose from: ")
    print("1. Add")
    print("2. Update")
    print("3. Delete")



def main():
    '''
    This is where all the user input going to be coded

    :return: None
    '''
    # Ask for user input
    # assuming the user input is always valid

    journal = Journal()
    journal.display_today()
    user_input()

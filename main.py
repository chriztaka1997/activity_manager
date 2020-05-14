import json
from os import path
from datetime import date
from datetime import datetime as dt
import time
from journal import Journal

DATE_FORMAT = "%Y-%m-%d"








def main():
    '''
    This is where all the user input going to be coded

    :return: None
    '''
    # Ask for user input
    # assuming the user input is always valid

    journal = Journal()


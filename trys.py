

from curses.ascii import isalpha
from unicodedata import name


def user_data(name,purchase,):
    valid_name = False
    user_name = input("Please Enter your name, hit enter when done: ")
    if (user_name == isalpha()):
        updater = user_name.format("")
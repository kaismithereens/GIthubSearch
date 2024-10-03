import argparse
import sys
from pyfiglet import Figlet
import random


#Create a welcome screen that appears when user starts the program
#Return explanatory message about program's main purpose, stored as string

def welcome_screen():
    welcome = "GitHub Search"
    f = Figlet(font='stop')
    print(f.renderText(f"{welcome}"))

    header = 'This program allows users to search through GitHub repositories.\nTo exit the program at any time, press "CTRL" + "D"'
    return (f"{header}\n")

#Display all possible options end-user can choose
#Display how to exit the program
#Returns all different options, stored as tuple

def welcome_screen_options():
    message = 'To display options click "y".'
    option1 = "1. Display all my Github repositories."
    option2 = "2. Display Harvard repositories with most stars."
    option3 = "3. Display GitHub's repositories with most popular Python projects."
    option4 = "4. Save most popular Python repositories locally."
    option5 = "5. Save most popular Harvard repositories locally."
    option6 = "6. Save my profile image locally."
    option7 = "7. Search all repositories by providing a search term."
    option8 = "8. Search for all repositores by providing owner's name."
    exit_message = 'To exit the program at any time, press "CTRL" + "D".'

    return message, option1, option2, option3, option4, option5, option6, option7, option8, exit_message

"""
#If you want to change the font, you can use the code below to list all possible fonts:

figlet = Figlet()
myfonts = figlet.getFonts()
print(myfonts)
"""

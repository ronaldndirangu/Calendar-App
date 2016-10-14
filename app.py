#from app.models import CalendarModels
#from app.views import CalendarViews
import os
from time import sleep

class AppRun(object):

    def display_title(self):
        os.system('cls')
        print("\t+++++++++++++++++++++++++++++++++")
        print("\t+++++++++ Calender Tusker +++++++")
        print("\t+++++++++++++++++++++++++++++++++")

    def user_command(self):
        print("Press[1] to view a list of events")
        print("Press[2] to add event to Calender")
        print("Press[3] to view the last event")
        print("press 'q' to quit!")

        selection  = input("Enter 1,2,3 or 4 \n")
        return selection


#Main app part
app = AppRun()
app.display_title()
selection = ""
while selection != 'q':

    app.display_title()
    if selection == "1":
        print("Current Events are:\n")
        #display_events()
        input("Press Enter to continue")

    elif selection == "2":
        #add_event()
        print("Event has Been added")
        input("Press Enter to continue")

    elif selection == "3":
        print("Last Event is \n")
        #last_event()
        input("Press Enter to continue")

    else:
        print("Invalid choice try again")
    selection = app.user_command()

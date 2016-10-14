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

        print("Press[1] to create callendar")
        print("Press[2] to view a list of events")
        print("Press[3] to add event to Calender")
        print("Press[4] to view the last event")
        print("\npress 'q' to quit!")

        selection  = input("\nEnter 1,2,3 or 4 \n")
        return selection

#Main app part
app = AppRun()
app.display_title()
selection = app.user_command()

while selection != 'q':

    app.display_title()
    if selection == "1":
        print("Enter a name of the type of calendar you want:\n")
        #display_events()
        input("Press Enter to continue")

    elif selection == "2":
        print("A view of a list of events")
        #add_event()
        input("Press Enter to continue")

    elif selection == "3":
        #app.display_event()
        print("Event Added to calendar\n")
        input("Press Enter to continue")

    elif selection == "4":
        print("Last Event is \n")
        #app.display_last_event()
        input("Press Enter to continue")

    else:
        print("Invalid choice try again\n")
    selection = app.user_command()

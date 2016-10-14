import os
import json

clear = lambda: os.system('cls')

with open("calendar.json", "r") as cal:
	try:
		cal_dict = json.load(cal)
	# if the file is empty the ValueError will be thrown
	except ValueError:
		cal_dict = {}
	print "Menu\n", "-"*4
	print "1. View Calendar\n2. Create Calendar\n\n"
	option = raw_input("Choose an option: ")

	if option == str(1):
		clear()
		print "1. Add Event\n2. List Events\n3. View Last Event\n"
	elif option == str(2):
		new_cal_name = raw_input("Give the Calendar a name: ")
		cal_dict[new_cal_name] = {}
		print cal_dict
		

with open("calendar.json", "w") as cal:
	try:
		json.dump(cal_dict, cal)
	except ValueError:
		cal_dict = {}
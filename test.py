import os
import json
from datetime import datetime

clear = lambda: os.system('cls')


def add_event(selected_cal):
	# print "\nYou are in the", selected_cal, "Calendar\n"
	date = raw_input("Enter the Date of the event: ")
	name = raw_input("Enter the event name: ")
	start = raw_input("Enter the Start Time: ")
	stop = raw_input("Enter the Stop Time: ")
	description = raw_input("Enter the Description(optional): ")
	location = raw_input("Enter the location of the event(optional): ")
	try:
		cal_dict[selected_cal][date] = {}
		cal_dict[selected_cal][date]["Date"] = date
		cal_dict[selected_cal][date]["Start Time"] = start
		cal_dict[selected_cal][date]["Stop Time"] = stop
		cal_dict[selected_cal][date]["Event Name"] = name
		cal_dict[selected_cal][date]["Description"] = description
		cal_dict[selected_cal][date]["Location"] = location
		cal_dict[selected_cal][date]["Created On"] = str(datetime.now())
		print "Successfuly created the", name, "Event"
	except:
		raise("Something is wrong with the DB")

with open("calendar.json", "r") as cal:
	try:
		cal_dict = json.load(cal)
	# if the file is empty the ValueError will be thrown
	except ValueError:
		cal_dict = {}
	print "\nMenu\n", "-"*4
	print "1. View Calendar\n2. Create Calendar\n\n"
	option = raw_input("Choose an option: ")

	if option == str(1):
		clear()
		print "Select a Calendar below\n"
		for key in cal_dict.keys():
			print key
		selected_cal = raw_input("\nType the name of any calendar from above: ")
		clear()
		print "\nYou are in the", selected_cal, "Calendar\n\n1. Add Event\n2. List Events\n3. View Last Event\n"
		selected_task = raw_input("Choose a task: ")
		if selected_task == str(1):
			add_event(selected_cal)
	elif option == str(2):
		new_cal_name = raw_input("Give the Calendar a name: ")
		cal_dict[new_cal_name] = {}
		print cal_dict
		

with open("calendar.json", "w") as cal:
	try:
		json.dump(cal_dict, cal)
	except ValueError:
		cal_dict = {}
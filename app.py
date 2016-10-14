from app.models import CalendarModels
from app.views import CalendarViews

class AppRun(object):
	
	def __init__(self):
		pass

	def view_calendar(self, name):
		with open("calendar.db", "r") as cal:
			cal_dict = eval(cal.read())

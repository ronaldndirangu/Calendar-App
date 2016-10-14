import calendar
from models import CalendarModels


class CalendarViews(object):
    def __init__(self):
        pass

    def find_last_event(self, calendar):
    	last_event = max(calendar.items(), key=lambda x: x[1]['Date'])[1]
    	return last_event

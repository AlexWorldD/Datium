__author__ = 'Admin'
from timetable.models import Timetable, Lesson, DayInTimetable, WeekInTimetable, LessonInTimeTable
import datetime

def start_and_end_of_lesson(class_number):
    if class_number == 1:
        return (datetime.time(9,30,0,0,datetime.timezone(datetime.timedelta(hours=3))), datetime.time(11,5,0,0,datetime.timezone(datetime.timedelta(hours=3))))
    elif class_number == 2:
        return (datetime.time(11,15,0,0,datetime.timezone(datetime.timedelta(hours=3))), datetime.time(12,50,0,0,datetime.timezone(datetime.timedelta(hours=3))))
    elif class_number == 3:
        return (datetime.time(13,50,0,0,datetime.timezone(datetime.timedelta(hours=3))), datetime.time(15,25,0,0,datetime.timezone(datetime.timedelta(hours=3))))
    elif class_number == 2:
        return (datetime.time(15,35,0,0,datetime.timezone(datetime.timedelta(hours=3))), datetime.time(17,10,0,0,datetime.timezone(datetime.timedelta(hours=3))))
    elif class_number == 2:
        return (datetime.time(17,20,0,0,datetime.timezone(datetime.timedelta(hours=3))), datetime.time(18,55,0,0,datetime.timezone(datetime.timedelta(hours=3))))

import datetime
import pickle
from utils.lecture import Lecture
from utils.attender import Attender
import threading

# Get Lecture Details
# Flag: Current Lecture Session Status
# Import TT from CSV

with open('timetable.pickle','rb') as f:
    timetable = pickle.load(f)


# Get current time params
nowTime = datetime.datetime.now()
currentDay = nowTime.strftime('%a')
currentTime = nowTime.time().replace(microsecond=0,second=0)


# get current lecture
for lecture in timetable[currentDay]:
    if lecture.start_time <= currentTime  <= lecture.end_time:
        print(lecture.subject, lecture.meetcode)

def attendLecture():
    # You can access "attend" variable in this function
    threading.Timer(60, attendLecture).start()
    if attend.currentLecture == None:
        attend.join_meet('BECMPNA')

def launch():
    global attend
    attend = Attender()
    attendLecture()

launch()


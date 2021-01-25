import datetime
import pickle
from utils.lecture import Lecture
from utils.attender import Attender


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


def launch():
    attend = Attender()
    attend.join_meet('BECMPNA')

# launch()

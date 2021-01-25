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
currentTime = nowTime.strftime('%H:%M')


def launch():
    attend = Attender()
    attend.join_meet('BECMPNA')

# launch()

import time
import pickle
from utils.lecture import Lecture
from utils.attender import Attender


# Get Lecture Details
# Flag: Current Lecture Session Status
# Import TT from CSV

with open('timetable.pickle','rb') as f:
    timetable = pickle.load(f)
print(timetable)

def launch():
    attend = Attender()
    attend.join_meet('BECMPNA')

# launch()

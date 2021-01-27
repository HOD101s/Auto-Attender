import datetime
import pickle
import argparse
from utils.lecture import Lecture
from utils.attender import Attender
import timetable_builder
import threading


parser = argparse.ArgumentParser(description='Auto Attender System')
parser.add_argument('-build-sc', '--build_schedule',
                    default=True, type=bool, help='run schedule builder')
args = parser.parse_args()


# In seconds
launch_interval = 60

# build timetable into timetable.pickle
if args.build_schedule:
    # print('Building Timetable')
    timetable_builder.buildtimetable()
    # print('Timetable Built')

# print("Fetching Timetable")
with open('schedule.pickle', 'rb') as f:
    timetable = pickle.load(f)


# Get current lecture meet code
def getCurrentMeetCode():
    # Get current time params
    nowTime = datetime.datetime.now()
    currentDay = nowTime.strftime('%a')
    currentTime = nowTime.time().replace(microsecond=0, second=0)
    # get current lecture
    for lecture in timetable[currentDay]:
        if lecture.start_time <= currentTime < lecture.end_time:
            return lecture.meetcode
    return None


# get end time for last lecture ie. end of lectures for that day
def getLastLectureEndTime():
    currentDay = datetime.datetime.now().strftime('%a')
    endOfLectures = datetime.datetime(1970, 1, 1, 0, 0).time()
    for lecture in timetable[currentDay]:
        endOfLectures = max(lecture.end_time, endOfLectures)
    return endOfLectures


def attendLecture():
    # You can access "attend" variable in this function
    threading.Timer(launch_interval, attendLecture).start()
    # Gets current lecture meetcode
    currentMeet = getCurrentMeetCode()
    # attend.currentLecture is None for no ongoing meet : attend.currentLecture != currentMeet if next meetcode is different from current meet
    if attend.currentLecture == None or attend.currentLecture != currentMeet:
        # if currentMeet is not None
        if currentMeet:
            attend.join_meet(currentMeet)
        # if college hasnt ended for the day
        elif datetime.datetime.now().time() < lastLectureEndTime:
            if attend.driver.current_url != 'https://www.google.com/':
                attend.driver.get('https://www.google.com/')
            attend.currentLecture = None
            attend.driver.minimize_window()
        # college lectures ended for the day
        else:
            attend.driver.quit()


def launch():
    global attend, lastLectureEndTime
    lastLectureEndTime = getLastLectureEndTime()
    attend = Attender(block_mic_cam=False, mute_audio=False)
    attendLecture()


launch()

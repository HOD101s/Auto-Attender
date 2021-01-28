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


class Scheduler:
    def __init__(self, launch_interval, build_schedule, block_mic_cam, mute_audio):
        self.launch_interval = launch_interval
        if build_schedule:
            timetable_builder.buildtimetable()
        with open('schedule.pickle', 'rb') as f:
            self.timetable = pickle.load(f)
        self.lastLectureEndTime = self.getLastLectureEndTime()
        self.attend = Attender(block_mic_cam=False, mute_audio=False)

    # get end time for last lecture ie. end of lectures for that day
    def getLastLectureEndTime(self):
        currentDay = datetime.datetime.now().strftime('%a')
        endOfLectures = datetime.datetime(1970, 1, 1, 0, 0).time()
        for lecture in self.timetable[currentDay]:
            endOfLectures = max(lecture.end_time, endOfLectures)
        return endOfLectures

    # Get current lecture meet code
    def getCurrentMeetCode(self):
        # Get current time params
        currentDateTime = datetime.datetime.now()
        currentDay = currentDateTime.strftime('%a')
        currentTime = currentDateTime.time().replace(microsecond=0, second=0)
        # get current lecture
        for lecture in self.timetable[currentDay]:
            if lecture.start_time <= currentTime < lecture.end_time:
                return lecture.meetcode
        return None

    def attendLecture(self):
        # You can access "attend" variable in this function
        threading.Timer(self.launch_interval, self.attendLecture).start()
        # Gets current lecture meetcode
        currentMeet = self.getCurrentMeetCode()
        # attend.currentLecture is None for no ongoing meet : attend.currentLecture != currentMeet if next meetcode is different from current meet
        if self.attend.currentLecture == None or self.attend.currentLecture != currentMeet:
            # if currentMeet is not None
            if currentMeet:
                self.attend.driver.maximize_window()
                self.attend.join_meet(currentMeet)
            # if college hasnt ended for the day
            elif datetime.datetime.now().time() < self.lastLectureEndTime:
                if self.attend.driver.current_url != 'https://www.google.com/':
                    self.attend.driver.get('https://www.google.com/')
                self.attend.currentLecture = None
                self.attend.driver.minimize_window()
            # college lectures ended for the day
            else:
                self.attend.driver.quit()


scheduler = Scheduler(20, args.build_schedule, False, False)
scheduler.attendLecture()

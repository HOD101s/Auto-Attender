import pickle
import datetime
import pandas as pd
from utils.lecture import Lecture


def buildtimetable():
    ttdata = pd.read_csv('schedule.csv').set_index('Time')
    ttdict = ttdata.to_dict()
    timetable = {}

    for day, sessions in ttdict.items():
        timetable[day] = []
        for time, info in sessions.items():
            if pd.isna(info):
                continue
            start, end = map(lambda t: datetime.datetime.strptime(
                t, '%H:%M').time(), time.split('-'))
            info = info.split(',')
            if len(info) == 2:
                subject, meetcode = info
            else:
                meetcode = info[0]
                subject = ''
            timetable[day].append(
                Lecture(start_time=start, end_time=end, subject=subject, meetcode=meetcode))

    with open("schedule.pickle", "wb") as f:
        pickle.dump(timetable, f)


buildtimetable()

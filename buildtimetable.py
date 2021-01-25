import pandas as pd
import pickle
import datetime

class Lecture:
    def __init__(self,start_time="", end_time="", subject="", meetcode=""):
        self.start_time = start_time
        self.end_time = end_time
        self.subject = subject
        self.meetcode = meetcode
    
    def setStartTime(self,start):
        self.start = start
    
    def setEndTime(self,end):
        self.end = end

    def setSubject(self,subject):
        self.subject = subject
    
    def setMeetCode(self,meetcode):
        self.meetcode = meetcode
    
    def getStartTime(self):
        return self.start
    
    def getEndTime(self):
        return self.end

    def getSubject(self):
        return self.subject
    
    def getMeetCode(self):
        return self.meetcode

ttdata = pd.read_csv('timetable.csv').set_index('Time')
ttdict = ttdata.to_dict()
timetable = {}

for day,sessions in ttdict.items():
    timetable[day] = []
    for time,info in sessions.items():
        if pd.isna(info):
            continue
        start, end = map(lambda t : datetime.datetime.strptime(t, '%H:%M').time() ,time.split('-'))
        info = info.split(',')
        if len(info) == 2:
            subject, meetcode = info
        else:
            meetcode = info[0]
            subject = ''
        timetable[day].append(Lecture(start_time=start, end_time=end, subject=subject, meetcode=meetcode))
    
 
with open("timetable.pickle","wb") as f:
    pickle.dump(timetable,f)
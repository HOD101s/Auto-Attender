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
#roger robinson

import random
import queue
names = ["joe", "bobby", "suesan", "loretta", "grant", \
         "jenny", "billy", "tucker", "cletus", "hunter", \
         "gunner", "rose", "amy", "charlotte", "duke", \
         "ricky", "bo", "duke", "jesse"]

waitingRoom = []

triageRoom = []


examRoom = []
examRoomSize = 6
doctors = 6



def callNurse():
    """move patient from waiting room to triage room"""
    triageRoom.append(waitingRoom.pop(0))
    sort(triageRoom, key = patient.triageRoom)

class Patient:
    time = 0
    def __init__(self, time):
        self.triageNumber = random.randint(0, 100)
        #self.name = names(random.randint(0, len(names)-1)) \
                          #+ names(random.randint(0, len(names)))
        self.arrivalTime = time
        self.treatmentTime = random.randrange(15, 20)
    def leave(self):
        examRoom.pop(0)
    def getExTime():
        self.enTime = time
        return self.enTime
    def getEnTime():
        self.exTime = time
        return self.exTime

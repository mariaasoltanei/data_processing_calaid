import pymongo
from datetime import datetime
def millisToHour(millis):
    return (millis/(1000*60*60))%24

def millisToMins(millis):
    return (millis/(1000*60))%60

def calculateMETSWalking(speedPerMin):
    return 0.0272 * speedPerMin + 1.2

def calculateCalories(duration, mets, userWeight):
    return 1.05 * mets * duration * userWeight

#MAKE FUNCTION TO USE INSIDE SERVER
# def getNoCalories():
uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb)
db = client['calaid_android']
stepCountDataCollection = db['StepCount']
userCollection = db['User']
userWeight = 70
userHeight = 170
strideLengthMeters = 0.415 * userHeight * 0.01
print("Stride Length", strideLengthMeters)
timestamps = []
noSteps = []
for document in stepCountDataCollection.find():
    noSteps.append(int(document['noSteps']))
for document in stepCountDataCollection.find({}):
    timestamps.append(document["timestamp"])

activityDurationMins = (max(timestamps) - min(timestamps)).total_seconds() / 60.0
activityDurationHours = (max(timestamps) - min(timestamps)).total_seconds() / 3600.0
print("Hours", activityDurationHours)
print("Minutes", activityDurationMins) 
stepFrequnecy = (max(noSteps) - min(noSteps))/activityDurationMins #steps per minute
print("Step Frequency", stepFrequnecy)
speed = strideLengthMeters * stepFrequnecy #m/min
print("Speed", speed)
mets = calculateMETSWalking(speed)
calories = calculateCalories(activityDurationHours,mets, userWeight)
print("METS",mets)
print("Calories", calories)

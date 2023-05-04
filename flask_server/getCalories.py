import pymongo
from datetime import datetime
import certifi
import pandas as pd
import time
ca = certifi.where()

def millisToHour(millis):
    return (millis/(1000*60*60))%24

def millisToMins(millis):
    return (millis/(1000*60))%60

def calculateMETSWalking(speedPerMin):
    return 0.0272 * speedPerMin + 1.2

def calculateCalories(duration, mets, userWeight):
    return 1.05 * mets * duration * userWeight

def getActivityDetails(mongoUserId, noSteps):
    uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
    client = pymongo.MongoClient(uriMongodb, tlsCAFile=ca)
    db = client['calaid_android']
    stepCountDataCollection = db['StepCount']
    userCollection = db['User']
    user = userCollection.find_one({"mongoUserId": mongoUserId})
    userWeight = float(user["weight"])
    userHeight = user["height"]
    strideLengthMeters = 0.415 * int(userHeight) * 0.01
    timestamps = []
    noSteps = []
    listStepData = list(stepCountDataCollection.find({ "userId": mongoUserId, "noSteps": { "$gte" : noSteps}})) #
    if(len(listStepData) != 0):
        dfStepData = pd.DataFrame(listStepData)
        dfStepData = dfStepData.sort_values('timestamp')

        activityDurationMins = (max(dfStepData['timestamp']) - min(dfStepData['timestamp'])).total_seconds() / 60
        activityDurationHours = (max(dfStepData['timestamp']) - min(dfStepData['timestamp'])).total_seconds() / 3600.0

        stepFrequnecy = (max(dfStepData['noSteps']) - min(dfStepData['noSteps']))/activityDurationMins #steps per minute

        speed = strideLengthMeters * stepFrequnecy #m/min

        mets = calculateMETSWalking(speed)
        calories = "{:.2f}".format(calculateCalories(activityDurationHours, mets, userWeight))
        return calories, speed, "{:.2f}".format(activityDurationMins)
    else:
        time.sleep(5)


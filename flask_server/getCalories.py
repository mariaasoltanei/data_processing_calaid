import pymongo
import os
from datetime import datetime, timedelta
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

def getActivityDetails(mongoUserId, currentTimestamp):
    print("Current", currentTimestamp)
    dt = datetime.strptime(currentTimestamp, '%Y-%m-%d %H:%M:%S.%f')
    dtMongo = dt - timedelta(hours=3)
    print("Dt mongo", type(dtMongo))
    print("Mongo",dtMongo)
    dtFiveSec = dtMongo - timedelta(seconds=150) #cu cat inainte au fost gasitit pasii
    print("3 sec",dtFiveSec)
    uriMongodb = os.getenv('uriMongodb')
    client = pymongo.MongoClient(uriMongodb, tlsCAFile=ca)
    db = client['calaid_android']
    stepCountDataCollection = db['StepCount']
    userCollection = db['User']
    user = userCollection.find_one({"mongoUserId": mongoUserId})
    userWeight = float(user["weight"])
    userHeight = user["height"]
    strideLengthMeters = 0.415 * int(userHeight) * 0.01

    #TODO take steps in the las 10 seconds 2023-05-04T16:27:51.050+00:00
    #, "timestamp":{"$gte": dtFiveSec, "$lte": dtMongo}
    listStepData = list(stepCountDataCollection.find({ "userId": mongoUserId, "timestamp":{"$gte": dtFiveSec, "$lte": dtMongo} }))
    print(len(listStepData))
    if(len(listStepData) > 1):
        dfStepData = pd.DataFrame(listStepData)
        
        dfStepData = dfStepData.sort_values('timestamp')
        # print(dfStepData)

        activityDurationMins = (max(dfStepData['timestamp']) - min(dfStepData['timestamp'])).total_seconds() / 60
        activityDurationHours = (max(dfStepData['timestamp']) - min(dfStepData['timestamp'])).total_seconds() / 3600.0
        print(activityDurationHours)

        stepFrequnecy = (max(dfStepData['noSteps']) - min(dfStepData['noSteps']))/activityDurationMins #steps per minute

        speed = strideLengthMeters * stepFrequnecy #m/min

        mets = calculateMETSWalking(speed)
        calories = "{:.2f}".format(calculateCalories(activityDurationHours, mets, userWeight))
        print("Calories", calories)
        print("Speed", speed)
        return calories, speed
    else:
        return 0, 0




import pymongo
from datetime import datetime, timedelta
import certifi
from app import mongo
import pandas as pd
ca = certifi.where()

def millisToHour(millis):
    return (millis/(1000*60*60))%24

def millisToMins(millis):
    return (millis/(1000*60))%60

def calculateMETSWalking(speedPerMin):
    return 0.0272 * speedPerMin + 1.2

def calculateCalories(duration, mets, userWeight):
    return 1.05 * mets * duration * userWeight


uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb, tlsCAFile=ca)
db = client['calaid_android']
stepCountDataCollection = db['StepCount']
accelerometerDataCollection = db['AccelerometerData']
# accelerometerDataCollection.delete_many({ "userId": "6414e7b4911b2b5943024071" })
userCollection = db['User']
user = userCollection.find_one({"mongoUserId": "6414e7b4911b2b5943024071"})
userWeight = float(user["weight"])
userHeight = user["height"]
strideLengthMeters = 0.415 * int(userHeight) * 0.01
print("Stride Length", strideLengthMeters)
timestamps = []
noSteps = []
timestamp_str = "2023-05-06 22:54:34.649000" #la ora 19 in mongo e 16
dt = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
dt_minus_3_hours = dt - timedelta(hours=3)
three_seconds_ago = dt_minus_3_hours - timedelta(seconds=5)
print(three_seconds_ago)
# print(dt_minus_3_hours)
# print(type(dt_minus_3_hours))

listStepData = list(stepCountDataCollection.find({ "userId": "6414e7b4911b2b5943024071" , "timestamp":{"$gte": three_seconds_ago, "$lte": dt_minus_3_hours}}))
print(len(listStepData))
dfStepData = pd.DataFrame(listStepData)
dfStepData = dfStepData.sort_values('timestamp')
print(dfStepData)

print(max(dfStepData['timestamp']))
activityDurationMins = (max(dfStepData['timestamp']) - min(dfStepData['timestamp'])).total_seconds() / 60
activityDurationHours = (max(dfStepData['timestamp']) - min(dfStepData['timestamp'])).total_seconds() / 3600.0

print(activityDurationMins)
stepFrequnecy = (max(dfStepData['noSteps']) - min(dfStepData['noSteps']))/activityDurationMins #steps per minute
print("Step Frequency", stepFrequnecy)
speed = strideLengthMeters * stepFrequnecy #m/min
print(speed)
mets = calculateMETSWalking(speed)
calories = "{:.2f}".format(calculateCalories(activityDurationHours, mets, userWeight))
print("METS",mets)
print("Calories", calories)
# stepCountDataCollection.delete_many({ "userId": "6414e7b4911b2b5943024071" })


# for document in stepCountDataCollection.find({ "userId": "6414e7b4911b2b5943024071", "noSteps": {"$lt":145} }):
#     noSteps.append(int(document['noSteps']))
#     print(int(document['noSteps']))
# for document in stepCountDataCollection.find({}):
#     timestamps.append(document["timestamp"])

# activityDurationMins = (max(timestamps) - min(timestamps)).total_seconds() / 60.0
# activityDurationHours = (max(timestamps) - min(timestamps)).total_seconds() / 3600.0
# # print("Hours", activityDurationHours)
# # print("Minutes", activityDurationMins) 
# stepFrequnecy = (max(noSteps) - min(noSteps))/activityDurationMins #steps per minute
# # 
# speed = strideLengthMeters * stepFrequnecy #m/min
# # print("Speed", speed)
# mets = calculateMETSWalking(speed)
# calories = calculateCalories(activityDurationHours,mets, userWeight)
# print("METS",mets)
# print("Calories", calories)

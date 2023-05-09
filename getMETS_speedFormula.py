import math
import pymongo
import statistics
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

def millisToHour(millis):
    return (millis/(1000*60*60))%24

def millisToMins(millis):
    return (millis/(1000*60))%60

def calculateMETSWalking(speedPerMin):
    return 0.0272 * speedPerMin + 1.2

def calculateMETSRunning(speedPerMin):
    0.093 * speedPerMin - 4.7

def calculateCalories(duration, mets, userWeight):
    return 1.05 * mets * duration * userWeight

def calculateSpeed(accelerometerData, lastRecordedTimestamp):
    vx, vy, vz = 0, 0, 0  
    for document in accelerometerData:
        ax, ay, az = document['x'], document['y'], document['z']
        t = int(document['timestamp'].timestamp())
    
        if lastRecordedTimestamp is not None:
            dt = (t - lastRecordedTimestamp) / 1000  
            vx += ax * dt
            vy += ay * dt
            vz += az * dt

        lastRecordedTimestamp = t

    return math.sqrt(vx**2 + vy**2 + vz**2)*60
    
uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb)
db = client['calaid_android']
accelerometerDataCollection = db['AccelerometerData']
userCollection = db['User']
user = userCollection.find_one({"mongoUserId": "6414e7b4911b2b5943024071"})
userWeight = float(user["weight"])
userHeight = user["height"]

timestamps = []
for document in accelerometerDataCollection.find({"userId": "6414e7b4911b2b5943024071"}):
    # for key in document:
    # timestamps.append(int(document["timestamp"].timestamp()))
    timestamps.append(document["timestamp"])

activityDurationHours = (max(timestamps) - min(timestamps)).total_seconds() / 3600.0
speed = calculateSpeed(accelerometerDataCollection.find({"userId": "6414e7b4911b2b5943024071"}), max(timestamps).timestamp())
print("Hours", activityDurationHours)
mets = calculateMETSWalking(speed)

caloriesBurned = calculateCalories(activityDurationHours, mets, userWeight)

print("Activity duration", activityDurationHours, "hours")
print(f"Speed: {speed:.2f} m/min")
print(f"METS: {mets:.2f}")
print(f"Calories burned: {caloriesBurned:.2f} calories")

# listAccelerometerData = list(accelerometerDataCollection.find({ "userId": "6414e7b4911b2b5943024071"}))
# dfAccData = pd.DataFrame(listAccelerometerData)
# dfAccData = dfAccData.sort_values('timestamp')
# print((dfAccData['x'].values))
# print((max(dfAccData['timestamp']) - min(dfAccData['timestamp'])).total_seconds()/60)

# activityDurationMins = (max(dfAccData['timestamp']) - min(dfAccData['timestamp'])).total_seconds() / 60
# activityDurationHours = (max(dfAccData['timestamp']) - min(dfAccData['timestamp'])).total_seconds() / 3600.0
# print(activityDurationMins)
# speed = calculateSpeed2(dfAccData)
# print(speed)





# # dt = datetime.strptime("21:52:52.742000", '%Y-%m-%d %H:%M:%S.%f')
# # dtMongo = dt - timedelta(hours=3)
# # print("Dt mongo", type(dtMongo))
# # print("Mongo",dtMongo)
# # dtFiveSec = dtMongo - timedelta(seconds=20) #poate merge mai putin
# timestamps = []
# for document in accelerometerDataCollection.find({"userId": {"$eq":"644fd0ad89a2bee6f0d565dd"}}):
#     print(document['timestamp'].timestamp())
#     timestamps.append(document["timestamp"])

# activityDurationHours = (max(timestamps) - min(timestamps)).total_seconds() / 3600.0
# speed = calculateSpeed(accelerometerDataCollection.find(), max(timestamps).timestamp())
# print("Hours", activityDurationHours)
# mets = calculateMETSWalking(speed)

# caloriesBurned = calculateCalories(activityDurationHours, mets, userWeight)

# print("Activity duration", activityDurationHours, "hours")
# print(f"Speed: {speed:.2f} m/min")
# print(f"METS: {mets:.2f}")
# print(f"Calories burned: {caloriesBurned:.2f} calories")

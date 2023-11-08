import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import pymongo
import certifi
ca = certifi.where()

def getTDEETest(currentTimestamp, userId, currentBMR):
    dtMongoStart = datetime.strptime(currentTimestamp, '%Y-%m-%d %H:%M:%S.%f') #- timedelta(hours=3)
    dtMongoEnd = dtMongoStart + timedelta(days=7) 
    uriMongodb = os.getenv('uriMongodb')
    client = pymongo.MongoClient(uriMongodb, tlsCAFile=ca)
    db = client['calaid_android']
    activityDataCollection = db['ActivityData']
    listActivityData = list(activityDataCollection.find({ "userId": userId ,"startTimestamp":{"$gte": dtMongoStart, "$lte": dtMongoEnd }}))#
    dfActivityData = pd.DataFrame(listActivityData)
    dfActivityData = dfActivityData.sort_values('startTimestamp')
    sumCalories = dfActivityData['caloriesBurned'].sum()
    avgCalories = sumCalories / 7
    print("Avg", avgCalories)
    tdee = currentBMR + avgCalories
    return tdee/currentBMR


# print(getTDEETest("2023-05-21 01:41:30.733000", "6414e7b4911b2b5943024071", 1660))

def getTDEE(currentTimestamp, userId, currentBMR):
    dtMongoStart = datetime.strptime(currentTimestamp, '%Y-%m-%d %H:%M:%S.%f') - timedelta(hours=3)
    dtMongoEnd = dtMongoStart - timedelta(days=7) 
    uriMongodb = os.getenv('uriMongodb')
    client = pymongo.MongoClient(uriMongodb, tlsCAFile=ca)
    db = client['calaid_android']
    activityDataCollection = db['ActivityData']
    listActivityData = list(activityDataCollection.find({ "userId": userId ,"startTimestamp":{"$gte": dtMongoEnd, "$lte": dtMongoStart }}))#
    dfActivityData = pd.DataFrame(listActivityData)
    dfActivityData = dfActivityData.sort_values('startTimestamp')
    sumCalories = dfActivityData['caloriesBurned'].sum()
    avgCalories = sumCalories / 7
    print("Avg", avgCalories)
    tdee = currentBMR + avgCalories
    return round(tdee/currentBMR, 2)


def addActivityMultiplierDB(userId, activityMultiplier):
    uriMongodb = os.getenv('uriMongodb')
    client = pymongo.MongoClient(uriMongodb, tlsCAFile=ca)
    db = client['calaid_android']
    userDataCollection = db['User']
    findUser = { "mongoUserId": userId }
    newActivityMultiplier = { "$set": { "activityMultiplier": activityMultiplier } }
    userDataCollection.update_one(findUser, newActivityMultiplier)

# activityMultiplier = getTDEE("2023-05-28 03:41:30.733000", "6414e7b4911b2b5943024071", 1660)
# addActivityMultiplierDB("64542741880a6eeeee57825b", activityMultiplier)
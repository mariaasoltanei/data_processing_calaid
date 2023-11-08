import random
from datetime import datetime, timedelta
import pymongo
import pandas as pd
import certifi
import os
ca = certifi.where()
from getActivity import prepareData, getActivity,calculateCalories, addToDatabase
from scipy import interpolate

activity_types = ['SITTING', 'WALKING', 'WALKING_DOWNSTAIRS', 'WALKING_UPSTAIRS', 'LAYING', 'STANDING']

data = []
activity_types = {
    'SITTING': 1.2,
    'WALKING': 3.5,
    'WALKING_DOWNSTAIRS': 4.0,
    'WALKING_UPSTAIRS': 5.0,
    'LAYING': 1.0,
    'STANDING': 1.5,
}
#2023-05-21 01:41:30.733000
start_timestamp = datetime(2023, 5, 20, 1, 41, 30, 733000)
for _ in range(2400):
    
    end_timestamp = start_timestamp + timedelta(milliseconds=300000)
    activity_type = random.choice(list(activity_types.keys()))
    calories_burned = activity_types[activity_type]
    data.append({
        'startTimestamp': start_timestamp,
        'endTimestamp': end_timestamp,
        'userId': '6414e7b4911b2b5943024071',
        'activityType': activity_type,
        'caloriesBurned': calories_burned
    })
    start_timestamp = end_timestamp

print(data)

uriMongodb = os.getenv('uriMongodb')
client = pymongo.MongoClient(uriMongodb, tlsCAFile=ca)
db = client['calaid_android']
activityDataCollection = db['ActivityData']
activityDataCollection.insert_many(data)




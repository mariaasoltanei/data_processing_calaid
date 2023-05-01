from math import sqrt
import pymongo

def calculate_walking_speed(accelerometerData, lastRecordedTimestamp):
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

    return sqrt(vx**2 + vy**2 + vz**2)

uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb)
db = client['calaid_android']
accelerometerDataCollection = db['AccelerometerData']
userCollection = db['User']
timestamps = []
for document in accelerometerDataCollection.find({}):
    for key in document:
        timestamps.append(int(document["timestamp"].timestamp()))
walking_speed = calculate_walking_speed(accelerometerDataCollection.find(), max(timestamps) )

print("Walking speed:", walking_speed)
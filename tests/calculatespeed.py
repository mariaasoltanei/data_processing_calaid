from math import sqrt
import pymongo

def calculate_walking_speed(data):
    v_x, v_y, v_z = 0, 0, 0  
    last_t = None 
    for point in data:
        a_x, a_y, a_z = point['x'], point['y'], point['z']
        t = point['timestamp'].timestamp()
        
        if last_t is not None:
            dt = (t - last_t) / 1000  
            
            v_x += a_x * dt
            v_y += a_y * dt
            v_z += a_z * dt

        last_t = t

    return sqrt(v_x**2 + v_y**2 + v_z**2)

uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb)
db = client['calaid_android']
accelerometerDataCollection = db['AccelerometerData']
userCollection = db['User']
walking_speed = calculate_walking_speed(accelerometerDataCollection.find())

print("Walking speed:", walking_speed)
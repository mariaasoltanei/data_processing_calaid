import pymongo
import pandas as pd
import numpy as np
import math
from scipy.stats import median_abs_deviation, entropy
from phase1.processingFunctions import filterAcceleration, findFFT, maxInds, findMagnitudeGravity,findMagnitudeBodyJerk, findBodyJerk, findSMAMagnitude, findMagnitudeBody, filterGravity, findSMA, findEnergy, findQuantile, findEntropy, findArCoeff
from phase1.testDict import testDataDict
from scipy.fft import fft, fftfreq

def findWindowJerk(df):
    vx = np.gradient(df['xBody'].values, df['timestamp_ms'])
    # vy = np.gradient(df['yBody'].values, df['timestamp_ms'])
    # vz = np.gradient(df['zBody'].values, df['timestamp_ms'])

    #  second derivative of the accelerometer data
    ax = np.gradient(vx, df['timestamp_ms'])
    # ay = np.gradient(vy, df['timestamp_ms'])
    # az = np.gradient(vz, df['timestamp_ms'])

    # third derivative (jerk) of the accelerometer data
    jerkx = np.gradient(ax, df['timestamp_ms'])
    # jerky = np.gradient(ay, df['timestamp_ms'])
    # jerkz = np.gradient(az, df['timestamp_ms'])

    return jerkx

uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb)
db = client['calaid_android']
accelerometerDataCollection = db['AccelerometerData']

listAccData = list(accelerometerDataCollection.find({ "userId": "6414e7b4911b2b5943024071" }))
print(len(listAccData))
dfAccData = pd.DataFrame(listAccData)
print(dfAccData['timestamp'])
dfAccData['timestamp'] = pd.to_datetime(dfAccData['timestamp'])
dfAccData['timestamp_ms'] = dfAccData['timestamp'].apply(lambda x: int(x.timestamp() * 1000))

dfAccData = dfAccData.sort_values('timestamp')
dfAccData['xBody'] = filterAcceleration(dfAccData['x'])
dfAccData['yBody'] = filterAcceleration(dfAccData['y'])
dfAccData['zBody'] = filterAcceleration(dfAccData['z'])

dfAccData['xGravity'] = filterGravity(dfAccData['x'])
dfAccData['yGravity'] = filterGravity(dfAccData['y'])
dfAccData['zGravity'] = filterGravity(dfAccData['z'])

window_length = 128
overlap_pct = 0.5
shift = int(window_length * overlap_pct)
print("Mean overall",findWindowJerk(dfAccData).mean())
windowed_data = []
for i in range(0, len(dfAccData) - window_length, shift):
    window = dfAccData.iloc[i:i+window_length]
    print((findWindowJerk(window)).mean())
    windowed_data.append(window)

windowed_df = pd.concat(windowed_data, ignore_index=True)

# x = dfAccData['xBody']
# t = dfAccData['timestamp']
# print(x.values)
# dfAccData['xBodyJerk'], dfAccData['yBodyJerk'], dfAccData['zBodyJerk'] = findBodyJerk(dfAccData)
# dfAccData['bodyMagnitude'] = findMagnitudeBody(dfAccData)
# dfAccData['gravityMagnitude'] = findMagnitudeGravity(dfAccData)
# dfAccData['bodyMagnitudeJerk'] = findMagnitudeBodyJerk(dfAccData)





# Calculate the first derivative (velocity) of the accelerometer data
# vx = np.gradient(dfAccData['xBody'], dfAccData['timestamp'])
# vy = np.gradient(dfAccData['yBody'], dfAccData['timestamp'])
# vz = np.gradient(dfAccData['zBody'], dfAccData['timestamp'])

# # Calculate the second derivative (acceleration) of the accelerometer data
# ax = np.gradient(vx, dfAccData['timestamp'])
# ay = np.gradient(vy, dfAccData['timestamp'])
# az = np.gradient(vz, dfAccData['timestamp'])

# # Calculate the third derivative (jerk) of the accelerometer data
# dfAccData['jerk_x'] = np.gradient(ax, dfAccData['timestamp'])
# dfAccData['jerk_y'] = np.gradient(ay, dfAccData['timestamp'])
# dfAccData['jerk_z'] = np.gradient(az, dfAccData['timestamp'])

# print(dfAccData['jerk_x'])


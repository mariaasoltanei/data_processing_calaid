import pymongo
import pandas as pd
import numpy as np
import math
from scipy.stats import median_abs_deviation, entropy
from processingFunctions import filterAcceleration, findFFT, maxInds, findMagnitudeGravity,findMagnitudeBodyJerk, findBodyJerk, findSMAMagnitude, findMagnitudeBody, filterGravity, findSMA, findEnergy, findQuantile, findEntropy, findArCoeff
from testDict import testDataDict
from scipy.fft import fft, fftfreq

uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb)
db = client['calaid_android']
accelerometerDataCollection = db['AccelerometerData']

listAccData = list(accelerometerDataCollection.find({ "userId": "6414e7b4911b2b5943024071" }))
print(len(listAccData))
dfAccData = pd.DataFrame(listAccData)

dfAccData = dfAccData.sort_values('timestamp')


window_length = 128
overlap_pct = 0.5
shift = int(window_length * overlap_pct)

windowed_data = []

for i in range(0, len(dfAccData) - window_length, shift):
    window = dfAccData.iloc[i:i+window_length]
    xBody = filterAcceleration(window['x'])
    yBody = filterAcceleration(window['y'])
    zBody = filterAcceleration(window['z'])
    print(xBody)
    print(np.abs(fft(xBody)))
    windowed_data.append(window)

windowed_df = pd.concat(windowed_data, ignore_index=True)
# print(testDataDict)
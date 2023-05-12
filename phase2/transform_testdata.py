import pymongo
import pandas as pd
import numpy as np
import math
from scipy.stats import median_abs_deviation, entropy
from processingFunctions import filterAcceleration, findFFT, maxInds, findMagnitudeGravity,findMagnitudeBodyJerk, findBodyJerk, findSMAMagnitude, findMagnitudeBody, filterGravity, findSMA, findEnergy, findQuantile, findEntropy, findArCoeff
from scipy.fft import fft

uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb)
db = client['calaid_android']
accelerometerDataCollection = db['AccelerometerData']

listAccData = list(accelerometerDataCollection.find({ "userId": "645e41cab22e8213021b5467" }))
print(len(listAccData))
dfAccData = pd.DataFrame(listAccData)

dfAccData = dfAccData.sort_values('timestamp')
dfAccData['xBody'] = filterAcceleration(dfAccData['x'])
dfAccData['yBody'] = filterAcceleration(dfAccData['y'])
dfAccData['zBody'] = filterAcceleration(dfAccData['z'])

testDataDict = {
    'body_acc_x_mean': [],
    'body_acc_y_mean': [],
    'body_acc_z_mean': [],
    'body_acc_x_std': [],
    'body_acc_y_std': [],
    'body_acc_z_std': []#,

    # 'body_gyro_x_mean': [],
    # 'body_gyro_y_mean': [],
    # 'body_gyro_z_mean': [],
    # 'body_gyro_x_std': [],
    # 'body_gyro_y_std': [],
    # 'body_gyro_z_std': []#,

    # 'total_acc_x_mean': [],
    # 'total_acc_y_mean': [],
    # 'total_acc_z_mean': [],
    # 'total_acc_x_std': [],
    # 'total_acc_y_std': [],
    # 'total_acc_z_std': []
}
window_length = 128
overlap_pct = 0.5
shift = int(window_length * overlap_pct)

windowed_data = []
#raport activitate pe zi 
for i in range(0, len(dfAccData) - window_length, shift):
    window = dfAccData.iloc[i:i+window_length]
    testDataDict['body_acc_x_mean'].append(np.mean(window['xBody']))
    testDataDict['body_acc_y_mean'].append(np.mean(window['yBody']))
    testDataDict['body_acc_z_mean'].append(np.mean(window['zBody']))
    testDataDict['body_acc_x_std'].append(np.std(window['xBody']))
    testDataDict['body_acc_y_std'].append(np.std(window['yBody']))
    testDataDict['body_acc_z_std'].append(np.std(window['zBody']))
    print(np.mean(window['xBody']))

testDataDF = pd.DataFrame(testDataDict)
testDataDF.to_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/data_processing_calaid/phase2/test_real.csv', encoding='utf-8', index=False)
print(testDataDF)
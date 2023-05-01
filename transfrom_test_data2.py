import pymongo
import pandas as pd
import numpy as np
import math
from scipy.stats import median_abs_deviation, entropy
from processingFunctions import filterAcceleration, findJerk,filterGravity, findSMA, findEnergy, findQuantile, findEntropy, findArCoeff
from testDict import testDataDict

uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb)
db = client['calaid_android']
accelerometerDataCollection = db['AccelerometerData']

listAccData = list(accelerometerDataCollection.find({ "userId": "6414e7b4911b2b5943024071" }))
print(len(listAccData))
dfAccData = pd.DataFrame(listAccData)

dfAccData = dfAccData.sort_values('timestamp')
dfAccData['xBody'] = filterAcceleration(dfAccData['x'])
dfAccData['yBody'] = filterAcceleration(dfAccData['y'])
dfAccData['zBody'] = filterAcceleration(dfAccData['z'])

dfAccData['xGravity'] = filterGravity(dfAccData['x'])
dfAccData['yGravity'] = filterGravity(dfAccData['y'])
dfAccData['zGravity'] = filterGravity(dfAccData['z'])

# dfAccData['xJerk'], dfAccData['yJerk'], dfAccData['zJerk'] = findJerk(dfAccData)
dfAccData.to_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/modeled_csv/test2.csv', encoding='utf-8', index=False)

window_length = 128
overlap_pct = 0.5
shift = int(window_length * overlap_pct)

windowed_data = []

for i in range(0, len(dfAccData) - window_length, shift):
    window = dfAccData.iloc[i:i+window_length]
    testDataDict['tBodyAcc-mean()-X'].append(window['xBody'].mean())
    testDataDict['tBodyAcc-mean()-Y'].append(window['yBody'].mean())
    testDataDict['tBodyAcc-mean()-Z'].append((window['zBody']).mean())

    testDataDict['tBodyAcc-std()-X'].append((window['xBody']).std())
    testDataDict['tBodyAcc-std()-Y'].append((window['yBody']).std())
    testDataDict['tBodyAcc-std()-Z'].append((window['zBody']).std())

    testDataDict['tBodyAcc-mad()-X'].append(median_abs_deviation((window['xBody'])))
    testDataDict['tBodyAcc-mad()-Y'].append(median_abs_deviation((window['yBody'])))
    testDataDict['tBodyAcc-mad()-Z'].append(median_abs_deviation((window['zBody'])))
    
    testDataDict['tBodyAcc-max()-X'].append(max((window['xBody'])))
    testDataDict['tBodyAcc-max()-Y'].append(max((window['yBody'])))
    testDataDict['tBodyAcc-max()-Z'].append(max((window['zBody'])))

    testDataDict['tBodyAcc-min()-X'].append(min((window['xBody'])))
    testDataDict['tBodyAcc-min()-Y'].append(min((window['yBody'])))
    testDataDict['tBodyAcc-min()-Z'].append(min((window['zBody'])))

    testDataDict['tBodyAcc-sma()'].append(findSMA((window['xBody']), (window['yBody']), (window['zBody'])))

    testDataDict['tBodyAcc-energy()-X'].append(findEnergy((window['xBody'])))
    testDataDict['tBodyAcc-energy()-Y'].append(findEnergy((window['yBody'])))
    testDataDict['tBodyAcc-energy()-Z'].append(findEnergy((window['zBody'])))

    testDataDict['tBodyAcc-iqr()-X'].append(findQuantile((window['xBody'])))
    testDataDict['tBodyAcc-iqr()-Y'].append(findQuantile((window['yBody'])))
    testDataDict['tBodyAcc-iqr()-Z'].append(findQuantile((window['zBody'])))

    testDataDict['tBodyAcc-entropy()-X'].append(findEntropy((window['xBody'])))
    testDataDict['tBodyAcc-entropy()-Y'].append(findEntropy((window['yBody'])))
    testDataDict['tBodyAcc-entropy()-Z'].append(findEntropy((window['zBody'])))

    testDataDict['tBodyAcc-arCoeff()-X,1'].append(findArCoeff((window['xBody']),4)[0])
    testDataDict['tBodyAcc-arCoeff()-X,2'].append(findArCoeff((window['xBody']),4)[1])
    testDataDict['tBodyAcc-arCoeff()-X,3'].append(findArCoeff((window['xBody']),4)[2])
    testDataDict['tBodyAcc-arCoeff()-X,4'].append(findArCoeff((window['xBody']),4)[3])

    testDataDict['tBodyAcc-arCoeff()-Y,1'].append(findArCoeff((window['yBody']),4)[0])
    testDataDict['tBodyAcc-arCoeff()-Y,2'].append(findArCoeff((window['yBody']),4)[1])
    testDataDict['tBodyAcc-arCoeff()-Y,3'].append(findArCoeff((window['yBody']),4)[2])
    testDataDict['tBodyAcc-arCoeff()-Y,4'].append(findArCoeff((window['yBody']),4)[3])

    testDataDict['tBodyAcc-arCoeff()-Z,1'].append(findArCoeff((window['zBody']),4)[0])
    testDataDict['tBodyAcc-arCoeff()-Z,2'].append(findArCoeff((window['zBody']),4)[1])
    testDataDict['tBodyAcc-arCoeff()-Z,3'].append(findArCoeff((window['zBody']),4)[2])
    testDataDict['tBodyAcc-arCoeff()-Z,4'].append(findArCoeff((window['zBody']),4)[3])

    testDataDict['tBodyAcc-correlation()-X,Y'].append(window['xBody'].corr(window['yBody']))
    testDataDict['tBodyAcc-correlation()-X,Z'].append(window['xBody'].corr(window['zBody']))
    testDataDict['tBodyAcc-correlation()-Y,Z'].append(window['yBody'].corr(window['zBody']))


    testDataDict['tGravityAcc-mean()-X'].append(window['xGravity'].mean())
    testDataDict['tGravityAcc-mean()-Y'].append(window['yGravity'].mean())
    testDataDict['tGravityAcc-mean()-Z'].append((window['zGravity']).mean())

    testDataDict['tGravityAcc-std()-X'].append((window['xGravity']).std())
    testDataDict['tGravityAcc-std()-Y'].append((window['yGravity']).std())
    testDataDict['tGravityAcc-std()-Z'].append((window['zGravity']).std())

    testDataDict['tGravityAcc-mad()-X'].append(median_abs_deviation((window['xGravity'])))
    testDataDict['tGravityAcc-mad()-Y'].append(median_abs_deviation((window['yGravity'])))
    testDataDict['tGravityAcc-mad()-Z'].append(median_abs_deviation((window['zGravity'])))
    
    testDataDict['tGravityAcc-max()-X'].append(max((window['xGravity'])))
    testDataDict['tGravityAcc-max()-Y'].append(max((window['yGravity'])))
    testDataDict['tGravityAcc-max()-Z'].append(max((window['zGravity'])))

    testDataDict['tGravityAcc-min()-X'].append(min((window['xGravity'])))
    testDataDict['tGravityAcc-min()-Y'].append(min((window['yGravity'])))
    testDataDict['tGravityAcc-min()-Z'].append(min((window['zGravity'])))

    testDataDict['tGravityAcc-sma()'].append(findSMA((window['xGravity']), (window['yGravity']), (window['zGravity'])))

    testDataDict['tGravityAcc-energy()-X'].append(findEnergy((window['xGravity'])))
    testDataDict['tGravityAcc-energy()-Y'].append(findEnergy((window['yGravity'])))
    testDataDict['tGravityAcc-energy()-Z'].append(findEnergy((window['zGravity'])))

    testDataDict['tGravityAcc-iqr()-X'].append(findQuantile((window['xGravity'])))
    testDataDict['tGravityAcc-iqr()-Y'].append(findQuantile((window['yGravity'])))
    testDataDict['tGravityAcc-iqr()-Z'].append(findQuantile((window['zGravity'])))

    testDataDict['tGravityAcc-entropy()-X'].append(findEntropy((window['xGravity'])))
    testDataDict['tGravityAcc-entropy()-Y'].append(findEntropy((window['yGravity'])))
    testDataDict['tGravityAcc-entropy()-Z'].append(findEntropy((window['zGravity'])))

    testDataDict['tGravityAcc-arCoeff()-X,1'].append(findArCoeff((window['xGravity']),4)[0])
    testDataDict['tGravityAcc-arCoeff()-X,2'].append(findArCoeff((window['xGravity']),4)[1])
    testDataDict['tGravityAcc-arCoeff()-X,3'].append(findArCoeff((window['xGravity']),4)[2])
    testDataDict['tGravityAcc-arCoeff()-X,4'].append(findArCoeff((window['xGravity']),4)[3])

    testDataDict['tGravityAcc-arCoeff()-Y,1'].append(findArCoeff((window['yGravity']),4)[0])
    testDataDict['tGravityAcc-arCoeff()-Y,2'].append(findArCoeff((window['yGravity']),4)[1])
    testDataDict['tGravityAcc-arCoeff()-Y,3'].append(findArCoeff((window['yGravity']),4)[2])
    testDataDict['tGravityAcc-arCoeff()-Y,4'].append(findArCoeff((window['yGravity']),4)[3])

    testDataDict['tGravityAcc-arCoeff()-Z,1'].append(findArCoeff((window['zGravity']),4)[0])
    testDataDict['tGravityAcc-arCoeff()-Z,2'].append(findArCoeff((window['zGravity']),4)[1])
    testDataDict['tGravityAcc-arCoeff()-Z,3'].append(findArCoeff((window['zGravity']),4)[2])
    testDataDict['tGravityAcc-arCoeff()-Z,4'].append(findArCoeff((window['zGravity']),4)[3])

    testDataDict['tGravityAcc-correlation()-X,Y'].append(window['xGravity'].corr(window['yGravity']))
    testDataDict['tGravityAcc-correlation()-X,Z'].append(window['xGravity'].corr(window['zGravity']))
    testDataDict['tGravityAcc-correlation()-Y,Z'].append(window['yGravity'].corr(window['zGravity']))
    

    testDataDict['tBodyAccJerk-mean()-X'].append(findJerk(window).mean())




    # testDataDict['tBodyAcc-correlation()-X,Y'].append(filterAcceleration(window['x']).corr(filterAcceleration(window['y'])))
    #findArCoeff(filterAcceleration(dfAccData['x']), 4)[0]
    # body = filterAcceleration(window['x'])
    windowed_data.append(window)

windowed_df = pd.concat(windowed_data, ignore_index=True)
# print(testDataDict)

print(len((testDataDict['tBodyAccJerk-mean()-X'])))
# print((testDataDict['tBodyAcc-arCoeff()-Y,1']))
# print((testDataDict['tBodyAcc-arCoeff()-Z,1']))
# print((testDataDict['tBodyAcc-correlation()-X,Y']))
testDataDF = pd.DataFrame(testDataDict)
print(testDataDF)
testDataDF.to_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/modeled_csv/test1.csv', encoding='utf-8', index=False)
# print(windowed_df)

import pymongo
import pandas as pd
import numpy as np
import math
from scipy.stats import median_abs_deviation, entropy
from processingFunctions import filterAcceleration, findFFT, maxInds, findMagnitudeGravity,findMagnitudeBodyJerk, findBodyJerk, findSMAMagnitude, findMagnitudeBody, filterGravity, findSMA, findEnergy, findQuantile, findEntropy, findArCoeff
from testDict import testDataDict
from scipy.fft import fft

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

dfAccData['xBodyJerk'], dfAccData['yBodyJerk'], dfAccData['zBodyJerk'] = findBodyJerk(dfAccData)
dfAccData['bodyMagnitude'] = findMagnitudeBody(dfAccData)
dfAccData['gravityMagnitude'] = findMagnitudeGravity(dfAccData)
dfAccData['bodyMagnitudeJerk'] = findMagnitudeBodyJerk(dfAccData)
dfAccData['xfBody'] = findFFT(dfAccData['xBody'])
dfAccData['yfBody'] = findFFT(dfAccData['yBody'])
dfAccData['zfBody'] = findFFT(dfAccData['zBody'])
# print(findFFT(dfAccData['xBody']))
dfAccData = dfAccData.dropna()
# print("Null vals - test", sum(dfAccData.isnull().values))

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
    
    testDataDict['tBodyAcc-max()-X'].append(max((window['xBody'].values)))
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

    testDataDict['tBodyAccJerk-mean()-X'].append(window['xBodyJerk'].mean())
    testDataDict['tBodyAccJerk-mean()-Y'].append(window['yBodyJerk'].mean())
    testDataDict['tBodyAccJerk-mean()-Z'].append(window['zBodyJerk'].mean())

    testDataDict['tBodyAccJerk-std()-X'].append((window['xBodyJerk']).std())
    testDataDict['tBodyAccJerk-std()-Y'].append((window['yBodyJerk']).std())
    testDataDict['tBodyAccJerk-std()-Z'].append((window['zBodyJerk']).std())

    testDataDict['tBodyAccJerk-mad()-X'].append(median_abs_deviation((window['xBodyJerk'])))
    testDataDict['tBodyAccJerk-mad()-Y'].append(median_abs_deviation((window['yBodyJerk'])))
    testDataDict['tBodyAccJerk-mad()-Z'].append(median_abs_deviation((window['zBodyJerk'])))
    
    testDataDict['tBodyAccJerk-max()-X'].append(max((window['xBodyJerk'])))
    testDataDict['tBodyAccJerk-max()-Y'].append(max((window['yBodyJerk'])))
    testDataDict['tBodyAccJerk-max()-Z'].append(max((window['zBodyJerk'])))

    testDataDict['tBodyAccJerk-min()-X'].append(min((window['xBodyJerk'])))
    testDataDict['tBodyAccJerk-min()-Y'].append(min((window['yBodyJerk'])))
    testDataDict['tBodyAccJerk-min()-Z'].append(min((window['zBodyJerk'])))

    testDataDict['tBodyAccJerk-sma()'].append(findSMA((window['xBodyJerk']), (window['yBodyJerk']), (window['zBodyJerk'])))

    testDataDict['tBodyAccJerk-energy()-X'].append(findEnergy((window['xBodyJerk'])))
    testDataDict['tBodyAccJerk-energy()-Y'].append(findEnergy((window['yBodyJerk'])))
    testDataDict['tBodyAccJerk-energy()-Z'].append(findEnergy((window['zBodyJerk'])))

    testDataDict['tBodyAccJerk-iqr()-X'].append(findQuantile((window['xBodyJerk'])))
    testDataDict['tBodyAccJerk-iqr()-Y'].append(findQuantile((window['yBodyJerk'])))
    testDataDict['tBodyAccJerk-iqr()-Z'].append(findQuantile((window['zBodyJerk'])))

    testDataDict['tBodyAccJerk-entropy()-X'].append(findEntropy((window['xBodyJerk'])))
    testDataDict['tBodyAccJerk-entropy()-Y'].append(findEntropy((window['yBodyJerk'])))
    testDataDict['tBodyAccJerk-entropy()-Z'].append(findEntropy((window['zBodyJerk'])))

    testDataDict['tBodyAccJerk-arCoeff()-X,1'].append(findArCoeff((window['xBodyJerk']),4)[0])
    testDataDict['tBodyAccJerk-arCoeff()-X,2'].append(findArCoeff((window['xBodyJerk']),4)[1])
    testDataDict['tBodyAccJerk-arCoeff()-X,3'].append(findArCoeff((window['xBodyJerk']),4)[2])
    testDataDict['tBodyAccJerk-arCoeff()-X,4'].append(findArCoeff((window['xBodyJerk']),4)[3])

    testDataDict['tBodyAccJerk-arCoeff()-Y,1'].append(findArCoeff((window['yBodyJerk']),4)[0])
    testDataDict['tBodyAccJerk-arCoeff()-Y,2'].append(findArCoeff((window['yBodyJerk']),4)[1])
    testDataDict['tBodyAccJerk-arCoeff()-Y,3'].append(findArCoeff((window['yBodyJerk']),4)[2])
    testDataDict['tBodyAccJerk-arCoeff()-Y,4'].append(findArCoeff((window['yBodyJerk']),4)[3])

    testDataDict['tBodyAccJerk-arCoeff()-Z,1'].append(findArCoeff((window['zBodyJerk']),4)[0])
    testDataDict['tBodyAccJerk-arCoeff()-Z,2'].append(findArCoeff((window['zBodyJerk']),4)[1])
    testDataDict['tBodyAccJerk-arCoeff()-Z,3'].append(findArCoeff((window['zBodyJerk']),4)[2])
    testDataDict['tBodyAccJerk-arCoeff()-Z,4'].append(findArCoeff((window['zBodyJerk']),4)[3])

    testDataDict['tBodyAccJerk-correlation()-X,Y'].append(window['xBodyJerk'].corr(window['yBodyJerk']))
    testDataDict['tBodyAccJerk-correlation()-X,Z'].append(window['xBodyJerk'].corr(window['zBodyJerk']))
    testDataDict['tBodyAccJerk-correlation()-Y,Z'].append(window['yBodyJerk'].corr(window['zBodyJerk']))

    testDataDict['tBodyAccMag-mean()'].append(window['bodyMagnitude'].mean())
    testDataDict['tBodyAccMag-std()'].append(window['bodyMagnitude'].std())
    testDataDict['tBodyAccMag-mad()'].append(median_abs_deviation((window['bodyMagnitude'])))
    testDataDict['tBodyAccMag-max()'].append(max((window['bodyMagnitude'])))
    testDataDict['tBodyAccMag-min()'].append(min((window['bodyMagnitude'])))
    testDataDict['tBodyAccMag-sma()'].append(findSMAMagnitude(window['bodyMagnitude']))
    testDataDict['tBodyAccMag-energy()'].append(findEnergy(window['bodyMagnitude']))
    testDataDict['tBodyAccMag-iqr()'].append(findQuantile(window['bodyMagnitude']))
    testDataDict['tBodyAccMag-entropy()'].append(findEntropy(window['bodyMagnitude']))
    testDataDict['tBodyAccMag-arCoeff()1'].append(findArCoeff((window['bodyMagnitude']),4)[0])
    testDataDict['tBodyAccMag-arCoeff()2'].append(findArCoeff((window['bodyMagnitude']),4)[1])
    testDataDict['tBodyAccMag-arCoeff()3'].append(findArCoeff((window['bodyMagnitude']),4)[2])
    testDataDict['tBodyAccMag-arCoeff()4'].append(findArCoeff((window['bodyMagnitude']),4)[3])

    testDataDict['tGravityAccMag-mean()'].append(window['gravityMagnitude'].mean())
    testDataDict['tGravityAccMag-std()'].append(window['gravityMagnitude'].std())
    testDataDict['tGravityAccMag-mad()'].append(median_abs_deviation((window['gravityMagnitude'])))
    testDataDict['tGravityAccMag-max()'].append(max((window['gravityMagnitude'])))
    testDataDict['tGravityAccMag-min()'].append(min((window['gravityMagnitude'])))
    testDataDict['tGravityAccMag-sma()'].append(findSMAMagnitude(window['gravityMagnitude']))
    testDataDict['tGravityAccMag-energy()'].append(findEnergy(window['gravityMagnitude']))
    testDataDict['tGravityAccMag-iqr()'].append(findQuantile(window['gravityMagnitude']))
    testDataDict['tGravityAccMag-entropy()'].append(findEntropy(window['gravityMagnitude']))
    testDataDict['tGravityAccMag-arCoeff()1'].append(findArCoeff((window['gravityMagnitude']),4)[0])
    testDataDict['tGravityAccMag-arCoeff()2'].append(findArCoeff((window['gravityMagnitude']),4)[1])
    testDataDict['tGravityAccMag-arCoeff()3'].append(findArCoeff((window['gravityMagnitude']),4)[2])
    testDataDict['tGravityAccMag-arCoeff()4'].append(findArCoeff((window['gravityMagnitude']),4)[3])

    testDataDict['tBodyAccJerkMag-mean()'].append(window['bodyMagnitudeJerk'].mean())
    testDataDict['tBodyAccJerkMag-std()'].append(window['bodyMagnitudeJerk'].std())
    testDataDict['tBodyAccJerkMag-mad()'].append(median_abs_deviation((window['bodyMagnitudeJerk'])))
    testDataDict['tBodyAccJerkMag-max()'].append(max((window['bodyMagnitudeJerk'])))
    testDataDict['tBodyAccJerkMag-min()'].append(min((window['bodyMagnitudeJerk'])))
    testDataDict['tBodyAccJerkMag-sma()'].append(findSMAMagnitude(window['bodyMagnitudeJerk']))
    testDataDict['tBodyAccJerkMag-energy()'].append(findEnergy(window['bodyMagnitudeJerk']))
    testDataDict['tBodyAccJerkMag-iqr()'].append(findQuantile(window['bodyMagnitudeJerk']))
    testDataDict['tBodyAccJerkMag-entropy()'].append(findEntropy(window['bodyMagnitudeJerk']))
    testDataDict['tBodyAccJerkMag-arCoeff()1'].append(findArCoeff((window['bodyMagnitudeJerk']),4)[0])
    testDataDict['tBodyAccJerkMag-arCoeff()2'].append(findArCoeff((window['bodyMagnitudeJerk']),4)[1])
    testDataDict['tBodyAccJerkMag-arCoeff()3'].append(findArCoeff((window['bodyMagnitudeJerk']),4)[2])
    testDataDict['tBodyAccJerkMag-arCoeff()4'].append(findArCoeff((window['bodyMagnitudeJerk']),4)[3])
    #FFT?
    
    # print(np.mean(np.abs(np.fft.fft(testDataDict['tBodyAcc-mean()-X']))))
    testDataDict['fBodyAcc-mean()-X'].append(np.mean(np.abs(np.fft.fft(testDataDict['tBodyAcc-mean()-X']))))
    testDataDict['fBodyAcc-mean()-Y'].append(np.mean(np.abs(np.fft.fft(testDataDict['tBodyAcc-mean()-Y']))))
    testDataDict['fBodyAcc-mean()-Z'].append(np.mean(np.abs(np.fft.fft(testDataDict['tBodyAcc-mean()-Z']))))

    testDataDict['fBodyAcc-std()-X'].append(np.std(np.abs(np.fft.fft(testDataDict['tBodyAcc-std()-X']))))
    testDataDict['fBodyAcc-std()-Y'].append(np.std(np.abs(np.fft.fft(testDataDict['tBodyAcc-std()-Y']))))
    testDataDict['fBodyAcc-std()-Z'].append(np.std(np.abs(np.fft.fft(testDataDict['tBodyAcc-std()-Z']))))

    testDataDict['fBodyAcc-mad()-X'].append(median_abs_deviation(np.abs(np.fft.fft(testDataDict['tBodyAcc-mad()-X']))))
    testDataDict['fBodyAcc-mad()-Y'].append(median_abs_deviation(np.abs(np.fft.fft(testDataDict['tBodyAcc-mad()-Y']))))
    testDataDict['fBodyAcc-mad()-Z'].append(median_abs_deviation(np.abs(np.fft.fft(testDataDict['tBodyAcc-mad()-Z']))))

    testDataDict['fBodyAcc-max()-X'].append(np.max(np.abs(np.fft.fft(testDataDict['tBodyAcc-max()-X']))))
    testDataDict['fBodyAcc-max()-Y'].append(np.max(np.abs(np.fft.fft(testDataDict['tBodyAcc-max()-Y']))))
    testDataDict['fBodyAcc-max()-Z'].append(np.max(np.abs(np.fft.fft(testDataDict['tBodyAcc-max()-Z']))))

    testDataDict['fBodyAcc-min()-X'].append(np.min(np.abs(np.fft.fft(testDataDict['tBodyAcc-min()-X']))))
    testDataDict['fBodyAcc-min()-Y'].append(np.min(np.abs(np.fft.fft(testDataDict['tBodyAcc-min()-Y']))))
    testDataDict['fBodyAcc-min()-Z'].append(np.min(np.abs(np.fft.fft(testDataDict['tBodyAcc-min()-Z']))))

    #nu cred ca trebuie mean pt urmatoarele
    testDataDict['fBodyAcc-sma()'].append(np.abs(np.fft.fft(testDataDict['tBodyAcc-sma()'])).mean())
    
    testDataDict['fBodyAcc-energy()-X'].append(np.abs(np.fft.fft(testDataDict['tBodyAcc-energy()-X'])).mean())
    testDataDict['fBodyAcc-energy()-Y'].append(np.abs(np.fft.fft(testDataDict['tBodyAcc-energy()-Y'])).mean())
    testDataDict['fBodyAcc-energy()-Z'].append(np.abs(np.fft.fft(testDataDict['tBodyAcc-energy()-Z'])).mean())

    testDataDict['fBodyAcc-iqr()-X'].append(np.abs(np.fft.fft(testDataDict['tBodyAcc-iqr()-X'])).mean())
    testDataDict['fBodyAcc-iqr()-Y'].append(np.abs(np.fft.fft(testDataDict['tBodyAcc-iqr()-Y'])).mean())
    testDataDict['fBodyAcc-iqr()-Z'].append(np.abs(np.fft.fft(testDataDict['tBodyAcc-iqr()-Z'])).mean())

    testDataDict['fBodyAcc-entropy()-X'].append(np.abs(np.fft.fft(testDataDict['tBodyAcc-entropy()-X'])).mean())
    testDataDict['fBodyAcc-entropy()-Y'].append(np.abs(np.fft.fft(testDataDict['tBodyAcc-entropy()-X'])).mean())
    testDataDict['fBodyAcc-entropy()-Z'].append(np.abs(np.fft.fft(testDataDict['tBodyAcc-entropy()-X'])).mean())

    print(np.abs(np.fft.fft(window['xBody'].values)))
    # print(np.mean(np.abs(np.fft.fft(window['xBody'].values))))

    #fft = np.fft.fft(window['xBody'])
    # power_spectrum = np.abs(fft) ** 2
    # freqs = np.fft.fftfreq(window_length, 1/50)
    # pos_freqs = freqs[:window_length//2 + 1]

    # # Sum the power spectrum over the positive frequency bins to obtain the energy of the signal
    # energy = np.sum(power_spectrum[:window_length//2 + 1])
    # print(energy)

    # testDataDict['fBodyAcc-mean()-X'].append(window['xfBody'].mean())
    # testDataDict['fBodyAcc-mean()-Y'].append(window['yfBody'].mean())
    # testDataDict['fBodyAcc-mean()-Z'].append(window['zfBody'].mean())
    # testDataDict['fBodyAcc-std()-X'].append(window['xfBody'].std())
    # testDataDict['fBodyAcc-std()-Y'].append(window['yfBody'].std())
    # testDataDict['fBodyAcc-std()-Z'].append(window['zfBody'].std())
    # testDataDict['fBodyAcc-mad()-X'].append(median_abs_deviation((window['xfBody'])))
    # testDataDict['fBodyAcc-mad()-Y'].append(median_abs_deviation((window['yfBody'])))
    # testDataDict['fBodyAcc-mad()-Z'].append(median_abs_deviation((window['zfBody'])))

    # testDataDict['fBodyAcc-max()-X'].append(max((window['xfBody'])))
    # testDataDict['fBodyAcc-max()-Y'].append(max((window['yfBody'])))
    # testDataDict['fBodyAcc-max()-Z'].append(max((window['zfBody'])))

    # testDataDict['fBodyAcc-min()-X'].append(min((window['xfBody'])))
    # testDataDict['fBodyAcc-min()-Y'].append(min((window['yfBody'])))
    # testDataDict['fBodyAcc-min()-Z'].append(min((window['zfBody'])))
    # testDataDict['fBodyAcc-sma()'].append(findSMA((window['xfBody']), (window['yfBody']), (window['zfBody'])))

    # testDataDict['fBodyAcc-energy()-X'].append(findEnergy((window['xfBody'])))
    # testDataDict['fBodyAcc-energy()-Y'].append(findEnergy((window['yfBody'])))
    # testDataDict['fBodyAcc-energy()-Z'].append(findEnergy((window['zfBody'])))

    # testDataDict['fBodyAcc-iqr()-X'].append(findQuantile((window['xfBody'])))
    # testDataDict['fBodyAcc-iqr()-Y'].append(findQuantile((window['yfBody'])))
    # testDataDict['fBodyAcc-iqr()-Z'].append(findQuantile((window['zfBody'])))

    # testDataDict['fBodyAcc-entropy()-X'].append(findEntropy((window['xfBody'])))
    # testDataDict['fBodyAcc-entropy()-Y'].append(findEntropy((window['yfBody'])))
    # testDataDict['fBodyAcc-entropy()-Z'].append(findEntropy((window['zfBody'])))

#  'fBodyAcc-maxInds-X':[], 
#     'fBodyAcc-maxInds-Y':[],
#     'fBodyAcc-maxInds-Z':[], 
#     'fBodyAcc-meanFreq()-X':[], 
#     'fBodyAcc-meanFreq()-Y':[],
#     'fBodyAcc-meanFreq()-Z':[], 
#     'fBodyAcc-skewness()-X':[], 
#     'fBodyAcc-kurtosis()-X':[],
#     'fBodyAcc-skewness()-Y':[], 
#     'fBodyAcc-kurtosis()-Y':[], 
#     'fBodyAcc-skewness()-Z':[],
#     'fBodyAcc-kurtosis()-Z':[], 
#     'fBodyAcc-bandsEnergy()-1,8':[], 
#     'fBodyAcc-bandsEnergy()-9,16':[],
#     'fBodyAcc-bandsEnergy()-17,24':[], 
#     'fBodyAcc-bandsEnergy()-25,32':[], 
#     'fBodyAcc-bandsEnergy()-33,40':[],
#     'fBodyAcc-bandsEnergy()-41,48':[], 
#     'fBodyAcc-bandsEnergy()-49,56':[], 
#     'fBodyAcc-bandsEnergy()-57,64':[],
#     'fBodyAcc-bandsEnergy()-1,16':[], 
#     'fBodyAcc-bandsEnergy()-17,32':[], 
#     'fBodyAcc-bandsEnergy()-33,48':[],
#     'fBodyAcc-bandsEnergy()-49,64':[], 
#     'fBodyAcc-bandsEnergy()-1,24':[], 
#     'fBodyAcc-bandsEnergy()-25,48':[],
#     'fBodyAcc-bandsEnergy()-1,8':[], 
#     'fBodyAcc-bandsEnergy()-9,16':[], 
#     'fBodyAcc-bandsEnergy()-17,24':[],
#     'fBodyAcc-bandsEnergy()-25,32':[], 
#     'fBodyAcc-bandsEnergy()-33,40':[], 
#     'fBodyAcc-bandsEnergy()-41,48':[],
#     'fBodyAcc-bandsEnergy()-49,56':[], 
#     'fBodyAcc-bandsEnergy()-57,64':[], 
#     'fBodyAcc-bandsEnergy()-1,16':[],
#     'fBodyAcc-bandsEnergy()-17,32':[], 
#     'fBodyAcc-bandsEnergy()-33,48':[], 
#     'fBodyAcc-bandsEnergy()-49,64':[],
#     'fBodyAcc-bandsEnergy()-1,24':[], 
#     'fBodyAcc-bandsEnergy()-25,48':[], 

    # body = filterAcceleration(window['x'])
    windowed_data.append(window)

windowed_df = pd.concat(windowed_data, ignore_index=True)
# print(testDataDict)

# print(((testDataDict['fBodyAcc-maxInds-X'])))
# print((testDataDict['tBodyAcc-arCoeff()-Y,1']))
# print((testDataDict['tBodyAcc-arCoeff()-Z,1']))
# print((testDataDict['tBodyAcc-correlation()-X,Y']))
testDataDF = pd.DataFrame(testDataDict)
print(testDataDict['tBodyAcc-mean()-X'])

x_acc = testDataDF['tBodyAcc-mean()-X'].values
fft_signal = fft(x_acc)
x_freq = fft_signal[1]
print(fft_signal[1])
x_freq_mean = np.mean(np.abs(x_freq))
print(x_freq_mean)
testDataDF.to_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/modeled_csv/test1.csv', encoding='utf-8', index=False)
# print(windowed_df)
import pymongo
import pandas as pd
import numpy as np
import math
import statsmodels.api as sm
from scipy.signal import butter, filtfilt, medfilt
from scipy.stats import median_abs_deviation, entropy
# def compute_tBodyAcc_mean_X(data):
#     # Applying median filter
#     data = data.rolling(window=3, center=True).median().fillna(method='bfill').fillna(method='ffill')
    
#     # Applying low pass Butterworth filter
#     fs = 50  # sampling frequency
#     cutoff = 20  # cutoff frequency
#     nyq = 0.5 * fs  # Nyquist frequency
#     normal_cutoff = cutoff / nyq  # normalized cutoff frequency
#     b, a = butter(3, normal_cutoff, btype='low', analog=False)
#     data = filtfilt(b, a, data, axis=0)
    
#     # Separating body and gravity acceleration signals
#     cutoff = 0.3  # cutoff frequency
#     nyq = 0.5 * fs  # Nyquist frequency
#     normal_cutoff = cutoff / nyq  # normalized cutoff frequency
#     b, a = signal.butter(1, normal_cutoff, btype='low', analog=False)
#     data = signal.filtfilt(b, a, data, axis=0)
    
#     # Computing tBodyAcc-mean()-X
#     tBodyAcc_X = data['x']
#     tBodyAcc_mean_X = tBodyAcc_X.mean()
    
#     return tBodyAcc_mean_X
def findSMA(dfx, dfy, dfz):
    sum_abs = np.abs(dfx) + np.abs(dfy) + np.abs(dfz)
    return (sum_abs/len(dfx)).mean()

def filterAcceleration(df):
    df = df.rolling(window=3, center=True, min_periods=1).median()

    fs = 50  #sampling rate
    f_cutoff = 20  # Filter cutoff frequency (Hz)
    f_cutoff2 = 0.3  # Second filter cutoff frequency (Hz)

    b, a = butter(3, f_cutoff/(fs/2), 'low')
    df_filtered = filtfilt(b, a, df, axis=0)

    b2, a2 = butter(3, f_cutoff2/(fs/2), 'low')
    gravity = filtfilt(b2, a2, df_filtered, axis=0)
    # print("Gravity mean", gravity.mean())

    body = df_filtered - gravity
    return body

def findEnergy(df):
    return sum((df**2))/len(df)
    #Sum of the squares divided by the number of values. 

def findQuantile(df):
    return np.percentile(df, 75) - np.percentile(df, 25)

def findEntropy(df, colName):
    value_counts = df[colName].value_counts(normalize=True)
    probabilities = value_counts / len(df)
    entropy = sum(-p * math.log2(p) for p in probabilities)
    return entropy

def findArCoeff(df, order):
    rho, sigma2 = sm.regression.linear_model.burg(df, order=order)
    return rho

uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb)
db = client['calaid_android']
accelerometerDataCollection = db['AccelerometerData']

listAccData = list(accelerometerDataCollection.find())
dfAccData = pd.DataFrame(listAccData)
print(dfAccData.sample())
# with np.printoptions(threshold=np.inf):
#     print(dfAccData['x'])
testDf = filterAcceleration(dfAccData['x']).mean()
print(testDf)
print(filterAcceleration(dfAccData['y']).mean())
print(filterAcceleration(dfAccData['z']).mean())
# print(dfAccData.sample())
print("Median", median_abs_deviation(filterAcceleration(dfAccData['x'])))
print("Max", max(filterAcceleration(dfAccData['x'])))
print(type(dfAccData['x']))


print("SMA", findSMA(filterAcceleration(dfAccData['x']), filterAcceleration(dfAccData['y']), filterAcceleration(dfAccData['z'])))
print("Energy", findEnergy(filterAcceleration(dfAccData['x'])))
print("Quantile", -findQuantile(filterAcceleration(dfAccData['x'])))
print("Entropy", findEntropy(filterAcceleration(dfAccData['x']), 'x'))
# print(type(dfAccData['x'].mean()))
# print("ArCoeff1", findArCoeff(filterAcceleration(dfAccData['x']), 1))
# print("ArCoeff2", findArCoeff(filterAcceleration(dfAccData['x']), 2))
# print("ArCoeff3", findArCoeff(filterAcceleration(dfAccData['x']), 3))
print("ArCoeff4", findArCoeff(filterAcceleration(dfAccData['x']), 4)[0])

testDataDict = {
    'tBodyAcc-mean()-X': [filterAcceleration(dfAccData['x']).mean()],
    "tBodyAcc-mean()-Y": [filterAcceleration(dfAccData['y']).mean()], 
    "tBodyAcc-mean()-Z": [filterAcceleration(dfAccData['z']).mean()], 
    "tBodyAcc-std()-X": [filterAcceleration(dfAccData['x']).std()], 
    "tBodyAcc-std()-Y": [filterAcceleration(dfAccData['y']).std()], 
    "tBodyAcc-std()-Z": [filterAcceleration(dfAccData['z']).std()], 
    "tBodyAcc-mad()-X": [median_abs_deviation(filterAcceleration(dfAccData['x']))], 
    "tBodyAcc-mad()-Y": [median_abs_deviation(filterAcceleration(dfAccData['y']))], 
    "tBodyAcc-mad()-Z": [median_abs_deviation(filterAcceleration(dfAccData['z']))], 
    "tBodyAcc-max()-X": [max(filterAcceleration(dfAccData['x']))], 
    "tBodyAcc-max()-Y": [max(filterAcceleration(dfAccData['y']))], 
    "tBodyAcc-max()-Z": [max(filterAcceleration(dfAccData['z']))], 
    "tBodyAcc-min()-X": [min(filterAcceleration(dfAccData['x']))], 
    "tBodyAcc-min()-Y": [min(filterAcceleration(dfAccData['y']))], 
    "tBodyAcc-min()-Z": [min(filterAcceleration(dfAccData['z']))], 
    "tBodyAcc-sma()": [findSMA(filterAcceleration(dfAccData['x']), filterAcceleration(dfAccData['y']), filterAcceleration(dfAccData['z']))], 
    "tBodyAcc-energy()-X": 0, #?
    "tBodyAcc-energy()-Y": 0, #?
    "tBodyAcc-energy()-Z": 0, #?
    "tBodyAcc-iqr()-X": [-findQuantile(filterAcceleration(dfAccData['x']))], 
    "tBodyAcc-iqr()-Y": [-findQuantile(filterAcceleration(dfAccData['y']))], 
    "tBodyAcc-iqr()-Z": [-findQuantile(filterAcceleration(dfAccData['z']))], 
    "tBodyAcc-entropy()-X": 0, 
    "tBodyAcc-entropy()-Y": 0, 
    "tBodyAcc-entropy()-Z": 0, 
    "tBodyAcc-arCoeff()-X,1": 0, 
    "tBodyAcc-arCoeff()-X,2": 0, 
    "tBodyAcc-arCoeff()-X,3": 0, 
    "tBodyAcc-arCoeff()-X,4": 0, 
    "tBodyAcc-arCoeff()-Y,1": 0, 
    "tBodyAcc-arCoeff()-Y,2": 0, 
    "tBodyAcc-arCoeff()-Y,3": 0, 
    "tBodyAcc-arCoeff()-Y,4": 0, 
    "tBodyAcc-arCoeff()-Z,1": 0, 
    "tBodyAcc-arCoeff()-Z,2": 0, 
    "tBodyAcc-arCoeff()-Z,3": 0, 
    "tBodyAcc-arCoeff()-Z,4": 0, 
    "tBodyAcc-correlation()-X,Y": 0, 
    "tBodyAcc-correlation()-X,Z": 0, 
    "tBodyAcc-correlation()-Y,Z": 0, 
    "tGravityAcc-mean()-X": 0, 
    "tGravityAcc-mean()-Y": 0, 
    "tGravityAcc-mean()-Z": 0, 
    "tGravityAcc-std()-X": 0, 
    "tGravityAcc-std()-Y": 0, 
    "tGravityAcc-std()-Z": 0, 
    "tGravityAcc-mad()-X": 0, 
    "tGravityAcc-mad()-Y": 0, 
    "tGravityAcc-mad()-Z": 0, 
    "tGravityAcc-max()-X": 0, 
    "tGravityAcc-max()-Y": 0, 
    "tGravityAcc-max()-Z": 0, 
    "tGravityAcc-min()-X": 0,
    'tGravityAcc-min()-Y': 0,
    'tGravityAcc-min()-Z': 0,
    'tGravityAcc-sma()': 0,
    'tGravityAcc-energy()-X': 0,
    'tGravityAcc-energy()-Y': 0,
    'tGravityAcc-energy()-Z': 0,
    'tGravityAcc-iqr()-X': 0,
    'tGravityAcc-iqr()-Y': 0,
    'tGravityAcc-iqr()-Z': 0,
    'tGravityAcc-entropy()-X': 0,
    'tGravityAcc-entropy()-Y': 0,
    'tGravityAcc-entropy()-Z': 0,
    'tGravityAcc-arCoeff()-X,1': 0,
    'tGravityAcc-arCoeff()-X,2': 0,
    'tGravityAcc-arCoeff()-X,3': 0,
    'tGravityAcc-arCoeff()-X,4': 0,
    'tGravityAcc-arCoeff()-Y,1': 0,
    'tGravityAcc-arCoeff()-Y,2': 0,
    'tGravityAcc-arCoeff()-Y,3': 0,
    'tGravityAcc-arCoeff()-Y,4': 0,
    'tGravityAcc-arCoeff()-Z,1': 0,
    'tGravityAcc-arCoeff()-Z,2': 0,
    'tGravityAcc-arCoeff()-Z,3': 0,
    'tGravityAcc-arCoeff()-Z,4': 0,
    'tGravityAcc-correlation()-X,Y': 0,
    'tGravityAcc-correlation()-X,Z': 0,
    'tGravityAcc-correlation()-Y,Z': 0,
    'tBodyAccJerk-mean()-X': 0,
    'tBodyAccJerk-mean()-Y': 0,
    'tBodyAccJerk-mean()-Z': 0,
    'tBodyAccJerk-std()-X': 0,
    'tBodyAccJerk-std()-Y': 0,
    'tBodyAccJerk-std()-Z': 0,
    'tBodyAccJerk-mad()-X': 0,
    'tBodyAccJerk-mad()-Y': 0,
    'tBodyAccJerk-mad()-Z': 0,
    'tBodyAccJerk-max()-X': 0,
    'tBodyAccJerk-max()-Y': 0,
    'tBodyAccJerk-max()-Z': 0,
    'tBodyAccJerk-min()-X': 0,
    'tBodyAccJerk-min()-Y': 0,
    'tBodyAccJerk-min()-Z': 0,
    'tBodyAccJerk-sma()': 0,
    'tBodyAccJerk-energy()-X': 0,
    'tBodyAccJerk-energy()-Y': 0,
    'tBodyAccJerk-energy()-Z': 0,
    'tBodyAccJerk-iqr()-X': 0,
    'tBodyAccJerk-iqr()-Y': 0,
    'tBodyAccJerk-iqr()-Z': 0,
    'tBodyAccJerk-entropy()-X': 0,
    'tBodyAccJerk-entropy()-Y': 0,
    'tBodyAccJerk-entropy()-Z': 0,
    'tBodyAccJerk-arCoeff()-X,1': 0,
    'tBodyAccJerk-arCoeff()-X,2': 0,
    'tBodyAccJerk-arCoeff()-X,3': 0,
    'tBodyAccJerk-arCoeff()-X,4': 0,
    'tBodyAccJerk-arCoeff()-Y,1': 0,
    'tBodyAccJerk-arCoeff()-Y,2': 0,
    'tBodyAccJerk-arCoeff()-Y,3': 0,
    'tBodyAccJerk-arCoeff()-Y,4': 0,
    'tBodyAccJerk-arCoeff()-Z,1': 0,
    'tBodyAccJerk-arCoeff()-Z,2': 0,
    'tBodyAccJerk-arCoeff()-Z,3': 0,
    'tBodyAccJerk-arCoeff()-Z,4': 0,
    'tBodyAccJerk-correlation()-X,Y': 0,
    'tBodyAccJerk-correlation()-X,Z': 0,
    'tBodyAccJerk-correlation()-Y,Z': 0,
    'tBodyAccMag-mean()': 0,
    'tBodyAccMag-std()': 0,
    'tBodyAccMag-mad()': 0,
    'tBodyAccMag-max()': 0,
    'tBodyAccMag-min()': 0,
    'tBodyAccMag-sma()': 0,
    'tBodyAccMag-energy()': 0,
    'tBodyAccMag-iqr()': 0,
    'tBodyAccMag-entropy()': 0,
    'tBodyAccMag-arCoeff()1': 0,
    'tBodyAccMag-arCoeff()2': 0,
    'tBodyAccMag-arCoeff()3': 0,
    'tBodyAccMag-arCoeff()4': 0,
    'tGravityAccMag-mean()': 0,
    'tGravityAccMag-std()': 0,
    'tGravityAccMag-mad()': 0,
    'tGravityAccMag-max()': 0,
    'tGravityAccMag-min()': 0,
    'tGravityAccMag-sma()': 0,
    'tGravityAccMag-energy()': 0,
    'tGravityAccMag-iqr()': 0,
    'tGravityAccMag-entropy()': 0,
    'tGravityAccMag-arCoeff()1': 0,
    'tGravityAccMag-arCoeff()2': 0,
    'tGravityAccMag-arCoeff()3': 0,
    'tGravityAccMag-arCoeff()4': 0,
    'tBodyAccJerkMag-mean()': 0,
    'tBodyAccJerkMag-std()': 0,
    'tBodyAccJerkMag-mad()': 0,
    'tBodyAccJerkMag-max()': 0,
    'tBodyAccJerkMag-min()': 0,
    'tBodyAccJerkMag-sma()': 0,
    'tBodyAccJerkMag-energy()': 0,
    'tBodyAccJerkMag-iqr()': 0,
    'tBodyAccJerkMag-entropy()': 0,
    'tBodyAccJerkMag-arCoeff()1': 0,
    'tBodyAccJerkMag-arCoeff()2': 0,
    'tBodyAccJerkMag-arCoeff()3': 0,
}



# 1 tBodyAcc-mean()-X
# 2 tBodyAcc-mean()-Y
# 3 tBodyAcc-mean()-Z
# 4 tBodyAcc-std()-X
# 5 tBodyAcc-std()-Y
# 6 tBodyAcc-std()-Z
# 7 tBodyAcc-mad()-X
# 8 tBodyAcc-mad()-Y
# 9 tBodyAcc-mad()-Z
# 10 tBodyAcc-max()-X
# 11 tBodyAcc-max()-Y
# 12 tBodyAcc-max()-Z
# 13 tBodyAcc-min()-X
# 14 tBodyAcc-min()-Y
# 15 tBodyAcc-min()-Z
# 16 tBodyAcc-sma()
# 17 tBodyAcc-energy()-X
# 18 tBodyAcc-energy()-Y
# 19 tBodyAcc-energy()-Z
# 20 tBodyAcc-iqr()-X
# 21 tBodyAcc-iqr()-Y
# 22 tBodyAcc-iqr()-Z
# 23 tBodyAcc-entropy()-X
# 24 tBodyAcc-entropy()-Y
# 25 tBodyAcc-entropy()-Z
# 26 tBodyAcc-arCoeff()-X,1
# 27 tBodyAcc-arCoeff()-X,2
# 28 tBodyAcc-arCoeff()-X,3
# 29 tBodyAcc-arCoeff()-X,4
# 30 tBodyAcc-arCoeff()-Y,1
# 31 tBodyAcc-arCoeff()-Y,2
# 32 tBodyAcc-arCoeff()-Y,3
# 33 tBodyAcc-arCoeff()-Y,4
# 34 tBodyAcc-arCoeff()-Z,1
# 35 tBodyAcc-arCoeff()-Z,2
# 36 tBodyAcc-arCoeff()-Z,3
# 37 tBodyAcc-arCoeff()-Z,4
# 38 tBodyAcc-correlation()-X,Y
# 39 tBodyAcc-correlation()-X,Z
# 40 tBodyAcc-correlation()-Y,Z
# 41 tGravityAcc-mean()-X
# 42 tGravityAcc-mean()-Y
# 43 tGravityAcc-mean()-Z
# 44 tGravityAcc-std()-X
# 45 tGravityAcc-std()-Y
# 46 tGravityAcc-std()-Z
# 47 tGravityAcc-mad()-X
# 48 tGravityAcc-mad()-Y
# 49 tGravityAcc-mad()-Z
# 50 tGravityAcc-max()-X
# 51 tGravityAcc-max()-Y
# 52 tGravityAcc-max()-Z
# 53 tGravityAcc-min()-X
# 54 tGravityAcc-min()-Y
# 55 tGravityAcc-min()-Z
# 56 tGravityAcc-sma()
# 57 tGravityAcc-energy()-X
# 58 tGravityAcc-energy()-Y
# 59 tGravityAcc-energy()-Z
# 60 tGravityAcc-iqr()-X
# 61 tGravityAcc-iqr()-Y
# 62 tGravityAcc-iqr()-Z
# 63 tGravityAcc-entropy()-X
# 64 tGravityAcc-entropy()-Y
# 65 tGravityAcc-entropy()-Z
# 66 tGravityAcc-arCoeff()-X,1
# 67 tGravityAcc-arCoeff()-X,2
# 68 tGravityAcc-arCoeff()-X,3
# 69 tGravityAcc-arCoeff()-X,4
# 70 tGravityAcc-arCoeff()-Y,1
# 71 tGravityAcc-arCoeff()-Y,2
# 72 tGravityAcc-arCoeff()-Y,3
# 73 tGravityAcc-arCoeff()-Y,4
# 74 tGravityAcc-arCoeff()-Z,1
# 75 tGravityAcc-arCoeff()-Z,2
# 76 tGravityAcc-arCoeff()-Z,3
# 77 tGravityAcc-arCoeff()-Z,4
# 78 tGravityAcc-correlation()-X,Y
# 79 tGravityAcc-correlation()-X,Z
# 80 tGravityAcc-correlation()-Y,Z
# 81 tBodyAccJerk-mean()-X
# 82 tBodyAccJerk-mean()-Y
# 83 tBodyAccJerk-mean()-Z
# 84 tBodyAccJerk-std()-X
# 85 tBodyAccJerk-std()-Y
# 86 tBodyAccJerk-std()-Z
# 87 tBodyAccJerk-mad()-X
# 88 tBodyAccJerk-mad()-Y
# 89 tBodyAccJerk-mad()-Z
# 90 tBodyAccJerk-max()-X
# 91 tBodyAccJerk-max()-Y
# 92 tBodyAccJerk-max()-Z
# 93 tBodyAccJerk-min()-X
# 94 tBodyAccJerk-min()-Y
# 95 tBodyAccJerk-min()-Z
# 96 tBodyAccJerk-sma()
# 97 tBodyAccJerk-energy()-X
# 98 tBodyAccJerk-energy()-Y
# 99 tBodyAccJerk-energy()-Z
# 100 tBodyAccJerk-iqr()-X
# 101 tBodyAccJerk-iqr()-Y
# 102 tBodyAccJerk-iqr()-Z
# 103 tBodyAccJerk-entropy()-X
# 104 tBodyAccJerk-entropy()-Y
# 105 tBodyAccJerk-entropy()-Z
# 106 tBodyAccJerk-arCoeff()-X,1
# 107 tBodyAccJerk-arCoeff()-X,2
# 108 tBodyAccJerk-arCoeff()-X,3
# 109 tBodyAccJerk-arCoeff()-X,4
# 110 tBodyAccJerk-arCoeff()-Y,1
# 111 tBodyAccJerk-arCoeff()-Y,2
# 112 tBodyAccJerk-arCoeff()-Y,3
# 113 tBodyAccJerk-arCoeff()-Y,4
# 114 tBodyAccJerk-arCoeff()-Z,1
# 115 tBodyAccJerk-arCoeff()-Z,2
# 116 tBodyAccJerk-arCoeff()-Z,3
# 117 tBodyAccJerk-arCoeff()-Z,4
# 118 tBodyAccJerk-correlation()-X,Y
# 119 tBodyAccJerk-correlation()-X,Z
# 120 tBodyAccJerk-correlation()-Y,Z
# 201 tBodyAccMag-mean()
# 202 tBodyAccMag-std()
# 203 tBodyAccMag-mad()
# 204 tBodyAccMag-max()
# 205 tBodyAccMag-min()
# 206 tBodyAccMag-sma()
# 207 tBodyAccMag-energy()
# 208 tBodyAccMag-iqr()
# 209 tBodyAccMag-entropy()
# 210 tBodyAccMag-arCoeff()1
# 211 tBodyAccMag-arCoeff()2
# 212 tBodyAccMag-arCoeff()3
# 213 tBodyAccMag-arCoeff()4
# 214 tGravityAccMag-mean()
# 215 tGravityAccMag-std()
# 216 tGravityAccMag-mad()
# 217 tGravityAccMag-max()
# 218 tGravityAccMag-min()
# 219 tGravityAccMag-sma()
# 220 tGravityAccMag-energy()
# 221 tGravityAccMag-iqr()
# 222 tGravityAccMag-entropy()
# 223 tGravityAccMag-arCoeff()1
# 224 tGravityAccMag-arCoeff()2
# 225 tGravityAccMag-arCoeff()3
# 226 tGravityAccMag-arCoeff()4
# 227 tBodyAccJerkMag-mean()
# 228 tBodyAccJerkMag-std()
# 229 tBodyAccJerkMag-mad()
# 230 tBodyAccJerkMag-max()
# 231 tBodyAccJerkMag-min()
# 232 tBodyAccJerkMag-sma()
# 233 tBodyAccJerkMag-energy()
# 234 tBodyAccJerkMag-iqr()
# 235 tBodyAccJerkMag-entropy()
# 236 tBodyAccJerkMag-arCoeff()1
# 237 tBodyAccJerkMag-arCoeff()2
# 238 tBodyAccJerkMag-arCoeff()3
# 239 tBodyAccJerkMag-arCoeff()4
# 266 fBodyAcc-mean()-X
# 267 fBodyAcc-mean()-Y
# 268 fBodyAcc-mean()-Z
# 269 fBodyAcc-std()-X
# 270 fBodyAcc-std()-Y
# 271 fBodyAcc-std()-Z
# 272 fBodyAcc-mad()-X
# 273 fBodyAcc-mad()-Y
# 274 fBodyAcc-mad()-Z
# 275 fBodyAcc-max()-X
# 276 fBodyAcc-max()-Y
# 277 fBodyAcc-max()-Z
# 278 fBodyAcc-min()-X
# 279 fBodyAcc-min()-Y
# 280 fBodyAcc-min()-Z
# 281 fBodyAcc-sma()
# 282 fBodyAcc-energy()-X
# 283 fBodyAcc-energy()-Y
# 284 fBodyAcc-energy()-Z
# 285 fBodyAcc-iqr()-X
# 286 fBodyAcc-iqr()-Y
# 287 fBodyAcc-iqr()-Z
# 288 fBodyAcc-entropy()-X
# 289 fBodyAcc-entropy()-Y
# 290 fBodyAcc-entropy()-Z
# 291 fBodyAcc-maxInds-X
# 292 fBodyAcc-maxInds-Y
# 293 fBodyAcc-maxInds-Z
# 294 fBodyAcc-meanFreq()-X
# 295 fBodyAcc-meanFreq()-Y
# 296 fBodyAcc-meanFreq()-Z
# 297 fBodyAcc-skewness()-X
# 298 fBodyAcc-kurtosis()-X
# 299 fBodyAcc-skewness()-Y
# 300 fBodyAcc-kurtosis()-Y
# 301 fBodyAcc-skewness()-Z
# 302 fBodyAcc-kurtosis()-Z
# 303 fBodyAcc-bandsEnergy()-1,8
# 304 fBodyAcc-bandsEnergy()-9,16
# 305 fBodyAcc-bandsEnergy()-17,24
# 306 fBodyAcc-bandsEnergy()-25,32
# 307 fBodyAcc-bandsEnergy()-33,40
# 308 fBodyAcc-bandsEnergy()-41,48
# 309 fBodyAcc-bandsEnergy()-49,56
# 310 fBodyAcc-bandsEnergy()-57,64
# 311 fBodyAcc-bandsEnergy()-1,16
# 312 fBodyAcc-bandsEnergy()-17,32
# 313 fBodyAcc-bandsEnergy()-33,48
# 314 fBodyAcc-bandsEnergy()-49,64
# 315 fBodyAcc-bandsEnergy()-1,24
# 316 fBodyAcc-bandsEnergy()-25,48
# 317 fBodyAcc-bandsEnergy()-1,8
# 318 fBodyAcc-bandsEnergy()-9,16
# 319 fBodyAcc-bandsEnergy()-17,24
# 320 fBodyAcc-bandsEnergy()-25,32
# 321 fBodyAcc-bandsEnergy()-33,40
# 322 fBodyAcc-bandsEnergy()-41,48
# 323 fBodyAcc-bandsEnergy()-49,56
# 324 fBodyAcc-bandsEnergy()-57,64
# 325 fBodyAcc-bandsEnergy()-1,16
# 326 fBodyAcc-bandsEnergy()-17,32
# 327 fBodyAcc-bandsEnergy()-33,48
# 328 fBodyAcc-bandsEnergy()-49,64
# 329 fBodyAcc-bandsEnergy()-1,24
# 330 fBodyAcc-bandsEnergy()-25,48
# 331 fBodyAcc-bandsEnergy()-1,8
# 332 fBodyAcc-bandsEnergy()-9,16
# 333 fBodyAcc-bandsEnergy()-17,24
# 334 fBodyAcc-bandsEnergy()-25,32
# 335 fBodyAcc-bandsEnergy()-33,40
# 336 fBodyAcc-bandsEnergy()-41,48
# 337 fBodyAcc-bandsEnergy()-49,56
# 338 fBodyAcc-bandsEnergy()-57,64
# 339 fBodyAcc-bandsEnergy()-1,16
# 340 fBodyAcc-bandsEnergy()-17,32
# 341 fBodyAcc-bandsEnergy()-33,48
# 342 fBodyAcc-bandsEnergy()-49,64
# 343 fBodyAcc-bandsEnergy()-1,24
# 344 fBodyAcc-bandsEnergy()-25,48
# 345 fBodyAccJerk-mean()-X
# 346 fBodyAccJerk-mean()-Y
# 347 fBodyAccJerk-mean()-Z
# 348 fBodyAccJerk-std()-X
# 349 fBodyAccJerk-std()-Y
# 350 fBodyAccJerk-std()-Z
# 351 fBodyAccJerk-mad()-X
# 352 fBodyAccJerk-mad()-Y
# 353 fBodyAccJerk-mad()-Z
# 354 fBodyAccJerk-max()-X
# 355 fBodyAccJerk-max()-Y
# 356 fBodyAccJerk-max()-Z
# 357 fBodyAccJerk-min()-X
# 358 fBodyAccJerk-min()-Y
# 359 fBodyAccJerk-min()-Z
# 360 fBodyAccJerk-sma()
# 361 fBodyAccJerk-energy()-X
# 362 fBodyAccJerk-energy()-Y
# 363 fBodyAccJerk-energy()-Z
# 364 fBodyAccJerk-iqr()-X
# 365 fBodyAccJerk-iqr()-Y
# 366 fBodyAccJerk-iqr()-Z
# 367 fBodyAccJerk-entropy()-X
# 368 fBodyAccJerk-entropy()-Y
# 369 fBodyAccJerk-entropy()-Z
# 370 fBodyAccJerk-maxInds-X
# 371 fBodyAccJerk-maxInds-Y
# 372 fBodyAccJerk-maxInds-Z
# 373 fBodyAccJerk-meanFreq()-X
# 374 fBodyAccJerk-meanFreq()-Y
# 375 fBodyAccJerk-meanFreq()-Z
# 376 fBodyAccJerk-skewness()-X
# 377 fBodyAccJerk-kurtosis()-X
# 378 fBodyAccJerk-skewness()-Y
# 379 fBodyAccJerk-kurtosis()-Y
# 380 fBodyAccJerk-skewness()-Z
# 381 fBodyAccJerk-kurtosis()-Z
# 382 fBodyAccJerk-bandsEnergy()-1,8
# 383 fBodyAccJerk-bandsEnergy()-9,16
# 384 fBodyAccJerk-bandsEnergy()-17,24
# 385 fBodyAccJerk-bandsEnergy()-25,32
# 386 fBodyAccJerk-bandsEnergy()-33,40
# 387 fBodyAccJerk-bandsEnergy()-41,48
# 388 fBodyAccJerk-bandsEnergy()-49,56
# 389 fBodyAccJerk-bandsEnergy()-57,64
# 390 fBodyAccJerk-bandsEnergy()-1,16
# 391 fBodyAccJerk-bandsEnergy()-17,32
# 392 fBodyAccJerk-bandsEnergy()-33,48
# 393 fBodyAccJerk-bandsEnergy()-49,64
# 394 fBodyAccJerk-bandsEnergy()-1,24
# 395 fBodyAccJerk-bandsEnergy()-25,48
# 396 fBodyAccJerk-bandsEnergy()-1,8
# 397 fBodyAccJerk-bandsEnergy()-9,16
# 398 fBodyAccJerk-bandsEnergy()-17,24
# 399 fBodyAccJerk-bandsEnergy()-25,32
# 400 fBodyAccJerk-bandsEnergy()-33,40
# 401 fBodyAccJerk-bandsEnergy()-41,48
# 402 fBodyAccJerk-bandsEnergy()-49,56
# 403 fBodyAccJerk-bandsEnergy()-57,64
# 404 fBodyAccJerk-bandsEnergy()-1,16
# 405 fBodyAccJerk-bandsEnergy()-17,32
# 406 fBodyAccJerk-bandsEnergy()-33,48
# 407 fBodyAccJerk-bandsEnergy()-49,64
# 408 fBodyAccJerk-bandsEnergy()-1,24
# 409 fBodyAccJerk-bandsEnergy()-25,48
# 410 fBodyAccJerk-bandsEnergy()-1,8
# 411 fBodyAccJerk-bandsEnergy()-9,16
# 412 fBodyAccJerk-bandsEnergy()-17,24
# 413 fBodyAccJerk-bandsEnergy()-25,32
# 414 fBodyAccJerk-bandsEnergy()-33,40
# 415 fBodyAccJerk-bandsEnergy()-41,48
# 416 fBodyAccJerk-bandsEnergy()-49,56
# 417 fBodyAccJerk-bandsEnergy()-57,64
# 418 fBodyAccJerk-bandsEnergy()-1,16
# 419 fBodyAccJerk-bandsEnergy()-17,32
# 420 fBodyAccJerk-bandsEnergy()-33,48
# 421 fBodyAccJerk-bandsEnergy()-49,64
# 422 fBodyAccJerk-bandsEnergy()-1,24
# 423 fBodyAccJerk-bandsEnergy()-25,48
# fBodyAccMag-mean()
# 504 fBodyAccMag-std()
# 505 fBodyAccMag-mad()
# 506 fBodyAccMag-max()
# 507 fBodyAccMag-min()
# 508 fBodyAccMag-sma()
# 509 fBodyAccMag-energy()
# 510 fBodyAccMag-iqr()
# 511 fBodyAccMag-entropy()
# 512 fBodyAccMag-maxInds
# 513 fBodyAccMag-meanFreq()
# 514 fBodyAccMag-skewness()
# 515 fBodyAccMag-kurtosis()
# 516 fBodyBodyAccJerkMag-mean()
# 517 fBodyBodyAccJerkMag-std()
# 518 fBodyBodyAccJerkMag-mad()
# 519 fBodyBodyAccJerkMag-max()
# 520 fBodyBodyAccJerkMag-min()
# 521 fBodyBodyAccJerkMag-sma()
# 522 fBodyBodyAccJerkMag-energy()
# 523 fBodyBodyAccJerkMag-iqr()
# 524 fBodyBodyAccJerkMag-entropy()
# 525 fBodyBodyAccJerkMag-maxInds
# 526 fBodyBodyAccJerkMag-meanFreq()
# 527 fBodyBodyAccJerkMag-skewness()
# 528 fBodyBodyAccJerkMag-kurtosis()
# 555 angle(tBodyAccMean,gravity)
# 556 angle(tBodyAccJerkMean,gravityMean)
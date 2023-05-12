import pymongo
import pandas as pd
import numpy as np
import math
import statsmodels.api as sm
from scipy.signal import butter, filtfilt, medfilt
from scipy.stats import median_abs_deviation, entropy
from scipy.fft import fft

def applyFilters(df):
    fs = 50 
    f_cutoff = 20  
    f_cutoff2 = 0.3  # Second filter cutoff frequency (Hz)
    df = medfilt(df, kernel_size=5)  #kernel_size=2

    b, a = butter(3, f_cutoff/(fs/2), 'low')
    df_filtered = filtfilt(b, a, df, axis=0)

    b2, a2 = butter(3, f_cutoff2/(fs/2), 'low')
    gravity = filtfilt(b2, a2, df_filtered, axis=0)

    return df_filtered, gravity

def filterAcceleration(df):
    df_filtered, gravity = applyFilters(df)
    body = df_filtered - gravity
    return body

def filterGravity(df):
    df_filtered, gravity = applyFilters(df)
    return gravity

def findBodyJerk(dfAccData):
    dt = pd.to_datetime(dfAccData['timestamp']).diff().apply(lambda x: x/np.timedelta64(1, 'ms')).fillna(0).astype('int64')

    vx = dfAccData['xBody'].diff() / dt
    vy = dfAccData['yBody'].diff() / dt
    vz = dfAccData['zBody'].diff() / dt

    jx = vx.diff() / dt
    jy = vy.diff() / dt
    jz = vz.diff() / dt

    return vx, vy, vz

def findSMA(dfx, dfy, dfz):
    sum_abs = np.abs(dfx) + np.abs(dfy) + np.abs(dfz)
    return (sum_abs/len(dfx)).mean()

def findSMAMagnitude(df):
    sum_abs = np.abs(df)
    return (sum_abs/len(df)).mean()

def findEnergy(df):
    return np.sum((df**2))/len(df)
    #Sum of the squares divided by the number of values. 

def findQuantile(df):
    return np.percentile(df, 75) - np.percentile(df, 25)

def findEntropy(df, base=None):
    hist, _ = np.histogram(df, bins='auto')
    hist = hist / sum(hist)
    return entropy(hist)
    # value,counts = np.unique(df, return_counts=True)
    # return entropy(counts, base=base)
    # value_counts = df[colName].value_counts(normalize=True)
    # probabilities = value_counts / len(df)
    # entropy = sum(-p * math.log2(p) for p in probabilities)
    # return entropy


def entropy1(labels, base=None):
  value,counts = np.unique(labels, return_counts=True)
  return entropy(counts, base=base)


def findArCoeff(df, order):
    rho, sigma2 = sm.regression.linear_model.burg(df, order=order)
    return rho

def findMagnitudeBody(df):
    return np.sqrt(df['xBody']**2 + df['yBody']**2 + df['zBody']**2)

def findMagnitudeGravity(df):
    return np.sqrt(df['xGravity']**2 + df['yGravity']**2 + df['zGravity']**2)

def findMagnitudeBodyJerk(df):
    return np.sqrt(df['xBodyJerk']**2 + df['yBodyJerk']**2 + df['zBodyJerk']**2)

def findFFT(df):
    return np.abs(np.fft.fft(df.values))
     
def maxInds(df):
    max_index = np.argmax(np.abs(df))
    return max_index
import pymongo
import pandas as pd
import numpy as np
import math
import statsmodels.api as sm
from scipy.signal import butter, filtfilt, medfilt
from scipy.stats import median_abs_deviation, entropy

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

def filterGravity(df):
    df = df.rolling(window=3, center=True, min_periods=1).median()

    fs = 50  #sampling rate
    f_cutoff = 20  # Filter cutoff frequency (Hz)
    f_cutoff2 = 0.3  # Second filter cutoff frequency (Hz)

    b, a = butter(3, f_cutoff/(fs/2), 'low')
    df_filtered = filtfilt(b, a, df, axis=0)

    b2, a2 = butter(3, f_cutoff2/(fs/2), 'low')
    gravity = filtfilt(b2, a2, df_filtered, axis=0)

    return gravity

def findJerk(dfAccData):
    dt = pd.to_datetime(dfAccData['timestamp']).diff().apply(lambda x: x/np.timedelta64(1, 'ms')).fillna(0).astype('int64')

    vx = dfAccData['xBody'].diff() / dt
    # vy = dfAccData['y'].diff() / dt
    # vz = dfAccData['z'].diff() / dt

    jx = vx.diff() / dt
    # jy = vy.diff() / dt
    # jz = vz.diff() / dt

    return jx

def findSMA(dfx, dfy, dfz):
    sum_abs = np.abs(dfx) + np.abs(dfy) + np.abs(dfz)
    return (sum_abs/len(dfx)).mean()

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

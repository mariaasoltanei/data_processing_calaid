import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymongo
from processingFunctions import filterAcceleration, findFFT, maxInds, findMagnitudeGravity,findMagnitudeBodyJerk, findBodyJerk, findSMAMagnitude, findMagnitudeBody, filterGravity, findSMA, findEnergy, findQuantile, findEntropy, findArCoeff
from scipy.fft import fft,fftfreq, rfftfreq, rfft
uriMongodb = 'mongodb+srv://root:caloriepredictor2023@atlascluster.lyrf4oo.mongodb.net/calaid_android'
client = pymongo.MongoClient(uriMongodb)
db = client['calaid_android']
accelerometerDataCollection = db['AccelerometerData']

listAccData = list(accelerometerDataCollection.find({ "userId": "6414e7b4911b2b5943024071" }))
print(len(listAccData))
dfAccData = pd.DataFrame(listAccData)

dfAccData = dfAccData.sort_values('timestamp')
x = dfAccData['x']
y = dfAccData['y']
z = dfAccData['z']
t = dfAccData['timestamp']

dfAccData['xBody'] = filterAcceleration(dfAccData['x'])
dfAccData['yBody'] = filterAcceleration(dfAccData['y'])
dfAccData['zBody'] = filterAcceleration(dfAccData['z'])

dfAccData['xGravity'] = filterGravity(dfAccData['x'])
dfAccData['yGravity'] = filterGravity(dfAccData['y'])
dfAccData['zGravity'] = filterGravity(dfAccData['z'])
dfAccData['xBodyJerk'], dfAccData['yBodyJerk'], dfAccData['zBodyJerk'] = findBodyJerk(dfAccData)

dfAccData['xfBody'] = np.abs(fft(dfAccData['xBody'].values))
dfAccData['yfBody'] = np.abs(fft(dfAccData['yBody'].values))
dfAccData['zfBody'] = np.abs(fft(dfAccData['zBody'].values))

# fig, ax = plt.subplots(nrows=3, sharex=True, figsize=(10, 6))
# ax[0].plot(t, x, color='red')
# ax[0].set_ylabel('X acceleration')
# ax[1].plot(t, y, color='green')
# ax[1].set_ylabel('Y acceleration')
# ax[2].plot(t, z, color='blue')
# ax[2].set_ylabel('Z acceleration')
# ax[2].set_xlabel('Timestamp')


# fig2, ax2 = plt.subplots(nrows=3, sharex=True, figsize=(10, 6))
# ax2[0].plot(t, dfAccData['xBody'], color='red')
# ax2[0].set_ylabel('xBody')
# ax2[1].plot(t, dfAccData['yBody'], color='green')
# ax2[1].set_ylabel('yBody')
# ax2[2].plot(t, dfAccData['zBody'], color='blue')
# ax2[2].set_ylabel('zBody')
# ax2[2].set_xlabel('Timestamp')

# fig3, ax3 = plt.subplots(nrows=3, sharex=True, figsize=(10, 6))
# ax3[0].plot(t, dfAccData['xGravity'], color='red')
# ax3[0].set_ylabel('xGravity')
# ax3[1].plot(t, dfAccData['yGravity'], color='green')
# ax3[1].set_ylabel('yGravity')
# ax3[2].plot(t, dfAccData['yGravity'], color='blue')
# ax3[2].set_ylabel('zGravity')
# ax3[2].set_xlabel('Timestamp')

# fig4, ax4 = plt.subplots(nrows=3, sharex=True, figsize=(10, 6))
# ax4[0].plot(t, dfAccData['xBodyJerk'], color='red')
# ax4[0].set_ylabel('xBodyJerk')
# ax4[1].plot(t, dfAccData['yBodyJerk'], color='green')
# ax4[1].set_ylabel('yBodyJerk')
# ax4[2].plot(t, dfAccData['zBodyJerk'], color='blue')
# ax4[2].set_ylabel('zBodyJerk')
# ax4[2].set_xlabel('Timestamp')

#https://towardsdatascience.com/fourier-transform-the-practical-python-implementation-acdd32f1b96a

fig5, ax5 = plt.subplots(nrows=3, sharex=True, figsize=(10, 6))
ax5[0].plot(t, dfAccData['xfBody'], color='red')
ax5[0].set_ylabel('xfBody')
ax5[1].plot(t, dfAccData['yfBody'], color='green')
ax5[1].set_ylabel('yfBody')
ax5[2].plot(t, dfAccData['zfBody'], color='blue')
ax5[2].set_ylabel('zfBody')
ax5[2].set_xlabel('Timestamp')

#get the actual amplitudes of the spectrum, we have to normalize the output of (fft) by N/2 the number of samples.
N = len(dfAccData['xfBody'].values)
normalize = N/2
print(N)

fig6, ax6 = plt.subplots(nrows=3, sharex=True, figsize=(10, 6))
ax6[0].plot(dfAccData['xfBody'].values/normalize, color='red')
ax6[0].set_ylabel('xfBody')
ax6[0].set_xlabel('Samples')


sampling_rate = 200.0 # It's used as a sample spacing
frequency_axis = fftfreq(N, d=1.0/sampling_rate)
norm_amplitude = dfAccData['xfBody'].values/normalize

fig7, ax7 = plt.subplots(nrows=3, sharex=True, figsize=(10, 6))
ax7[0].plot(frequency_axis, norm_amplitude, color='red')
ax7[0].set_xlabel('Frequency[Hz]')
ax7[0].set_ylabel('Amplitude')

#final form of the spectrum (the actual amplitudes on the right frequencies).
fig8, ax8 = plt.subplots(nrows=3, sharex=True, figsize=(10, 6))
ax8[0].plot(rfftfreq(N, d=1/sampling_rate), 2*np.abs(rfft(dfAccData['xBody'].values))/N)
ax8[0].set_xlabel('Frequency[Hz]')
ax8[0].set_ylabel('Amplitude')
plt.show()

plt.close()
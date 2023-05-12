import os
import pandas as pd
import numpy as np
from sklearn import utils, metrics, svm
from statistics import mean

#TRAIN: 7352 windows, fiecare a cate 128 samples

path = "/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/"
trainFilesPaths = [
    path + "train/Inertial Signals/body_acc_x_train.txt",
    path + "train/Inertial Signals/body_acc_y_train.txt",
    path + "train/Inertial Signals/body_acc_z_train.txt",
    # path + "train/Inertial Signals/body_gyro_x_train.txt",
    # path + "train/Inertial Signals/body_gyro_y_train.txt",
    # path + "train/Inertial Signals/body_gyro_z_train.txt",
    # path + "train/Inertial Signals/total_acc_x_train.txt",
    # path + "train/Inertial Signals/total_acc_y_train.txt",
    # path + "train/Inertial Signals/total_acc_z_train.txt",
]
#ce alte operatii sa mai aplic
xTrain = {
    'body_acc_x_mean': [],
    'body_acc_y_mean': [],
    'body_acc_z_mean': [],
    'body_acc_x_std': [],
    'body_acc_y_std': [],
    'body_acc_z_std': [],
    'body_acc_x_max': [],
    'body_acc_y_max': [],
    'body_acc_z_max': [],
    'body_acc_x_min': [],
    'body_acc_y_min': [],
    'body_acc_z_min': [],

    'body_gyro_x_mean': [],
    'body_gyro_y_mean': [],
    'body_gyro_z_mean': [],
    'body_gyro_x_std': [],
    'body_gyro_y_std': [],
    'body_gyro_z_std': [],
    'body_gyro_x_max': [],
    'body_gyro_y_max': [],
    'body_gyro_z_max': [],
    'body_gyro_x_min': [],
    'body_gyro_y_min': [],
    'body_gyro_z_min': [],

    # 'total_acc_x_mean': [],
    # 'total_acc_y_mean': [],
    # 'total_acc_z_mean': [],
    # 'total_acc_x_std': [],
    # 'total_acc_y_std': [],
    # 'total_acc_z_std': []
}
for trainFile in trainFilesPaths:
    print(trainFile)
    if("body_acc" in trainFile):
        columnName = trainFile.split("/")[11][0:10]
    else:
        columnName = trainFile.split("/")[11][0:11]

    f = open(trainFile)
    lines = f.readlines()
    for line in lines:
        window = line.replace('  ', ' ').strip().split(' ')
        floats = [float(x) for x in window]
        xTrain[columnName + '_mean'].append(np.mean(floats))
        xTrain[columnName + '_std'].append(np.std(floats))
        xTrain[columnName + '_max'].append(max(floats))
        xTrain[columnName + '_min'].append(min(floats))


dfTrain = pd.DataFrame(xTrain)
print(dfTrain)
yTrain = pd.read_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/train/y_train.txt', header=None)
print(yTrain)
labelMappingDict = {}
with open('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/activity_labels.txt') as f:
    for line in f.readlines():
        labelMappingDict[int(line.split()[0])] = line.split()[1]
dfTrain['Activity'] = yTrain
dfTrain['ActivityName'] = dfTrain['Activity'].map(labelMappingDict)

dfTrain.to_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/data_processing_calaid/phase2/train.csv', index=False)


testFilesPaths = [
    path + "test/Inertial Signals/body_acc_x_test.txt",
    path + "test/Inertial Signals/body_acc_y_test.txt",
    path + "test/Inertial Signals/body_acc_z_test.txt",
    # path + "test/Inertial Signals/body_gyro_x_test.txt",
    # path + "test/Inertial Signals/body_gyro_y_test.txt",
    # path + "test/Inertial Signals/body_gyro_z_test.txt",
    # path + "test/Inertial Signals/total_acc_x_test.txt",
    # path + "test/Inertial Signals/total_acc_y_test.txt",
    # path + "test/Inertial Signals/total_acc_z_test.txt",
]
#ce alte operatii sa mai aplic
xTest = {
    'body_acc_x_mean': [],
    'body_acc_y_mean': [],
    'body_acc_z_mean': [],
    'body_acc_x_std': [],
    'body_acc_y_std': [],
    'body_acc_z_std': [],
    'body_acc_x_max': [],
    'body_acc_y_max': [],
    'body_acc_z_max': [],
    'body_acc_x_min': [],
    'body_acc_y_min': [],
    'body_acc_z_min': [],

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
for testFile in testFilesPaths:
    print(testFile)
    if("body_acc" in testFile):
        columnName = testFile.split("/")[11][0:10]
    else:
        columnName = testFile.split("/")[11][0:11]

    f = open(testFile)
    lines = f.readlines()
    for line in lines:
        window = line.replace('  ', ' ').strip().split(' ')
        floats = [float(x) for x in window]
        xTest[columnName + '_mean'].append(np.mean(floats))
        xTest[columnName + '_std'].append(np.std(floats))
        xTest[columnName + '_max'].append(max(floats))
        xTest[columnName + '_min'].append(min(floats))

#activity recognition pt activity multiplier
dfTest = pd.DataFrame(xTest)
yTest = pd.read_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/test/y_test.txt', header=None)
labelMappingDict = {}
with open('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/activity_labels.txt') as f:
    for line in f.readlines():
        labelMappingDict[int(line.split()[0])] = line.split()[1]
dfTest['Activity'] = yTest
dfTest['ActivityName'] = dfTrain['Activity'].map(labelMappingDict)

dfTest.to_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/data_processing_calaid/phase2/test.csv', index=False)

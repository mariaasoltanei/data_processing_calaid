import pandas as pd

features = list() # set()
with open('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/features.txt') as f:
    for line in f.readlines():
        # if "acc" in line.lower():
            features.append(line.split()[1])

uniqueFeatureName = set()
uniqueFeatures = list()
for id, x in enumerate(features):
    if x not in uniqueFeatureName:
        uniqueFeatures.append(x)
        uniqueFeatureName.add(x)
    elif x + 'n' not in uniqueFeatureName:
        uniqueFeatures.append(x + 'i')
        uniqueFeatureName.add(x + 'i')
    else:
        uniqueFeatures.append(x + 'ii')
        uniqueFeatureName.add(x + 'ii')

# for feature in features:
#     print(feature)

# for uniqueFeature in uniqueFeatures:
#     print(uniqueFeature)

print("Nr of features", len(features))

xTrain = pd.read_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/train/X_train.txt', delim_whitespace=True, header=None)
xTrain.columns = uniqueFeatures


yTrain = pd.read_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/train/y_train.txt', header=None)
labelMappingDict = {}
with open('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/activity_labels.txt') as f:
    for line in f.readlines():
        labelMappingDict[int(line.split()[0])] = line.split()[1]

trainDF = xTrain
trainDF = trainDF.drop(trainDF.columns[~trainDF.columns.str.contains('Acc')], axis=1)
trainDF['Participant no.'] = pd.read_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/train/subject_train.txt', header=None)
#print(trainDF.sample())
trainDF['Activity'] = yTrain
trainDF['ActivityName'] = trainDF['Activity'].map(labelMappingDict)
#print(trainDF.sample())
print("Duplicates - train", sum(trainDF.duplicated()))
#print("Null vals - train", sum(trainDF.isnull().values))

# print(trainDF.columns)

print("TRAIN SAMPLE")
print(trainDF.sample())
trainDF.to_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/modeled_csv/train_data.csv', index=False)
#---------------------------
#TEST DATA!!!!!
xTest = pd.read_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/test/X_test.txt', delim_whitespace=True, header=None)
xTest.columns = uniqueFeatures


yTest = pd.read_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/test/y_test.txt', header=None)

testDF = xTest
testDF = testDF.drop(testDF.columns[~testDF.columns.str.contains('Acc')], axis=1)
testDF['Participant no.'] = pd.read_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/test/subject_test.txt', header=None)
testDF['Activity'] = yTest
testDF['ActivityName'] = testDF['Activity'].map(labelMappingDict)
print("Duplicates - test", sum(testDF.duplicated()))
#print("Null vals - test", sum(testDF.isnull().values))

print("TEST SAMPLE")
print(testDF.sample())

testDF.to_csv('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/modeled_csv/test_data.csv', index=False)


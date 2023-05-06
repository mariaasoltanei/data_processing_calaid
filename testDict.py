testDataDict = {
    'tBodyAcc-mean()-X': [],
    "tBodyAcc-mean()-Y": [], 
    "tBodyAcc-mean()-Z": [], 
    "tBodyAcc-std()-X": [], 
    "tBodyAcc-std()-Y": [], 
    "tBodyAcc-std()-Z": [], 
    "tBodyAcc-mad()-X": [], 
    "tBodyAcc-mad()-Y": [], 
    "tBodyAcc-mad()-Z": [], 
    "tBodyAcc-max()-X": [], 
    "tBodyAcc-max()-Y": [], 
    "tBodyAcc-max()-Z": [], 
    "tBodyAcc-min()-X": [], 
    "tBodyAcc-min()-Y": [], 
    "tBodyAcc-min()-Z": [], 
    "tBodyAcc-sma()": [], 
    "tBodyAcc-energy()-X": [], #?
    "tBodyAcc-energy()-Y": [], #?
    "tBodyAcc-energy()-Z": [], #?
    "tBodyAcc-iqr()-X": [], 
    "tBodyAcc-iqr()-Y": [], 
    "tBodyAcc-iqr()-Z": [], 
    "tBodyAcc-entropy()-X": [], 
    "tBodyAcc-entropy()-Y": [], 
    "tBodyAcc-entropy()-Z": [], 
    "tBodyAcc-arCoeff()-X,1": [], 
    "tBodyAcc-arCoeff()-X,2": [], 
    "tBodyAcc-arCoeff()-X,3": [], 
    "tBodyAcc-arCoeff()-X,4": [], 
    "tBodyAcc-arCoeff()-Y,1": [], 
    "tBodyAcc-arCoeff()-Y,2": [], 
    "tBodyAcc-arCoeff()-Y,3": [], 
    "tBodyAcc-arCoeff()-Y,4": [], 
    "tBodyAcc-arCoeff()-Z,1": [], 
    "tBodyAcc-arCoeff()-Z,2": [], 
    "tBodyAcc-arCoeff()-Z,3": [], 
    "tBodyAcc-arCoeff()-Z,4": [], 
    "tBodyAcc-correlation()-X,Y": [], 
    "tBodyAcc-correlation()-X,Z": [], 
    "tBodyAcc-correlation()-Y,Z": [], 
    "tGravityAcc-mean()-X": [], 
    "tGravityAcc-mean()-Y": [], 
    "tGravityAcc-mean()-Z": [], 
    "tGravityAcc-std()-X": [], 
    "tGravityAcc-std()-Y": [], 
    "tGravityAcc-std()-Z": [], 
    "tGravityAcc-mad()-X": [], 
    "tGravityAcc-mad()-Y": [], 
    "tGravityAcc-mad()-Z": [], 
    "tGravityAcc-max()-X": [], 
    "tGravityAcc-max()-Y": [], 
    "tGravityAcc-max()-Z": [], 
    "tGravityAcc-min()-X": [],
    'tGravityAcc-min()-Y': [],
    'tGravityAcc-min()-Z': [],
    'tGravityAcc-sma()': [],
    'tGravityAcc-energy()-X': [],
    'tGravityAcc-energy()-Y': [],
    'tGravityAcc-energy()-Z': [],
    'tGravityAcc-iqr()-X': [],
    'tGravityAcc-iqr()-Y': [],
    'tGravityAcc-iqr()-Z': [],
    'tGravityAcc-entropy()-X': [],
    'tGravityAcc-entropy()-Y': [],
    'tGravityAcc-entropy()-Z': [],
    'tGravityAcc-arCoeff()-X,1': [],
    'tGravityAcc-arCoeff()-X,2': [],
    'tGravityAcc-arCoeff()-X,3': [],
    'tGravityAcc-arCoeff()-X,4': [],
    'tGravityAcc-arCoeff()-Y,1': [],
    'tGravityAcc-arCoeff()-Y,2': [],
    'tGravityAcc-arCoeff()-Y,3': [],
    'tGravityAcc-arCoeff()-Y,4': [],
    'tGravityAcc-arCoeff()-Z,1': [],
    'tGravityAcc-arCoeff()-Z,2': [],
    'tGravityAcc-arCoeff()-Z,3': [],
    'tGravityAcc-arCoeff()-Z,4': [],
    'tGravityAcc-correlation()-X,Y': [],
    'tGravityAcc-correlation()-X,Z': [],
    'tGravityAcc-correlation()-Y,Z': [],
    'tBodyAccJerk-mean()-X': [],
    'tBodyAccJerk-mean()-Y': [],
    'tBodyAccJerk-mean()-Z': [],
    'tBodyAccJerk-std()-X': [],
    'tBodyAccJerk-std()-Y': [],
    'tBodyAccJerk-std()-Z': [],
    'tBodyAccJerk-mad()-X': [],
    'tBodyAccJerk-mad()-Y': [],
    'tBodyAccJerk-mad()-Z': [],
    'tBodyAccJerk-max()-X': [],
    'tBodyAccJerk-max()-Y': [],
    'tBodyAccJerk-max()-Z': [],
    'tBodyAccJerk-min()-X': [],
    'tBodyAccJerk-min()-Y': [],
    'tBodyAccJerk-min()-Z': [],
    'tBodyAccJerk-sma()': [],
    'tBodyAccJerk-energy()-X': [],
    'tBodyAccJerk-energy()-Y': [],
    'tBodyAccJerk-energy()-Z': [],
    'tBodyAccJerk-iqr()-X': [],
    'tBodyAccJerk-iqr()-Y': [],
    'tBodyAccJerk-iqr()-Z': [],
    'tBodyAccJerk-entropy()-X': [],
    'tBodyAccJerk-entropy()-Y': [],
    'tBodyAccJerk-entropy()-Z': [],
    'tBodyAccJerk-arCoeff()-X,1': [],
    'tBodyAccJerk-arCoeff()-X,2': [],
    'tBodyAccJerk-arCoeff()-X,3': [],
    'tBodyAccJerk-arCoeff()-X,4': [],
    'tBodyAccJerk-arCoeff()-Y,1': [],
    'tBodyAccJerk-arCoeff()-Y,2': [],
    'tBodyAccJerk-arCoeff()-Y,3': [],
    'tBodyAccJerk-arCoeff()-Y,4': [],
    'tBodyAccJerk-arCoeff()-Z,1': [],
    'tBodyAccJerk-arCoeff()-Z,2': [],
    'tBodyAccJerk-arCoeff()-Z,3': [],
    'tBodyAccJerk-arCoeff()-Z,4': [],
    'tBodyAccJerk-correlation()-X,Y': [],
    'tBodyAccJerk-correlation()-X,Z': [],
    'tBodyAccJerk-correlation()-Y,Z': [],
    'tBodyAccMag-mean()': [],
    'tBodyAccMag-std()': [],
    'tBodyAccMag-mad()': [],
    'tBodyAccMag-max()': [],
    'tBodyAccMag-min()': [],
    'tBodyAccMag-sma()': [],
    'tBodyAccMag-energy()': [],
    'tBodyAccMag-iqr()': [],
    'tBodyAccMag-entropy()': [],
    'tBodyAccMag-arCoeff()1': [],
    'tBodyAccMag-arCoeff()2': [],
    'tBodyAccMag-arCoeff()3': [],
    'tBodyAccMag-arCoeff()4': [],
    'tGravityAccMag-mean()': [],
    'tGravityAccMag-std()': [],
    'tGravityAccMag-mad()': [],
    'tGravityAccMag-max()': [],
    'tGravityAccMag-min()': [],
    'tGravityAccMag-sma()': [],
    'tGravityAccMag-energy()': [],
    'tGravityAccMag-iqr()': [],
    'tGravityAccMag-entropy()': [],
    'tGravityAccMag-arCoeff()1': [],
    'tGravityAccMag-arCoeff()2': [],
    'tGravityAccMag-arCoeff()3': [],
    'tGravityAccMag-arCoeff()4': [],
    'tBodyAccJerkMag-mean()': [],
    'tBodyAccJerkMag-std()': [],
    'tBodyAccJerkMag-mad()': [],
    'tBodyAccJerkMag-max()': [],
    'tBodyAccJerkMag-min()': [],
    'tBodyAccJerkMag-sma()': [],
    'tBodyAccJerkMag-energy()': [],
    'tBodyAccJerkMag-iqr()': [],
    'tBodyAccJerkMag-entropy()': [],
    'tBodyAccJerkMag-arCoeff()1': [],
    'tBodyAccJerkMag-arCoeff()2': [],
    'tBodyAccJerkMag-arCoeff()3': [],
    'tBodyAccJerkMag-arCoeff()4':[],
    'fBodyAcc-mean()-X':[], 
    'fBodyAcc-mean()-Y':[],
    'fBodyAcc-mean()-Z':[],
    'fBodyAcc-std()-X':[],
    'fBodyAcc-std()-Y':[],
    'fBodyAcc-std()-Z':[],
    'fBodyAcc-mad()-X':[], 
    'fBodyAcc-mad()-Y':[], 
    'fBodyAcc-mad()-Z':[],
    'fBodyAcc-max()-X':[], 
    'fBodyAcc-max()-Y':[], 
    'fBodyAcc-max()-Z':[],
    'fBodyAcc-min()-X':[],
    'fBodyAcc-min()-Y':[], 
    'fBodyAcc-min()-Z':[],
    'fBodyAcc-sma()':[], 
    'fBodyAcc-energy()-X':[], 
    'fBodyAcc-energy()-Y':[],
    'fBodyAcc-energy()-Z':[], 
    'fBodyAcc-iqr()-X':[], 
    'fBodyAcc-iqr()-Y':[],
    'fBodyAcc-iqr()-Z':[], 
    'fBodyAcc-entropy()-X':[], 
    'fBodyAcc-entropy()-Y':[],
    'fBodyAcc-entropy()-Z':[], 
    'fBodyAcc-maxInds-X':[]
    # 'fBodyAcc-maxInds-Y':[],
    # 'fBodyAcc-maxInds-Z':[], 
    # 'fBodyAcc-meanFreq()-X':[], 
    # 'fBodyAcc-meanFreq()-Y':[],
    # 'fBodyAcc-meanFreq()-Z':[], 
    # 'fBodyAcc-skewness()-X':[], 
    # 'fBodyAcc-kurtosis()-X':[],
    # 'fBodyAcc-skewness()-Y':[], 
    # 'fBodyAcc-kurtosis()-Y':[], 
    # 'fBodyAcc-skewness()-Z':[],
    # 'fBodyAcc-kurtosis()-Z':[], 
    # 'fBodyAcc-bandsEnergy()-1,8':[], 
    # 'fBodyAcc-bandsEnergy()-9,16':[],
    # 'fBodyAcc-bandsEnergy()-17,24':[], 
    # 'fBodyAcc-bandsEnergy()-25,32':[], 
    # 'fBodyAcc-bandsEnergy()-33,40':[],
    # 'fBodyAcc-bandsEnergy()-41,48':[], 
    # 'fBodyAcc-bandsEnergy()-49,56':[], 
    # 'fBodyAcc-bandsEnergy()-57,64':[],
    # 'fBodyAcc-bandsEnergy()-1,16':[], 
    # 'fBodyAcc-bandsEnergy()-17,32':[], 
    # 'fBodyAcc-bandsEnergy()-33,48':[],
    # 'fBodyAcc-bandsEnergy()-49,64':[], 
    # 'fBodyAcc-bandsEnergy()-1,24':[], 
    # 'fBodyAcc-bandsEnergy()-25,48':[],
    # 'fBodyAcc-bandsEnergy()-1,8':[], 
    # 'fBodyAcc-bandsEnergy()-9,16':[], 
    # 'fBodyAcc-bandsEnergy()-17,24':[],
    # 'fBodyAcc-bandsEnergy()-25,32':[], 
    # 'fBodyAcc-bandsEnergy()-33,40':[], 
    # 'fBodyAcc-bandsEnergy()-41,48':[],
    # 'fBodyAcc-bandsEnergy()-49,56':[], 
    # 'fBodyAcc-bandsEnergy()-57,64':[], 
    # 'fBodyAcc-bandsEnergy()-1,16':[],
    # 'fBodyAcc-bandsEnergy()-17,32':[], 
    # 'fBodyAcc-bandsEnergy()-33,48':[], 
    # 'fBodyAcc-bandsEnergy()-49,64':[],
    # 'fBodyAcc-bandsEnergy()-1,24':[], 
    # 'fBodyAcc-bandsEnergy()-25,48':[], 
    # 'fBodyAccJerk-mean()-X':[],
    # 'fBodyAccJerk-mean()-Y':[],
    # 'fBodyAccJerk-mean()-Z':[],
    # 'fBodyAccJerk-std()-X':[],
    # 'fBodyAccJerk-std()-Y':[],
    # 'fBodyAccJerk-std()-Z':[],
    # 'fBodyAccJerk-mad()-X':[],
    # 'fBodyAccJerk-mad()-Y':[],
    # 'fBodyAccJerk-mad()-Z':[],
    # 'fBodyAccJerk-max()-X':[],
    # 'fBodyAccJerk-max()-Y':[],
    # 'fBodyAccJerk-max()-Z':[],
    # 'fBodyAccJerk-min()-X':[],
    # 'fBodyAccJerk-min()-Y':[],
    # 'fBodyAccJerk-min()-Z':[],
    # 'fBodyAccJerk-sma()':[],
    # 'fBodyAccJerk-energy()-X':[],
    # 'fBodyAccJerk-energy()-Y':[],
    # 'fBodyAccJerk-energy()-Z':[],
    # 'fBodyAccJerk-iqr()-X':[],
    # 'fBodyAccJerk-iqr()-Y':[],
    # 'fBodyAccJerk-iqr()-Z':[],
    # 'fBodyAccJerk-entropy()-X':[],
    # 'fBodyAccJerk-entropy()-Y':[],
    # 'fBodyAccJerk-entropy()-Z':[],
    # 'fBodyAccJerk-maxInds-X':[],
    # 'fBodyAccJerk-maxInds-Y':[],
    # 'fBodyAccJerk-maxInds-Z':[],
    # 'fBodyAccJerk-meanFreq()-X':[],
    # 'fBodyAccJerk-meanFreq()-Y':[],
    # 'fBodyAccJerk-meanFreq()-Z':[],
    # 'fBodyAccJerk-skewness()-X':[],
    # 'fBodyAccJerk-kurtosis()-X':[],
    # 'fBodyAccJerk-skewness()-Y':[],
    # 'fBodyAccJerk-kurtosis()-Y':[],
    # 'fBodyAccJerk-skewness()-Z':[],
    # 'fBodyAccJerk-kurtosis()-Z':[],
    # 'fBodyAccJerk-bandsEnergy()-1,8':[],
    # 'fBodyAccJerk-bandsEnergy()-9,16':[],
    # 'fBodyAccJerk-bandsEnergy()-17,24':[],
    # 'fBodyAccJerk-bandsEnergy()-25,32':[],
    # 'fBodyAccJerk-bandsEnergy()-33,40':[],
    # 'fBodyAccJerk-bandsEnergy()-41,48':[],
    # 'fBodyAccJerk-bandsEnergy()-49,56':[],
    # 'fBodyAccJerk-bandsEnergy()-57,64':[],
    # 'fBodyAccJerk-bandsEnergy()-1,16':[],
    # 'fBodyAccJerk-bandsEnergy()-17,32':[],
    # 'fBodyAccJerk-bandsEnergy()-33,48':[],
    # 'fBodyAccJerk-bandsEnergy()-49,64':[],
    # 'fBodyAccJerk-bandsEnergy()-1,24':[],
    # 'fBodyAccJerk-bandsEnergy()-25,48':[],
    # 'fBodyAccJerk-bandsEnergy()-1,8':[],
    # 'fBodyAccJerk-bandsEnergy()-9,16':[],
    # 'fBodyAccJerk-bandsEnergy()-17,24':[],
    # 'fBodyAccJerk-bandsEnergy()-25,32':[],
    # 'fBodyAccJerk-bandsEnergy()-33,40':[],
    # 'fBodyAccJerk-bandsEnergy()-41,48':[],
    # 'fBodyAccJerk-bandsEnergy()-49,56':[],
    # 'fBodyAccJerk-bandsEnergy()-57,64':[],
    # 'fBodyAccJerk-bandsEnergy()-1,16':[],
    # 'fBodyAccJerk-bandsEnergy()-17,32':[],
    # 'fBodyAccJerk-bandsEnergy()-33,48':[],
    # 'fBodyAccJerk-bandsEnergy()-49,64':[],
    # 'fBodyAccJerk-bandsEnergy()-1,24':[],
    # 'fBodyAccJerk-bandsEnergy()-25,48':[],
    # 'fBodyAccJerk-bandsEnergy()-1,8':[],
    # 'fBodyAccJerk-bandsEnergy()-9,16':[],
    # 'fBodyAccJerk-bandsEnergy()-17,24':[],
    # 'fBodyAccJerk-bandsEnergy()-25,32':[],
    # 'fBodyAccJerk-bandsEnergy()-33,40':[],
    # 'fBodyAccJerk-bandsEnergy()-41,48':[],
    # 'fBodyAccJerk-bandsEnergy()-49,56':[],
    # 'fBodyAccJerk-bandsEnergy()-57,64':[],
    # 'fBodyAccJerk-bandsEnergy()-1,16':[],
    # 'fBodyAccJerk-bandsEnergy()-17,32':[],
    # 'fBodyAccJerk-bandsEnergy()-33,48':[],
    # 'fBodyAccJerk-bandsEnergy()-49,64':[],
    # 'fBodyAccJerk-bandsEnergy()-1,24':[],
    # 'fBodyAccJerk-bandsEnergy()-25,48':[],
    # 'fBodyAccMag-mean()':[],
    # 'fBodyAccMag-std()':[],
    # 'fBodyAccMag-mad()':[],
    # 'fBodyAccMag-max()':[],
    # 'fBodyAccMag-min()':[],
    # 'fBodyAccMag-sma()':[],
    # 'fBodyAccMag-energy()':[],
    # 'fBodyAccMag-iqr()':[],
    # 'fBodyAccMag-entropy()':[],
    # 'fBodyAccMag-maxInds':[],
    # 'fBodyAccMag-meanFreq()':[],
    # 'fBodyAccMag-skewness()':[],
    # 'fBodyAccMag-kurtosis()':[],
    # 'fBodyBodyAccJerkMag-mean()':[],
    # 'fBodyBodyAccJerkMag-std()':[],
    # 'fBodyBodyAccJerkMag-mad()':[],
    # 'fBodyBodyAccJerkMag-max()':[],
    # 'fBodyBodyAccJerkMag-min()':[],
    # 'fBodyBodyAccJerkMag-sma()':[],
    # 'fBodyBodyAccJerkMag-energy()':[],
    # 'fBodyBodyAccJerkMag-iqr()':[],
    # 'fBodyBodyAccJerkMag-entropy()':[],
    # 'fBodyBodyAccJerkMag-maxInds':[],
    # 'fBodyBodyAccJerkMag-meanFreq()':[],
    # 'fBodyBodyAccJerkMag-skewness()':[],
    # 'fBodyBodyAccJerkMag-kurtosis()':[],
    # 'angle(tBodyAccMean,gravity)':[],
    # 'angle(tBodyAccJerkMean,gravityMean)':[],
    # 'angle(X,gravityMean)':[],
    # 'angle(Y,gravityMean)':[],
    # 'angle(Z,gravityMean)':[]
}



# with open("/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/featuresAcc.txt", "r") as f:
#     lines = f.readlines()
# with open("/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/features1.txt", "w") as f:
#     for line in lines:
#         element = line[3:]
#         print(element)
#         f.write("'{0}'".format(element))
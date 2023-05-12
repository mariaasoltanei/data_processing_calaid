import numpy as np
import pandas as pd
from sklearn import utils, metrics, svm

#total acc https://physics.stackexchange.com/questions/41653/how-do-i-get-the-total-acceleration-from-3-axes
def read_data(file):
    df = pd.read_csv(file)
    df = utils.shuffle(df)
    keep_columns = ['A', 'C', 'E', 'F', 'G']
    xData = df.drop(['Participant no.', 'Activity', 'ActivityName'], axis=1)
    yData = df.ActivityName
    
    return np.array(xData), np.array(yData)


train_X, train_y = read_data('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/modeled_csv/train_data.csv')
test_X, test_y = read_data('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/modeled_csv/test_data.csv')
print("Train data shape:", train_X.shape, train_y.shape)
print("Test data shape:", test_X.shape, test_y.shape)

model = svm.SVC(gamma='scale', probability=True)
model.fit(train_X, train_y)

validation = (test_X, test_y)
# print(validation[0])
y_hat = model.predict(validation[0])
# with np.printoptions(threshold=np.inf):
#     print(y_hat)
accuracy = metrics.accuracy_score(validation[1], y_hat)
print("SVM accuracy is:", accuracy)
cm = metrics.confusion_matrix(validation[1], y_hat)
print(cm)
recall = cm[0][0] / (cm[0][0] + cm[0][1])
precision = cm[0][0] / (cm[0][0] + cm[1][0])
f1 = 2*(precision*recall)/(precision+recall)
print("Recall in SVM:", recall)
print("Precision in SVM", precision)
# print(f"F1 Score in '{model_name}' = {f1}")
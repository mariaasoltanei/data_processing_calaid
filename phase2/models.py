import numpy as np
import pandas as pd
from sklearn import svm, utils, metrics
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier
#for cross validation
def read_data(file):
    df = pd.read_csv(file)
    df = utils.shuffle(df)
    df.dropna()
    print("Null vals - test", sum(df.isnull().values))
    xData = df.drop(['Activity', 'ActivityName'], axis=1)
    yData = df.ActivityName
    
    return np.array(xData), np.array(yData)
def trainModel(train_x, train_y, model_name='NB', validation=None):
    """
    Possible model names: ['NB', 'SVM', 'XGB', 'MLP', 'ADA', 'BAG', 'RF']
    default = 'NB'
    
    validation: (val_x, val_y) tupple for validation accuracy score.
    
    return: trained model
    """
    model = None
    if model_name == 'SVM':
        model = svm.SVC(gamma='scale', probability=True)
    elif model_name == 'MLP':
        model = MLPClassifier(hidden_layer_sizes=(100,100,100), max_iter=800, alpha=0.0001,
                     solver='sgd', verbose=10, tol=0.000000001)
    elif model_name == 'ADA':
        model = AdaBoostClassifier(n_estimators=50)
    elif model_name == 'BAG':
        model = BaggingClassifier(n_jobs=2, n_estimators=50)
    elif model_name == 'RF':
        model = RandomForestClassifier(n_estimators=200, max_depth=10)
    elif model_name == 'KNN':
        model = KNeighborsClassifier(n_neighbors=5, weights='distance', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=None)
    else:
        model = GaussianNB()
    
    model.fit(train_x, train_y)
    
    if validation is not None:
        y_hat = model.predict(validation[0])
        acc = metrics.accuracy_score(validation[1], y_hat)
        print(f"Validation Accuracy in '{model_name}' = {acc}")
        cm = metrics.confusion_matrix(validation[1], y_hat)
        print(cm)
        recall = cm[0][0] / (cm[0][0] + cm[0][1])
        precision = cm[0][0] / (cm[0][0] + cm[1][0])
        f1 = 2*(precision*recall)/(precision+recall)
        print(f"Recall in '{model_name}' = {recall}")
        print(f"Precision in '{model_name}' = {precision}")
        print(f"F1 Score in '{model_name}' = {f1}")
               
    return model
train_X, train_y = read_data('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/data_processing_calaid/phase2/train.csv')
test_X, test_y = read_data('/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/data_processing_calaid/phase2/test.csv')
print()
print("Train data shape:", train_X.shape, train_y.shape)
print("Test data shape:", test_X.shape, test_y.shape)
# print("Null vals - test", sum(testDF.isnull().values))
print(train_y)
model1 = trainModel(train_X, train_y, model_name='RF', validation=(test_X, test_y))

model2 = trainModel(train_X, train_y, model_name='BAG', validation=(test_X, test_y))

model3 = trainModel(train_X, train_y, model_name='SVM', validation=(test_X, test_y))

model4 = trainModel(train_X, train_y, model_name='MLP', validation=(test_X, test_y))

model5 = trainModel(train_X, train_y, model_name='KNN', validation=(test_X, test_y))

# model = svm.SVC(gamma='scale', probability=True)
# model.fit(train_X, train_y)

# validation = (test_X, test_y)
# # print(validation[0])
# y_hat = model.predict(validation[0])
# # with np.printoptions(threshold=np.inf):
# #     print(y_hat)
# accuracy = metrics.accuracy_score(validation[1], y_hat)
# print("SVM accuracy is:", accuracy)
# cm = metrics.confusion_matrix(validation[1], y_hat)
# print(cm)
# recall = cm[0][0] / (cm[0][0] + cm[0][1])
# precision = cm[0][0] / (cm[0][0] + cm[1][0])
# f1 = 2*(precision*recall)/(precision+recall)
# print("Recall in SVM:", recall)
# print("Precision in SVM", precision)
# # print(f"F1 Score in '{model_name}' = {f1}")
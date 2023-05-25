import pymongo
from datetime import datetime, timedelta
import certifi
from app import mongo
import joblib
import pandas as pd
ca = certifi.where()
from getActivity import getActivity, prepareData, calculateCalories
model = joblib.load("/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/data_processing_calaid/flask_server/linearsvc.pkl")
print((prepareData("6414e7b4911b2b5943024071", "2023-05-20 01:41:30.733000")))
# print(calculateCalories(activity, userWeight))



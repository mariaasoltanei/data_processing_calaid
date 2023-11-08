from app import app, mongo
from getActivity import prepareData, getActivity,calculateCalories, addToDatabase
from getTDEE import getTDEE, addActivityMultiplierDB
import certifi
from flask import jsonify, request
ca = certifi.where()
import joblib

model = joblib.load("linearsvc.pkl")

@app.route('/calories/<userId>', methods=['POST'])
def getCalories(userId):
    if request.method == 'POST':
        jsonTimestamp = request.get_json()
        timestamp = jsonTimestamp['timestamp']
        userWeight = jsonTimestamp['userWeight']
        activity = getActivity(prepareData(userId, timestamp), model)
        calories = calculateCalories(activity, userWeight)
        print(activity, calories)
        data = {
            "activity": activity,
            "calories": calories
        }
        addToDatabase(userId, timestamp, activity, calories)
        return jsonify(data)

@app.route('/activityMultiplier/<userId>', methods=['POST'])
def getActivityMultiplier(userId):
    if request.method == 'POST':
        jsonTimestamp = request.get_json()
        timestamp = jsonTimestamp['timestamp']
        currentBMR = jsonTimestamp['currentBMR']
        activityMultiplier = getTDEE(timestamp, userId, currentBMR)
        addActivityMultiplierDB(userId, activityMultiplier)
        totalCalories = currentBMR * activityMultiplier
        data = {
            "TDEE": totalCalories,
        }
        return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
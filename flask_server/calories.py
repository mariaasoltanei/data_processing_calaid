from app import app, mongo
from getActivity import prepareData, getActivity,calculateCalories
import certifi
from flask import jsonify, request
ca = certifi.where()
import joblib

model = joblib.load("C:\\Users\\sltnm\\Desktop\\FACULTATE\\LICENTA\\data_processing_calaid\\flask_server\\linearsvc.pkl")

@app.route('/calories/<userId>', methods=['POST'])
def getCalories(userId):
    if request.method == 'POST':
        print("USER ID", userId)
        jsonTimestamp = request.get_json()
        timestamp = jsonTimestamp['timestamp']
        userWeight = jsonTimestamp['userWeight']
        print(jsonTimestamp['timestamp'])
        print(userWeight)
        activity = getActivity(prepareData(userId, timestamp), model)
        calories = calculateCalories(activity, userWeight)
        print(activity, calories)
        data = {
            "activity": activity,
            "calories": calories
        }
        return jsonify(data)


@app.route('/test/<userId>', methods=['POST'])
def test(userId):
    if request.method == 'POST':
        print("USER ID", userId)
        jsonTimestamp = request.get_json()
        userWeight = jsonTimestamp['userWeight']
        print(jsonTimestamp['timestamp'])
        print(userWeight)
        data = {
            "activity": "hellow world",
        }
        return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
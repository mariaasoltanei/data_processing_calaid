from app import app, mongo
from getCalories import getActivityDetails
import certifi
from flask import jsonify, request
import time
ca = certifi.where()


@app.route('/calories/<userId>', methods=['POST'])
def getCalories(userId):
    if request.method == 'POST':
        print("USER ID", userId)
        jsonTimestamp = request.get_json()
        timestamp = jsonTimestamp['timestamp']
        print(jsonTimestamp['timestamp'])
        print(type(jsonTimestamp['timestamp']))
           #calories, speed, activityDurationMins = getActivityDetails(userId)
        calories, speed = getActivityDetails(userId, timestamp)
        
        print("Calories", calories)
        print("Speed", speed)
        data = {
            "calories": calories,
            "speed": speed
        }
        return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
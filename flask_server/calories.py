from app import app, mongo
from getCalories import getActivityDetails
import certifi
from flask import jsonify, request
import time
ca = certifi.where()

#ruta sa fie in functie de user id
@app.route('/calories/<userId>', methods=['GET', 'POST'])
def getCalories(userId):
    if request.method == 'POST':
           noSteps = request.args.get("noSteps")
           calories, speed, activityDurationMins = getActivityDetails(userId)
    else:
        calories, speed, activityDurationMins = getActivityDetails(userId)
        data = {
            "calories": calories,
            "speed": speed,
            "activityDurationMins": activityDurationMins
        }
        return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
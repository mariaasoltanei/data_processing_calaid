import math
import statistics

# Constants
WEIGHT_KG = 70  # User's weight in kg
STRIDE_LENGTH_M = 0.7  # User's stride length in meters
WALKING_SPEED_FREQ_VARIANCE_THRESHOLD = 0.01  # Variance threshold to determine if user is walking

def convertMillis(millis):
    seconds=(millis/1000)%60
    minutes=(millis/(1000*60))%60
    hours=(millis/(1000*60*60))%24
    return hours

def calculate_mets(speed_m_per_min):
    return 0.0272 * speed_m_per_min + 1.2

def calculate_calories_burned(duration_hrs, mets):
    return 1.05 * mets * duration_hrs * WEIGHT_KG

def calculate_speed(x, y, z):
    # Calculate magnitude of acceleration vector
    magnitude = math.sqrt(x**2 + y**2 + z**2)

    # Convert magnitude to speed (m/min)
    speed_m_per_min = magnitude * STRIDE_LENGTH_M * 60

    return speed_m_per_min

def determine_activity_type(speeds_m_per_min):
    # Determine if user is walking or running based on variance of speeds
    speed_var = statistics.variance(speeds_m_per_min)
    if speed_var < WALKING_SPEED_FREQ_VARIANCE_THRESHOLD:
        return 'walking'
    else:
        return 'running'

# Example accelerometer data
accel_data = [
    [1.2, 0.5, 0.9, 1627542050],  # X, Y, Z axis values and timestamp at time t=0
    [1.5, 0.3, 1.1, 1627542051],  # X, Y, Z axis values and timestamp at time t=1
    [1.3, 0.4, 0.8, 1627542052],  # X, Y, Z axis values and timestamp at time t=2
    [1.6, 0.2, 0.9, 1627542053],  # X, Y, Z axis values and timestamp at time t=3
    [1.4, 0.3, 1.2, 1627542054],  # X, Y, Z axis values and timestamp at time t=4
    [1.2, 0.5, 1.1, 1627542055],  # X, Y, Z axis values and timestamp at time t=5
    [1.3, 0.6, 0.9, 1627542056],  # X, Y, Z axis values and timestamp at time t=6
    [1.1, 0.4, 1.0, 1627542057],  # X, Y, Z axis values and timestamp at time t=7
    [1.5, 0.2, 1.1, 1627542058],  # X, Y, Z axis values and timestamp at time t=8
    [1.7, 0.3, 0.9, 1627542059],  # X, Y, Z axis values and timestamp at time t=9
]
duration_hrs = convertMillis(accel_data[len(accel_data)-1][3]- accel_data[0][3])  # Duration in hours
print(duration_hrs)

# Calculate speed for each time point
speeds_m_per_min = []
for i in range(len(accel_data)-1):
    x1, y1, z1, t1 = accel_data[i]
    x2, y2, z2, t2 = accel_data[i+1]
    print(t1)

    # Calculate time difference in minutes
    time_diff = (t2 - t1) / 60

    # Calculate speed
    # Calculate speed
    speed_m_per_min = calculate_speed(x2-x1, y2-y1, z2-z1)

    # Append speed to list of speeds
    speeds_m_per_min.append(speed_m_per_min)

# Determine if user is walking or running
activity_type = determine_activity_type(speeds_m_per_min)

# Calculate METS
if activity_type == 'walking':
    speed_m_per_min = math.mean(speeds_m_per_min)  # Calculate average speed for walking
mets = calculate_mets(speed_m_per_min)

# Calculate calories burned
calories_burned = calculate_calories_burned(duration_hrs, mets)

print(f"Activity type: {activity_type}")
print(f"Speed: {speed_m_per_min:.2f} m/min")
print(f"METS: {mets:.2f}")
print(f"Calories burned: {calories_burned:.2f} calories")

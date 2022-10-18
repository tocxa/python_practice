from datetime import datetime

system_time = datetime.now()  # getting all system time info
currentHour = system_time.hour  # getting current hour in int

if 4 < currentHour < 11:  # elif to determine current time of day based on hour
    timeOfDay = "morning"
elif 11 <= currentHour < 16:
    timeOfDay = "day"
elif 16 <= currentHour < 21:
    timeOfDay = "evening"
else:
    timeOfDay = "night"

print("Good " + timeOfDay + ", world!")  # printing it to console

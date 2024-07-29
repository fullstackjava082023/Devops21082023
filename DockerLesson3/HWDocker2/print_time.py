from datetime import datetime

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
day_of_week = datetime.now().strftime("%A")
print("today is:",time)
print("today :",day_of_week)

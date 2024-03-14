import datetime

# date = datetime.date(2022,2,4)
# print(date)
#
# today = datetime.date.today()
# print(today)
#
# if today > date:
#     print("the date is smaller than today")
#
# # difference in years between date and today
# print(abs(date.year - today.year))
#

#############################
#### input date and check difference between today and the date in days.
day = int(input("enter the day: "))
month = int(input("enter the month "))
year = int(input("enter the year "))
input_date = datetime.date(year,month,day)
today = datetime.date.today()

print(abs((input_date - today).days))




from datetime import datetime
year = int(input("please enter which year you were born: "))
month = int(input("please enter which month you were born: "))
day = int(input("please enter which day you were born: "))

my_date = datetime(year, month, day)
week_day = my_date.weekday()
if week_day == 0:
    print("monday")
elif week_day == 1:
    print("tuesday")
elif week_day == 2:
    print("wednesday")
elif week_day == 3:
    print("thursday")
elif week_day == 4:
    print("friday")
elif week_day == 5:
    print("saturday")
else:
    print("sunday")

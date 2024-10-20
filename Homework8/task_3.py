input_date = input("Please enter date: ")

regex = input_date[-6]
date_part, time_part = input_date.split("T")
year_part, month_part, day_part = date_part.split("-", 2)
clock_part, timezone_part = time_part.split(regex)
hour_part, minute_part, seconds_part = clock_part.split(":", 2)
just_seconds_part, ms_part = seconds_part.split(".")
timezone_hour_part, timezone_minute_part = timezone_part.split(":")

hour_part = int(hour_part)
if(hour_part > 12):
    hour_part -= 12


print(f"{day_part}-{month_part}-{year_part} {hour_part}:{minute_part}:{just_seconds_part}{regex}{int(timezone_hour_part)}")
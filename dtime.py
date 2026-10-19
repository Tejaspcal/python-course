from datetime import date, time, datetime

d_day = date.today()
now_for_on = datetime.now()
print("Today's date is:", d_day)
print("\nCurrent time is:", now_for_on)

print("\nCurrent components:", d_day.year, d_day.month, d_day.day)
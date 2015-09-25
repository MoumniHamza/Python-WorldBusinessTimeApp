from geopy import geocoders # $ pip  install geopy
import calendar
from datetime import datetime
import pytz # $ pip install pytz
g = geocoders.GoogleV3()
print(" I need some information from you to proceed ")
ask = input( "Which city do you live in now?:   ")
place, (lat, lng) = g.geocode(ask)
timezone = g.timezone((lat, lng)) # return pytz timezone object
print(timezone.zone)
now = datetime.now(timezone) 
weekday = now.weekday() 
print(calendar.day_name[weekday])
print(now)
if now.hour > 21 or now.hour < 9:
    print("sorry we are closed, we will be open in: " , 9 - now.hour , "Hours")
else:
    print(" We are open")

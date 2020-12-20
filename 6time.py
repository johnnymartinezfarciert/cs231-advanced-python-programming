import time
import datetime

# Produce a weekly calendar of the current year
thisYear = datetime.date.today().year
today = datetime.date(thisYear,1,1)

#Loop over the days in the year, splitting them into weeksself.
print( ' ' * (1+today.weekday()), end='' )
while today < datetime.date(thisYear+1,1,1):
    print( '{:2}'.format(today.day), end=' ' if 5 !=today.weekday() else '\n' )
    today += datetime.timedelta(1)
print()

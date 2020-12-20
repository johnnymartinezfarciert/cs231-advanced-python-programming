from datetime import datetime
import time


log = '/etc/httpd/logs/access_log'

#### GENERATOR ####
def midnight_gen():
    for line in open(log):
        date = line.split(" ")[3].split("[")[1].split(":")[0]
        log_time = ':'.join(line.split(" ")[3].split("[")[1].split(":")[1:4])
        FMT = '%H:%M:%S' # time format to be passed into datetime.strptime()

        # when you subtract two datetime objects you get a datetime.timedelta object
        # datetime.strptime(timeString, format) returns datetime object
        tdelta = datetime.strptime(log_time, FMT) - datetime.strptime('00:00:00', FMT)

        # now we can call timedelta's total_secods() method
        total_seconds = tdelta.total_seconds()
        msg = "Date: " + date + " | Seconds since midnight : " + "%d" % total_seconds
        yield msg
#### END OF GENERATOR ####

#instantiate generator
a = midnight_gen()

# keep looping through values at users request
i = 'y'
while (i == 'y'):
    print('Calculating seconds since midnight for events in access_log...')
    time.sleep(1)
    print('...')
    time.sleep(.5)
    for _ in range(10):
      try:
        print (next(a))
      except stopIterationError:
        print('you have reached the restaurant at the end of the universe, goodbye')
        break;
      time.sleep(.1)
    i = input("type 'y' to print more:  ")

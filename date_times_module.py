'''/home/ivar/Desktop/python/Chambucket'''
import os
import datetime
os.chdir('/home/ivar/Desktop/python/Chambucket')
gvn = datetime.date(1956, 1 ,31)
print(gvn)
print(gvn.year)
print(gvn.month)
print(gvn.day)

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill+dt)

print(gvn.strftime('%A, %B, %d, %Y'))
msg = 'GVR was born on {:%A, %B, %d, %Y}.'
print(msg.format(gvn))

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)

print(launch_time.minute)

now = datetime.datetime.today()
print(now)
print(now.microsecond)

moon_loading = '7/20/1969'
moon_loading_datetime = datetime.datetime.strptime(moon_loading, '%m/%d/%Y')
print(moon_loading_datetime)

import datetime
import pytz

d = datetime.date(2016, 7, 24)
print(d)
tday = datetime.date.today()
print(tday.year)
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)

#date2 = datel + timedelta
#timedelta = date1 + date2

bday = datetime.date(2016, 9, 24)

till_bday = bday - tday

print(till_bday.total_seconds())

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt.year)

tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

dt1 = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt1)

dt1_now = datetime.datetime.now(tz=pytz.UTC)
print(dt1_now)

dt1_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt1_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

#for tz in pytz.all_timezones:
#    print(tz)

dt_mtn = datetime.datetime.now()
mtn_tz= pytz.timezone('US/Mountain')

dt_mtn = mtn_tz.locallize(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_eas)
dt_east = dt+mtn.astimezone(pytz.timezone('US/Eastern'))

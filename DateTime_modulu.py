from datetime import date , time ,datetime
from datetime import timedelta


result= dir(datetime)
simdi =datetime.now()
result = simdi.day
result = simdi.hour
result = simdi.second
result = simdi.minute

result = datetime.ctime(simdi)
result = datetime.strftime(simdi , "%Y" " " "%B" " " "%A" " " "%d" " " "%X")
result = datetime.strftime(simdi, "%H:%M:%S")
print(result)

"""
%Y = year
%B = month
%A = day
%m = month
%d = day
%H = hour
%M = minute
%S = second

"""
t = "24 Mayıs 2003"
gun , ay ,yil = t.split() 
print(gun)
print(ay)
print(yil)

d = "15 April 2019 hour 10:45:03"
dt = datetime.strptime(d, "%d %B %Y hour %H:%M:%S")
print(dt)

birtday = datetime(2003,5,24,14,50,32)
print(birtday)

sonuc = datetime.timestamp(birtday) # saniye cinsinden tarihi verir
result = datetime.fromtimestamp(sonuc) # saniyeyi normal bir tarihe çevirir
result = datetime.fromtimestamp(0)#bilgisayarlarda varsayılan başlangıç değeri
print(result)

result = simdi - birtday #timedelta()
result = simdi + timedelta(days=730)
print(result)
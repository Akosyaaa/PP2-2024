#Ex1
import datetime
x=datetime.datetime.now()-datetime.timedelta(5)

print(x)
#Ex2
import datetime
x=datetime.datetime.now()-datetime.timedelta(1)
y=datetime.datetime.now()
z=datetime.datetime.now()+datetime.timedelta(1)
print(x)
print(y)
print(z)
#Ex3
import datetime

dt=datetime.datetime.today().replace(microsecond=0)
print(dt)
#Ex4
from datetime import datetime,time
def datetipe(dt1,dt2):
    timedelta=dt2-dt1
    return timedelta.days*24*3600+timedelta.seconds
date1=datetime.strptime('2024-02-21 12:00:00','%Y-%m-%d %H:%M:%S')
date2=datetime.now()
print("\n%d seconds"%(datetipe(date1,date2)))
print()

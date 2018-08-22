import bind.trygopy
import datetime

start = datetime.datetime.now()
print(bind.trygopy.HeavyCalc(800000))
print(datetime.datetime.now()-start)
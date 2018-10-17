days = int(input("geef aantal dagen"))*60*60*24
uren = int(input("geef aantal uren"))*60*60
minuten = int(input("geef aantal minuten"))*60
seconds = int(input("geef aantal seconden"))

time = days + uren + minuten+ seconds

print("aantal seconden:{0}".format(time))

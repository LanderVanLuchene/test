import calendar

y = int(input("geef een jaartal op"))
m = int(input("geef een maand op"))

print("dit is de kalender: {0}".format(calendar.month(y, m)))
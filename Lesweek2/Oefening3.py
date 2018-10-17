#namespace aanmaken via from
from datetime import datetime
limit = datetime.now().year -18
birthdate = int(input("geef jouw geboortejaar"))

if (birthdate > limit):
    print("je bent nog te jong")
else:
    print("welkom")
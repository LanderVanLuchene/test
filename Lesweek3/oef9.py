import random
n = 20
gok = -1
getal = int(random.random() * n)

while (gok != getal):
    gok = int(input("geef een gok tussen 0en 20."))
    if(gok > getal):
        print("het getal is kleiner")
    elif(gok < getal):
        print("het getal is groter")
    else:
        print("u hebt goed gegokt")
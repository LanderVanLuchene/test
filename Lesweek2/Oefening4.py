dogAge = int(input("Geef de leeftijd van uw hond."))
if (dogAge == 1):
    print("14 mensenjaren")
elif (dogAge == 2):
    print("22 mensenjaren")
else:
    print("{0} mensenjaren".format((22 + (dogAge - 2)* 5)))
from math import floor, ceil
score = float(input("Geef je score op."))

print(round(score))
decimalPartOfScore = score - int(score)
if (decimalPartOfScore <= 0.5):
    score = math.floor(score)
    #floor rond af naar beneden.
    #ceil rond af naar boven
    #round rond af maar dat zoude beter nog keer opzoeken.

else:
    score = math.ceil(score)

print("jouw score: {0}".format(score))
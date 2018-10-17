naam = input("ggef uw naam op")
voornaam = input("geef uw voornaam")
datum = input("geef uw bday op (dd-mm-yyyy")

def genereer_paswoord(naam, voornaam, datum):
    wachtwoord = naam.lower() [0:3] + voornaam.upper() [0:2] + datum [3:5] + datum [8:]
    return wachtwoord

print(genereer_paswoord(naam, voornaam, datum))

# achternaam = str(input("geef jouw achternaam"))
# voornaam = str(input("geef jouw voornaam"))
# geboortedatum = input("geef jouw geboortedatum (dd-mm-yyyy)")
#
# print(str.lower(achternaam[0:3]) + str.upper(voornaam[0:2]) + int(geboortedatum[0:4]))
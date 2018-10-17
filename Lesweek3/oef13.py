email_adres = input("geef uw email")

def check_email_format(email):
    #kijk af @ bestaat
    position_at = email.find("@")
    if (position_at == -1)
        return False

    #eindigt oop student.howest
    if(email[position_at:+1] != "student.howest.be"):
        return False

    positie_eerste_punt = email[0:position_at].find(".")
    if(positie_eerste_punt == -1): return False
    voornaam= email[positie_eerste_punt+1:position_at]
    if(voornaam == ""): return False
    if(naam == ""): return False

    return True

    if check_email




    return True
if check_email_format(email_adres):
    print("geldig")
else:
    print("ongeldig")
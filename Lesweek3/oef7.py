startwaarde = int(input("Geef een startwaarde."))
stapgrootte = int(input("geef een stapgrootte"))
aantal = int(input("geef het gewenste aantal af te printen getallen"))

def print_lijst_getallen(num1,num2,num3):
    for index in range(num1,num1+(num2*(num3)),num2):
        print(index)

print_lijst_getallen(startwaarde,stapgrootte,aantal)
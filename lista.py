imiona = ["Kasia", "Marysia", "Paula", "Paweł", "Krystian"]


i = 3
while ( i < 4 ):

    imie = input("Podaj imię: ")

    if (imie in imiona):
        print ("Cześć", imie)

    else:
        print ("Nie ma")

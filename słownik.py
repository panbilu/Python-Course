

imie = "Arkadiusz"
wiek = 29
plec = "mężczyzna"

imie2 = 'Wioletta'
wiek2= 23
plec2 = "kobieta"

osoba1 = ("Arkadiusz", 29, "mężczyzna")
osoba2 = ("Wioletta", 23, "mężczyzna")
osoba3 = ("Kuba", 32, "mężczyzna")

listaGosci = {
                ("Arkadiusz", 29, 'mężczyzna'),
                ("Wioletta", 23, "kobieta"),
                ("Kuba", 32, "mężczyzna")
            }


listaGosci2 = {
                ("Arkadiusz", 29, 'mężczyzna'),
                ("Wioletta", 23, "kobieta"),
                ("Kuba", 32, "mężczyzna")
            }

listaGosci3 = listaGosci & listaGosci2

for imie, wiek, plec in listaGosci:
    print ("imię: ", imie)
    print ("wiek: ", wiek)
    print ("plec: ", plec)
    print ("\n")

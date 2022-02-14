SzukanaLiczba = 12
i = 0

print("O jakiej liczbie teraz myślę?")

while i < 10:

    LiczbaUzytkownika = int(input("Podaj liczbę "))
    if ( LiczbaUzytkownika == SzukanaLiczba  ):
        print("Brawo! Właśnie o tej liczbie myślałem!")
        break
    elif ( LiczbaUzytkownika < SzukanaLiczba  ):
        print ( "Niestety ta liczba jest za niska")
        continue
    elif ( LiczbaUzytkownika > SzukanaLiczba  ):
        print ( "Niestety ta liczba jest za wysoka")
        continue

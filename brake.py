szukanaLiczba = 25
i = 0
print ('Właśnie myślę o jakiejś liczbie. Jak myślisz,jaka to liczba?')

while i <10:

    liczbaUzytkownika = int(input('podaj liczbę:'))
    if  ( liczbaUzytkownika == szukanaLiczba):
        print ('Brawo! O tą liczbę mi chodziło!')
        break

    elif ( liczbaUzytkownika > szukanaLiczba ):
        print ('ta liczba jest za duża')
        continue

    elif ( liczbaUzytkownika < szukanaLiczba ):
        print (' ta liczba jest za niska')
        continue
    




    
        

            

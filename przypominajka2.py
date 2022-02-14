i = 5
dzialania = [ '+', '-', '/', '//', '*']



while i < 10:
    wartosc = input( """ Wybierz rodzaj działania: * mnożenie / dzielenie
+ dodawanie - odejmowanie // dzielenie bez reszty
""")
    if not (wartosc in dzialania):
        print ( "nie znam takiego działania")
    else:

        a = int(input( "podaj pierwszą liczbę: "))

        b = int(input ( "podaj drugą liczbę: "))

    
    
        if ( wartosc == '*'):
            print ( a * b)
            
        elif ( wartosc == '/'):
      
            if ( a == 0):
                print ("Cholero nie dziel przez zero!")
            
            
            if ( b == 0):
                print ("Cholero nie dziel przez zero!")
            

            else:
                print(a / b)
            
        elif ( wartosc == '+'):
            print ( a + b)
        
        elif ( wartosc == '-'):
            print ( a - b)
        
        elif ( wartosc == '//'):
      
            if ( a == 0):
                print ("Cholero nie dziel przez zero!")
            
            
            if ( b == 0):
                print ("Cholero nie dziel przez zero!")
            

            else:
                print(a // b)

    
            
        


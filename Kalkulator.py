
i =  5
while (i>4):
    wybór = input ('''Wykonaj $działanie: * mnożenie / dzielenie + dodawanie - odejmowanie
** potęgowanie // dzielenie bez reszty
''')
    a = int(input("pierwsza liczba: "))
    b = int(input('druga liczba:'))

    if (wybór == '*'):
        print ( a * b)
    elif (wybór == '/'):
        if (b == 0):
            print ('nie dziel cholero przez zero')
        elif(a == 0):
            print ('nie dziel cholero przez zero')
        else:
            print ( a / b)

    elif (wybór == '+'):
        print ( a + b)
    elif (wybór == '-'):
        print ( a - b)
    elif (wybór == '**'):
        print ( a ** b)
    elif (wybór == '//'):
        if (b == 0):
            print ('nie dziel cholero przez zero')
        elif(a == 0):
            print ('nie dziel cholero przez zero')
        else:
            print ( a // b)
    else:
        print ( 'wybrałeś niwłaściwe działanie')

    

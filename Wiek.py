print ( 'Hej, jak masz na imię?')

a = input( 'Wpisz imię:')

print ('Miło cię poznać',a)
print ('Ile masz lat?')

b  = int(input('Podaj swój wiek:'))

if (  a[-1] == 'a'):
    mia = 'miała'
elif (  a[-1] != 'a'):
    mia = 'miał'
    

wiekZaRok = b + 1

print ('Za rok będziesz',mia,wiekZaRok,'lat')

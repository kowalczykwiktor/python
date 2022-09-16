#Zadanie 6.1

# -*- coding: utf8 -*-

print("Ile masz lat?")
age = int( input() )
if ( age >= 18 ):
    print("Użytkownik pełnoletni")
else:
    print("Użytkownik niepełnoletni")
    print("Do 18 urodzin zostało:", 18 - age, "lat")

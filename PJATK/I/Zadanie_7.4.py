#Zadanie 7.4

# -*- coding: utf8 -*-

numer = int(input("Podaj liczbę:\n"))
for n in range(1, 2):
    if numer % 3 == 0:
        print("Podana liczba jest wielokrotnością liczby 3")
    elif numer % 4 == 0:
        print("Liczba jest wielokrotnością liczby 4")
    elif numer % 3 == 0 and numer % 4 == 0:
        print("Podana liczba jest wielokrotnością liczby 3 i 4")
    else:
        print("Podana liczba nie jest wielokrotnością liczby 3 i 4")
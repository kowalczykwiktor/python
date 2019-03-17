#Zadanie 7.6

# -*- coding: utf8 -*-

szerokosc = 80
print("-" * szerokosc)
for wiersze in range (1, 11):
    for kolumny in range (1, 11):
        print(wiersze * kolumny, end="\t")
print("-" * szerokosc)      
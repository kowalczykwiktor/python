#Zadanie 7.3

# -*- coding: utf8 -*-

imie = input("Wprowadz proszę imiona: ")
lista_imion = imie.replace(",", "")
lista_imion = lista_imion.split()
print(lista_imion)

for imie in lista_imion:
    print("Cześć", imie)
#Zadanie 6.4

# -*- coding: utf8 -*-

dict_names = {
    "Anna" : "zenskie",
    "Julia" : "zenskie",
    "Zofia" : "zenskie",
    "Maja" : "zenskie",
    "Hania" : "zenskie",
    "Maria" : "zenskie",
    "Stanisława" : "zenskie",
    "Michał" : "meskie",
    "Antoni" : "meskie",
    "Jan" : "meskie",
    "Franciszek" : "meskie",
    "Piotr" : "meskie",
    "Wiktor" : "meskie",
    "Wawrzyniec" : "meskie"
    }

name = input("Podaj imię: ")

if (name in list(dict_names.keys())):
    print(name, "to imię", dict_names[name])
else:
    print("Nie mamy tego imienia! Dodaj je do zbioru")
    gender = input("To imię męskie czy żeńskie? wpisz m / z: ")
    if (gender == "m"):
        dict_names[name] = "meskie"
    else:
        dict_names[name] = "zenskie"
    print (list(dict_names.keys()))


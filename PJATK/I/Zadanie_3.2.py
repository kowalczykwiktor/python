#Zadanie 3.2 - Lokata

# -*- coding: utf8 -*-

start = float(input("Podaj proszę stan początkowy konta: "))
rate = float(input("Stopa oprocenotowania w skali roku (podaj wartość ułamkową, np.: 1% = 0.01): "))
n = int(input("Liczba lat na lokacie: "))
end = start*(1 + rate*n)

print("Po {} latach twój kapitał będzie wynosił {} zł".format(n, end))
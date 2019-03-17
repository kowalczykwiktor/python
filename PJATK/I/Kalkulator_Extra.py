# -*- coding: utf-8 -*-
print("Witaj w kalkulatorze zapotrzebowania na kalorie dla mężczyzn")
print("Podaj proszę swój wzrost w cm:")
wzrost = input()
print("Podaj teraz swoją wagę w kg:")
waga = input()
print("Pora na wiek! Ile masz lat?")
wiek = input()
print("Jak określasz swój poziom aktywności fizycznej? Wybierze odpowiedni poziom: /n 1: ")
wzrost = 1.7
waga = 63
wiek = 25
s = -161
aktywnosc_fizyczna = 1.6
kalorie = (10 * waga + 6.25 * wzrost - 5 * 25 + s) * aktywnosc_fizyczna
print("Zapotrzebowanie Twojej kobiety na kalorie to:", kalorie)

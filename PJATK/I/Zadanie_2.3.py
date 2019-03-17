#Zadanie 2.3 - KalkulatorZapotrzebowaniaKalorycznegoKOBIETA

# -*- coding: utf8 -*-

weight = float(input("Podaj proszę swoją wagę kg: "))
height = float(input("Podaj proszę swój wzrost w cm: "))
age = int(input("Podaj proszę swój wiek: "))
S = -161
PPM = 10 * weight + 6.25 * height + 5 * age + S

print("Twoje dzienne zapotrzebowanie kaloryczne wynosi:", PPM * 1.6, "kcal")
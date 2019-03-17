#Zadanie 2.2 - KalkulatorBMI2

# -*- coding: utf8 -*-

print("Podaj proszę swoją wagę w kg:")
weight = float(input())
print("Podaj proszę swój wzrost w m:")
height = float(input())
BMI = weight / (height ** 2)
print("Twoje BMI wynosi:", BMI)
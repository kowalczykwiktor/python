#Zadanie 4.2 - Spis oglądanych seriali

# -*- coding: utf8 -*-

serials = {
    'Mr ROBOT' : 9.5,
    'Narcos' : 9.0,
    'Game of Thrones' : 7.2,
    'Peaky Blinders' : 8.7,
    'The Big Bang Theory' : 8,
    'Lucyfer': 8,
    }

print(list(serials.keys()))
print('******************************************')

name = input('Który serial chcesz obejrzeć? ')
print("Wybrany serial {} posiada ocenę {}".format(name, serials[name]))

print('******************************************')
new = input('Jaki serial chcesz dodać do swojej bazy? ')
rating = input('Jaka jest twoja ocena tego serialu ' + new + '? ')
serials[new] = float(rating)

print('******************************************')
print(list(serials.keys())) 
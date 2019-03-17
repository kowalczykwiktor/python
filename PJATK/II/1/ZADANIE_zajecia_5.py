#Zadanie_5

# coding=utf-8
def test(fun, *args):
    print ("".join(['-' for i in range(40)]))
    print (fun.__name__[:-1].upper()+" "+fun.__name__[-1])
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print ("Yes, "+decoded.replace("my","your"))
        else:
            print ("No, "+decoded.replace("my","your").replace("has","has not")+" yet")
    else:
        print ("Is correct? "+ str(res == args[-1]))
    print ("".join(['-' for i in range(40)]))

from random import randint
while True:
    r = randint(1,9)
    try:
        quess = input("Wybierz cyfrę z zakresu 1-9\n")
        num = int(quess)
        if not 0 < num < 10:
            print ("Wybierz cyfrę z zakresu")
            continue
        if num == r:
            print ("Yeah! "+str(r))
            break
        else:
            print ("Sróbuj ponownie")
    except Exception:
        print ("Powinieneś wskazać liczbę całkowitą z zakresu 1-9")
    

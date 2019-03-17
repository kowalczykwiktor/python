#Zadanie_1

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

    
def zadanie1(listObject):
    newList = [listObject[0]]
    for e in listObject:
        if e != newList[-1]:
            newList.append(e)
    return newList
    
test(zadanie1, [1, 2, 3, 3, 5, 68, 68, 24], [1,2,3,5,68,24])

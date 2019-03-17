#Zadanie_3

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


def zadanie3(tupleList):
    #bubble sort
    for n in range(len(tupleList)-1, 0, -1):
        for i in range(n):
            if tupleList[i][-1] > tupleList[i+1][-1]:
                tmp = tupleList[i]
                tupleList[i] = tupleList[i+1]
                tupleList[i+1] = tmp

    return tupleList

test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])

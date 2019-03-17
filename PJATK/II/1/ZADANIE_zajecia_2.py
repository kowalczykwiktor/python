#Zadanie_2

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

def zadanie2(list1, list2):
    newList = []
    for item in list1:
        newList.append(item)
        if len(list2):
            newList.append(list2[0])
            list2.pop(0)
    return(newList)

test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12,'c','5'], [1, 12, 2, 'c', 19, '5', 'dd', ':P', ':('])

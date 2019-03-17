#Zadanie_4

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


def zadanie4(text):
    return " ".join([ s.replace("ok","") for s in text.split("$") if s.startswith("ok") ])

test(zadanie4, "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af", [109, 121, 32, 119, 97, 116, 99, 104, 32, 104, 97, 115, 32, 101, 110, 100, 101, 100])


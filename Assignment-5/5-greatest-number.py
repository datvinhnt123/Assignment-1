def skibidi():
    o=[]

    while True:
        n=(input("Input a number: "))
        for i in n:
            o.append(i)
        if n=="":
            break
    p=sorted(o,reverse=True)
    print(p[:5])
skibidi()
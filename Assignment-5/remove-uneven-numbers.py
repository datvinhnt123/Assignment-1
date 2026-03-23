def even_skibidi(s):
    e=[]
    for i in s:
        b=int(i)
        if b%2==0:
            e.append(i)
    return e
a=["1","2","3","4","5","6"]
print(a)
print(even_skibidi(a))
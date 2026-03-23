def skibidi():
    n=int(input(" is this a prime number?: "))
    if n==1:
        return True
    o=[]
    for i in range(1,n+1):
        if n%i==0:
            e=str(i)
            o.append(e)
    if len(o)==2:
        return True
    else:
        return False
print(skibidi())
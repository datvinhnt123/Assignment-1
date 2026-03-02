o=["1","2","3","4","5","6","7","8","9","10"]
def odd_remove(n):
    a=[]
    for i in range(len(n)):
        if int(n[i])%2==0:
            a.append(n[i])
    print(a)
odd_remove(o)
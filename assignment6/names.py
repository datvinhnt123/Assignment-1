def names():
    e=[]
    while True:
         a = input("enter a name: ")
         if a == "":
             break
         if a in e:
             print("Existing Name")
         else:
             e.append(a)
    print("\n".join(e))
names()
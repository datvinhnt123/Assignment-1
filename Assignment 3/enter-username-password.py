def login():
    while True:
        print("Welcome! Please login to your account! ")
        o=0
        k=0
        while o < 5:
            a = input("Enter your username: ")
            if a != "python":
                print("Please try again")
                o = o + 1
            elif a == "python":
                break
        if o == 5:
            print("Access denied")
            continue
        while k < 5:
            z = input("Enter your password: ")
            if z != "rules":
                print("Please try again")
                k = k + 1
            elif z == "rules":
                break
        if k == 5:
            print("Access denied")
            continue
        if a == "python" and z == "rules":
            print("Welcome!")
            return True
login()




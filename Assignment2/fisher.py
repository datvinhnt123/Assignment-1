def fisher():
    n=float(input("Enter the length of a zander (cm): "))
    if n>=42:
        print("Good job! A",n,"cm zander has been caught")
    elif n <= 0:
        print("Bro, what did you fish? There’s nothing there.")
    else:
        print("This zander is not long enough, need",42-n,"cm to be caught - Released already")

fisher()

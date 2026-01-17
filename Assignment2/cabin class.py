def yn():
    while True:
        answer = str(input("Please confirm your class (Y/N): ")).upper()

        if answer == "Y":
            print("Sure, welcome to our cruise ship trip")
            return True
        elif answer == "N":
            print("Okay, I'll ask again.")
            return False
        else:
            print("Please answer Y or N.")
def cabin():
    while True:
        print("Welcome to the cruise ship tour.")
        print("Please choose your cabin class (LUX, A, B, C): ")

        n = input("Enter your choice: ").upper()

        if n == "LUX":
            print("This class will be an upper-deck cabin with a balcony.")
            if yn():
                break

        elif n == "A":
            print("This class will be above the car deck, equipped with a window.")
            if yn():
                break

        elif n == "B":
            print("This class will be a windowless cabin above the car deck.")
            if yn():
                break

        elif n == "C":
            print("This class will be a windowless cabin below the car deck.")
            if yn():
                break
        else:
            print("Please enter a valid class.")
cabin()
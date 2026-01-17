def heal(gender):
    while True:
        try:
            condition = int(input("What is your hemoglobin value (g/L): "))

            if condition <= 0:
                print("Invalid number. Please enter a positive value.")
                continue

            if gender == "female":
                if 117 <= condition <= 155:
                    print("Your hemoglobin level is normal.")
                elif condition < 117:
                    print("Your level is a bit low and below the normal range.")
                else:
                    print("Your level is a bit high and above the normal range.")

            elif gender == "male":
                if 134 <= condition <= 167:
                    print("Your hemoglobin level is normal.")
                elif condition < 134:
                    print("Your level is a bit low and below the normal range.")
                else:
                    print("Your level is a bit high and above the normal range.")
            break

        except ValueError:
            print("Invalid input. Please enter a number.")
def ask():
    print("Welcome to the hemoglobin monitoring system, where you can assess your body’s condition.")

    while True:
        n = input("Are you male or female? : ").lower()
        if n in ["male", "female"]:
            heal(n)
            break
        else:
            print("Please enter 'male' or 'female'.")
ask()

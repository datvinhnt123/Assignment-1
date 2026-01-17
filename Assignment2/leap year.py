def leap_year():
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This year is a leap year.")
            else:
                print("This year is not a leap year.")
        else:
            print("This year is a leap year.")
    else:
        print("This year is not a leap year.")
leap_year()
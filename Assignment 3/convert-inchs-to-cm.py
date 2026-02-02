def convert_inchs_to_cm():
    while True:
        inchs = float(input("Enter inchs: "))
        if inchs < 0:
            print("Please enter a positive number!")
            break
        cm = inchs * 2.54
        print(cm,"cm")




convert_inchs_to_cm()
def get_digit(prompt, min_val, max_val):
    while True:
        value = input(prompt)
        if not value.isdigit():
            print("Wrong: please enter an integer number.")
            continue

        value = int(value)
        if min_val <= value <= max_val:
            print("Accepted")
            return value
        else:
            print(f"Wrong: number must be from {min_val} to {max_val}.")


def lock():
    # First pin: 3 digits (0–9)
    one = get_digit("The first number of the first pin: ", 0, 9)
    two = get_digit("The second number of the first pin: ", 0, 9)
    three = get_digit("The third number of the first pin: ", 0, 9)

    # Second pin: 4 digits (1–6)
    four = get_digit("The first number of the second pin: ", 1, 6)
    five = get_digit("The second number of the second pin: ", 1, 6)
    six = get_digit("The third number of the second pin: ", 1, 6)
    seven = get_digit("The fourth number of the second pin: ", 1, 6)

    s = 0  # score for first pin
    e = 0  # score for second pin

    # Check first pin
    while True:
        password1 = input("Enter the first pin (3 numbers separated by a space): ")
        parts1 = password1.split()

        if len(parts1) != 3 or not all(p.isdigit() for p in parts1):
            print("Wrong format. Try again.")
            continue

        if [one, two, three] == list(map(int, parts1)):
            print("Passed the first pin")
            s=s+1
            break
        else:
            print("Wrong password.Try again for the first pin.")
            s=0
    # Check second pin
    while True:
        password2 = input("Enter the second pin (4 numbers separated by a space): ")
        parts2 = password2.split()

        if len(parts2) != 4 or not all(p.isdigit() for p in parts2):
            print("Wrong format. Try again.")
            continue

        if [four, five, six, seven] == list(map(int, parts2)):
            e = e+2
            print("Passed the second pin")
            break
        else:
            e=0
            print("Wrong password.Try again for the second pin.")
    # Final result
    total = s + e
    if total == 3:
        print("Correct! Both pins are unlocked.")
    else:
        print("Incorrect combination.")
lock()

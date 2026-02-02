def extract_middle_word():
    a = input("Enter your word: ")
    n = len(a)
    if n % 2 == 1:
        print("Your middle character is:", a[n // 2])
    else:
        print("Your middle characters are:", a[n // 2 - 1], a[n // 2])
extract_middle_word()

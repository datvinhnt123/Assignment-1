def acronym():
    phrase = input("Enter your phrase: ")
    words = phrase.split()
    result = ""

    for word in words:
        result += word[0].upper()

    print(result)
acronym()
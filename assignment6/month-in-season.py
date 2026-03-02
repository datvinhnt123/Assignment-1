def mon():
    seasons = ("winter", "spring", "summer", "autumn")
    while True:
        n = input("Which month? :")
        if n == "":
            break
        if n in ("12", "1", "2"):
            print(seasons[0])
        elif n in ("3", "4", "5"):
            print(seasons[1])
        elif n in ("6", "7", "8"):
            print(seasons[2])
        elif n in ("9", "10", "11"):
            print(seasons[3])
        else:
            print("please enter a valid month from 1-12")
mon()
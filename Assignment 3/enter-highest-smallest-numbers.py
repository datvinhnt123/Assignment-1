def highest_smallest():
    a = []

    while True:
        s = str(input("Enter a number (press Enter to stop): "))
        if s == "":
            break
        a.append(int(s))
    if not a:
        print("No numbers entered!")
        return
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print("The highest number is:", a[-1])
    print("The lowest number is:", a[0])


highest_smallest()

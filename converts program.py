def one():
    talent=float(input("Talent: "))
    tl=talent*20*32*13.3
    pound=float(input("Pound: "))
    pd=pound*32*13.3
    lot=float(input("Lot: "))
    lt=lot*13.3
    grams=tl+pd+lt
    kilograms=int(grams/1000)
    gram=grams-kilograms*1000
    print("The weight in modern units:",kilograms,"kilograms and",f"{gram:.2f}","grams.")
one()
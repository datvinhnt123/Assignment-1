def unit_price(diameter_cm, price_usd):

    radius_cm = diameter_cm / 2
    area_cm2 = 3.1416 * radius_cm ** 2
    area_m2 = area_cm2 / 10000
    return price_usd / area_m2
def pizza():
    d1 = float(input("Enter the diameter of pizza 1 (cm): "))
    p1 = float(input("Enter the price of pizza 1 (USD): "))
    d2 = float(input("Enter the diameter of pizza 2 (cm): "))
    p2 = float(input("Enter the price of pizza 2 (USD): "))
    price1 = unit_price(d1, p1)
    price2 = unit_price(d2, p2)
    print(f"Pizza 1 unit price: {price1:.2f} USD/m²")
    print(f"Pizza 2 unit price: {price2:.2f} USD/m²")
    print("The area calculation is based on π ≈ 3.1416.")
    if price1 < price2:
        print("Pizza 1 provides better value for money.")
    elif price2 < price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same value for money.")
pizza()
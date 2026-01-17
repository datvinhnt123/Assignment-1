print("How long are the length and width of the rectangle?")

z = float(input("Length of rectangle: "))
w = float(input("Width of rectangle: "))

while w >= z:
    print("The width must be less than the length of the rectangle!")
    w = float(input("Width of rectangle: "))

print("So its perimeter is", 2 * (z + w), "and the area is", z * w)



import random
num = random.randint(1, 10)
def random_number(a):
    while True:
        n=int(input("Enter a number: "))
        if n==num:
            print("Correct!")
            break
        if n>num:
            print("Number is greater than the number")
        if n<num:
            print("Number is less than the number")
random_number(num)



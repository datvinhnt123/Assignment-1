import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 2000

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def display(self):
        print("Registration number:", self.registration_number)
        print("Maximum speed:", self.maximum_speed, "km/h")
        print("Current speed:", self.current_speed, "km/h")
        print("Travelled distance:", self.travelled_distance, "km")


reg = input("Registration number enter: ")
max_speed = int(input("Maximum speed: "))
car = Car(reg, max_speed)
i=int(input("How many times have ur car speed changed?:"))
for a in range(i):
    a=int(input("Enter a speed change: "))
    h=float(input("How many hours have u drove in that final speed car?:"))
    car.accelerate(a)
    print("Current speed:",car.current_speed)
    car.drive(h)
print("Final speed:", car.current_speed, "km/h")
car.display()
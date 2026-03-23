class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def display(self):
        print("Registration number:", self.registration_number)
        print("Maximum speed:", self.maximum_speed, "km/h")
        print("Current speed:", self.current_speed,"km/h")
        print("Travelled distance:", self.travelled_distance)
reg = input("Registration number enter: ")
max_speed = int(input("Maximum speed: "))

car = Car(reg, max_speed)
car.display()
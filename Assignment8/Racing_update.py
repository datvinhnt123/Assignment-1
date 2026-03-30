import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        self.hours = 0

    def hour_passes(self):
        self.hours += 1

        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\n--- {self.name} | Hour: {self.hours} ---")
        print(f"{'Reg':<10} {'Max':<10} {'Speed':<10} {'Distance':<15}")

        for car in self.cars:
            print(f"{car.registration_number:<10} "
                  f"{car.maximum_speed:<10} "
                  f"{car.current_speed:<10} "
                  f"{car.travelled_distance:<15}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


cars = []
for i in range(1, 11):
    reg = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))

race = Race("Grand Demolition Derby", 8000, cars)

while not race.race_finished():
    race.hour_passes()

    if race.hours % 10 == 0:
        race.print_status()

race.print_status()
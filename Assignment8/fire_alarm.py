class Elevator:
    def __init__(self):
        self.current_floor = 0

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)
        else:
            print("Already at your floor!")

    def floor_up(self, target_floor):
        while self.current_floor < target_floor:
            self.current_floor += 1
            print("Going up... now at floor", self.current_floor)
        print("Arrived at floor", self.current_floor)

    def floor_down(self, target_floor):
        while self.current_floor > target_floor:
            self.current_floor -= 1
            print("Going down... now at floor", self.current_floor)
        print("Arrived at floor", self.current_floor)


class Building:
    def __init__(self, lowest_floor, highest_floor, number_of_elevators):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.elevators = []

        for i in range(number_of_elevators):
            self.elevators.append(Elevator())
    def fire_alarm(self):
        print("\n🔥 FIRE ALARM ACTIVATED! Moving all elevators to bottom floor...\n")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i} going to bottom floor ({self.lowest_floor})")
            elevator.go_to_floor(self.lowest_floor)


    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Invalid elevator number!")
            return

        if target_floor < self.lowest_floor or target_floor > self.highest_floor:
            print("Invalid floor!")
            return

        print(f"\nRunning elevator {elevator_number} to floor {target_floor}")
        self.elevators[elevator_number].go_to_floor(target_floor)


# MAIN PROGRAM
building = Building(0, 10, 3)

building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.run_elevator(2, 3)
building.run_elevator(0, 2)
building.fire_alarm()
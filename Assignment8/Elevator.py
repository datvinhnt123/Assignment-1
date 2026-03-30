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


# test
elevator = Elevator()
elevator.go_to_floor(5)
elevator.go_to_floor(2)
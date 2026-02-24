import random
import time

class Environment:
    def __init__(self):
        self.rooms = {
            'A': random.choice(['Clean', 'Dirty']),
            'B': random.choice(['Clean', 'Dirty'])
        }

    def get_status(self, location):
        return self.rooms[location]

    def clean_room(self, location):
        self.rooms[location] = 'Clean'

    def random_dirt(self):
        if random.random() < 0.3:  # 30% chance
            room = random.choice(['A', 'B'])
            self.rooms[room] = 'Dirty'

    def display(self):
        print(f"Room Status -> A: {self.rooms['A']} | B: {self.rooms['B']}")


class VacuumCleaner:
    def __init__(self, location='A'):
        self.location = location

    def move(self):
        if self.location == 'A':
            self.location = 'B'
        else:
            self.location = 'A'

def run_simulation():
    env = Environment()
    vacuum = VacuumCleaner()

    print("Vacuum Cleaner Simulation Started...\n")

    while True:
        current_status = env.get_status(vacuum.location)

        print(f"Robot Location: {vacuum.location}")
        print(f"Perception: {current_status}")

        if current_status == 'Dirty':
            print("Action: Suck")
            env.clean_room(vacuum.location)

            vacuum.move()
            print("Action: Move")

        else:
            print("Action: Move")
            vacuum.move()

        env.random_dirt()

        env.display()
        print("----------------------------------")

        time.sleep(1.5)


if __name__ == "__main__":
    run_simulation()
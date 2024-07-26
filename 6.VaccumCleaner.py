import random

class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = (random.randint(0, 4), random.randint(0, 4))  # Random initial position
        self.visited = set()

    def print_environment(self):
        for row in self.environment:
            print(row)
        print()

    def clean(self):
        cleaned = 0
        while cleaned < 25:
            x, y = self.position
            if self.environment[x][y] == 1:
                print(f"Cleaning position ({x}, {y})")
                self.environment[x][y] = 0
                cleaned += 1
            self.print_environment()
            self.move()
            if self.position in self.visited:
                break
            self.visited.add(self.position)

    def move(self):
        x, y = self.position
        if x % 2 == 0:  
            if y < 4:
                y += 1
            else:
                x += 1
                y = 0
        else:  # Odd row
            if y > 0:
                y -= 1
            else:
                x += 1
                y = 4
        if x > 4:
            x = 0
        self.position = (x, y)

if __name__ == "__main__":
    environment = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
    print("Initial Environment:")
    for row in environment:
        print(row)
    print()
    cleaner = VacuumCleaner(environment)
    print("Starting cleaning process:")
    cleaner.clean()
    print("Cleaning completed. Final Environment:")
    for row in environment:
        print(row)
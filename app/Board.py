class Board:
    def __init__(self, data):
        self.width = data.width
        self.height = data.height
        self.turn = data.turn
        self.number_of_snakes = data.number_of_snakes
        self.food = data.food
        self.walls = data.walls
        self.gold = data.gold

    def update(self, data):
        self.turn += 1
        self.number_of_snakes = len(data.snakes)
        self.food = data.food
        self.walls = data.walls
        self.gold = data.gold

    
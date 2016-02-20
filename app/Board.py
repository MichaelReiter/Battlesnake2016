class Board:
    def __init__(self, width, height, turn, number_of_snakes, food, walls, gold):
        self.width = width
        self.height = height
        self.turn = turn
        self.number_of_snakes = number_of_snakes
        self.food = food
        self.walls = walls
        self.gold = gold

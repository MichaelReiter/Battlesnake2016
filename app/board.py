class Board(object):
    def __init__(self):
        self.width = None
        self.height = None
        self.turn = None
        self.number_of_snakes = None
        self.food = None
        self.walls = None
        self.gold = None

    def initialize(self, data):
        print data
        self.width = data["width"]
        self.height = data["height"]
        self.turn = data["turn"]
        self.number_of_snakes = len(data["snakes"])
        self.food = data["food"]
        if "walls" in data.keys():
            self.walls = data["walls"]
            self.gold = data["gold"]

    def update(self, data):
        self.turn += 1
        self.number_of_snakes = len(data["snakes"])
        self.food = data["food"]
        self.walls = data["walls"]
        self.gold = data["gold"]

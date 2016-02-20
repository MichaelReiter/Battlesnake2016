class Board(object):
    def __init__(self):
        self.width = None
        self.height = None
        self.turn = None
        self.number_of_snakes = None
        self.food = None
        self.walls = None
        self.gold = None

    def start(self, data):
        self.width = data["width"]
        self.height = data["height"]
        self.turn = data["turn"]
        self.number_of_snakes = len(data["snakes"])
        self.food = data["food"]
        self.walls = data["walls"]
        self.gold = data["gold"]
        print 'added'

    def update(self, data):
        self.turn += 1
        self.number_of_snakes = len(data["snakes"])
        self.food = data["food"]
        self.walls = data["walls"]
        self.gold = data["gold"]


def update_board(board, data):
    board.width = data["width"]
    board.height = data["height"]
    board.turn = data["turn"]
    board.number_of_snakes = len(data["snakes"])
    board.food = data["food"]
    board.walls = data["walls"]
    board.gold = data["gold"]
    return board

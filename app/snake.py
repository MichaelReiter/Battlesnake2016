class Snake:
    def __init__(self):
        pass

    def start(self, snake):
        self.id = snake["id"]
        self.coords = snake["coords"]
        self.x = self.coords[0][0]
        self.y = self.coords[0][1]
        self.age = snake["age"]
        self.health = snake["health"]
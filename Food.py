import random

class Food:
    def __init__(self, dis_width, dis_height, size):
        self.x = round(random.randrange(0, dis_width - size) / 10.0) * 10
        self.y = round(random.randrange(0, dis_height - size) / 10.0) * 10
        self.dis_width = dis_width
        self.dis_height = dis_height
        self.size = size
        self.pos = [[self.x, self.y]]

    def createFood(self):
        self.x = round(random.randrange(0, self.dis_width - self.size) / 10.0) * 10
        self.y = round(random.randrange(0, self.dis_height - self.size) / 10.0) * 10

        return self.x, self.y
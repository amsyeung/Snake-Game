from enum import Enum

class Snake:
    def __init__(self, init_x, init_y, init_speed):
        self.x = init_x
        self.y = init_y
        self.speed = init_speed
        self.size = 10
        self.head = 'RIGHT'
        self.body = [[self.x, self.y - x * 10] for x in range(5)]
        self.dead = False

    def move(self, next_x, next_y):
        orientation = ''
        opposite_direction = {'LEFT': 'RIGHT', 'RIGHT': 'LEFT', 'DOWN': 'UP', 'UP': 'DOWN'}

        if next_x > 0:
            orientation = 'RIGHT'
        elif next_x < 0:
            orientation = 'LEFT'
        elif next_y > 0:
            orientation = 'DOWN'
        elif next_y < 0:
            orientation = 'UP'

        # Avoid the snake move toward itself body and double movement to the heading direction
        if orientation != self.head and orientation != opposite_direction[self.head]:
            self.x += next_x
            self.y += next_y

            if self.isDead(self.x, self.y):
                return

            self.body.pop()
            self.body.insert(0, [self.x, self.y])
            self.head = orientation

    def auto_move(self):
        if self.head == 'RIGHT':
            self.x += 10
        elif self.head == 'LEFT':
            self.x -= 10
        elif self.head == 'DOWN':
            self.y += 10
        elif self.head == 'UP':
            self.y -= 10

        if self.isDead(self.x, self.y):
            return

        self.body.pop()
        self.body.insert(0, [self.x, self.y])

    def isDead(self, x, y):
        if [x, y] in self.body:
            self.dead = True
            return True
        return False
from direction import Direction

class Entity:

    def __init__(self, coords = (0, 0), speed = 1):

        self.default_coords = coords
        self.coords = coords
        self.default_speed = speed
        self.speed = speed

    def reset(self):
        self.speed = self.default_speed
        self.coords = self.default_coords

    def move(self, direction):
        if direction == Direction.UP_RIGHT:
            self.move(Direction.UP)
            self.move(Direction.RIGHT)
        elif direction == Direction.DOWN_RIGHT:
            self.move(Direction.DOWN)
            self.move(Direction.RIGHT)
        elif direction == Direction.DOWN_LEFT:
            self.move(Direction.DOWN)
            self.move(Direction.LEFT)
        elif direction == Direction.UP_LEFT:
            self.move(Direction.UP)
            self.move(Direction.LEFT)

        (x, y) = self.coords
        if direction == Direction.LEFT:
            x -= self.speed
        elif direction == Direction.RIGHT:
            x += self.speed
        elif direction == Direction.UP:
            y -= self.speed
        elif direction == Direction.DOWN:
            y += self.speed

        self.coords = (x, y)
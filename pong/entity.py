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
        if direction == "up_right":
            self.move("up")
            self.move("right")
        elif direction == "down_right":
            self.move("down")
            self.move("right")
        elif direction == "down_left":
            self.move("down")
            self.move("left")
        elif direction == "up_left":
            self.move("up")
            self.move("left")

        (x, y) = self.coords
        if direction == "left":
            x -= self.speed
        elif direction == "right":
            x += self.speed
        elif direction == "up":
            y -= self.speed
        elif direction == "down":
            y += self.speed

        self.coords = (x, y)
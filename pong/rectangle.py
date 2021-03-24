from pygame import draw

class Rectangle:

    def __init__(self, screen, coords = (0, 0), size = (32, 64), move_size = 1):
        
        self.coords = coords
        self.size = size
        self.screen = screen
        self.move_size = move_size

    def update(self):
        draw.rect(
            self.screen,
            (255, 255, 255),
            (self.coords[0], self.coords[1], self.size[0], self.size[1])
        )

    def move(self, direction):
        (x, y), (w, h) = self.coords, self.size
        if direction == "left":
            x -= self.move_size
        elif direction == "right":
            x += self.move_size
        elif direction == "up":
            y -= self.move_size
        elif direction == "down":
            y += self.move_size

        (screen_size_x, screen_size_y) = self.screen.get_size()
        if(x < 0):
            x = 0
        elif x + w > screen_size_x:
            x = screen_size_x - w
        elif y < 0:
            y = 0
        elif y + h > screen_size_y:
            y = screen_size_y - h

        self.coords = (x, y)
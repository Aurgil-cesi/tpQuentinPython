from pygame import draw

class Circle:

    def __init__(self, screen, coords = (0, 0), move_size = 1):
        
        # x, y
        self.screen = screen
        self.coords = coords
        self.move_size = move_size

    def update(self):
        draw.circle(
            self.screen,
            (255, 255, 255),
            self.coords,
            15
        )

    def move(self, direction):
        (x, y) = self.coords
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
        elif x > screen_size_x:
            x = screen_size_x
        elif y < 0:
            y = 0
        elif y > screen_size_y:
            y = screen_size_y

        self.coords = (x, y)
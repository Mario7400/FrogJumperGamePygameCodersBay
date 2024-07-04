import pygame, os

PATH = os.path.abspath('.')+'/'


class CreatingBackground:
    def __init__(self, grid_size, screen_width, screen_height):
        super().__init__()
        self.grid_size = grid_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.images_path = [
            PATH+"imagesField/01_green.png",
            PATH+"imagesField/02_greenToRoad.png",
            PATH+"imagesField/03_road.png",
            PATH+"imagesField/03_road.png",
            PATH+"imagesField/04_roadToGreen.png",
            PATH+"imagesField/01_green.png",
            PATH+"imagesField/01_green.png",
            PATH+"imagesField/05_greenToWater.png",
            PATH+"imagesField/06_water.png",
            PATH+"imagesField/06_water.png",
            PATH+"imagesField/07_waterToGreen.png",
            PATH+"imagesField/01_green.png"
        ]

    def load_image(self, line):
        return pygame.transform.scale(pygame.image.load(self.images_path[line-1]), (self.screen_width, self.grid_size))

    def background_pos(self, line):
        return 0, self.screen_height-self.grid_size*line

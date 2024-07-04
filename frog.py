import pygame


class Frog(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, movement_speed, screen_width, screen_height, grid_size, init_x_position,
                 y_position, sprite_width, sprite_height, sprite_columns, sprite_rows, movement_direction, start_row,
                 end_row):
        super().__init__()
        self.sprites = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = grid_size
        self.movement_direction = movement_direction

        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprite_columns = sprite_columns
        self.sprite_rows = sprite_rows

        self.is_animating = False
        self.movement_speed = movement_speed
        self.current_sprite = 0
        self.pos_x = init_x_position
        self.pos_y = y_position
        self.sprite_sheet = pygame.image.load(sprite_sheet_path)

        self.load_sprites(start_row, end_row)

        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

    def animate(self, is_animating):
        self.is_animating = is_animating

    def update(self, speed):
        if self.is_animating:
            self.pos_x += int(self.movement_speed)
            self.rect.topleft = [self.pos_x, self.pos_y]
            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

            if (1 <= self.current_sprite <= 1 + speed) or (2 >= self.current_sprite > (2 - speed)):
                if self.movement_direction == "up":
                    if self.pos_y - self.grid_size >= - self.grid_size:
                        self.pos_y -= self.grid_size / 2
                        self.rect.y = self.pos_y
                if self.movement_direction == "down":
                    if self.pos_y + self.grid_size <= self.screen_height - self.grid_size / 2:
                        self.pos_y += self.grid_size / 2
                        self.rect.y = self.pos_y
                if self.movement_direction == "left":
                    if self.pos_x >= self.grid_size / 2:  # Check if the movement is within the screen boundaries
                        self.pos_x -= self.grid_size / 2
                        self.rect.x = self.pos_x
                if self.movement_direction == "right":
                    if self.pos_x + self.grid_size / 2 <= self.screen_width - self.grid_size:
                        self.pos_x += self.grid_size / 2
                        self.rect.x = self.pos_x

    def update_water_movement(self):
        self.rect.topleft = [self.pos_x, self.pos_y]

    def won(self):
        if self.pos_y <= 0:
            return True
        else:
            return False

    def load_sprites(self, start_row, end_row):
        start_row = start_row
        end_row = end_row
        start_col = 4
        end_col = 6

        sprite_width = self.sprite_width
        sprite_height = self.sprite_height

        target_width = self.grid_size
        target_height = self.grid_size

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                x = col * sprite_width
                y = row * sprite_height
                sprite = self.sprite_sheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
                sprite = pygame.transform.scale(sprite, (target_width, target_height))  # Scale the sprite

                self.sprites.append(sprite)

    def current_line(self):
        if self.screen_height-self.grid_size-15 == self.pos_y:
            return 1
        if self.screen_height-2*self.grid_size-15 == self.pos_y:
            return 2
        if self.screen_height-3*self.grid_size-15 == self.pos_y:
            return 3
        if self.screen_height-4*self.grid_size-15 == self.pos_y:
            return 4
        if self.screen_height-5*self.grid_size-15 == self.pos_y:
            return 5
        if self.screen_height-6*self.grid_size-15 == self.pos_y:
            return 6
        if self.screen_height-7*self.grid_size-15 == self.pos_y:
            return 7
        if self.screen_height-8*self.grid_size-15 == self.pos_y:
            return 8
        if self.screen_height-9*self.grid_size-15 == self.pos_y:
            return 9
        if self.screen_height-10*self.grid_size-15 == self.pos_y:
            return 10
        if self.screen_height-11*self.grid_size-15 == self.pos_y:
            return 11
        if self.screen_height-12*self.grid_size-15 == self.pos_y:
            return 12
        return 0

    def set_new_x_position(self, new_x_position):
        if not new_x_position < 0 and not new_x_position > self.screen_width-self.grid_size:
            self.pos_x = new_x_position

    def reset_position(self):
        self.pos_x = self.grid_size*10
        self.pos_y = self.screen_height-self.grid_size-15
        self.rect.topleft = (self.pos_x, self.pos_y)

    def set_movement_direction(self, movement_direction):
        self.movement_direction = movement_direction
        if self.movement_direction == "up":
            self.sprites = []
            self.load_sprites(3, 4)
        elif self.movement_direction == "down":
            self.sprites = []
            self.load_sprites(0, 1)
        elif self.movement_direction == "left":
            self.sprites = []
            self.load_sprites(1, 2)
        elif self.movement_direction == "right":
            self.sprites = []
            self.load_sprites(2, 3)

    def is_dead(self):
        return self.is_dead

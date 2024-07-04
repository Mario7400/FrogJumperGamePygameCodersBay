import pygame


class Movements(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, movement_speed, screen_width, screen_height, grid_size, init_x_position,
                 y_position, sprite_width, sprite_height, sprite_columns, sprite_rows,  move_left_to_right=True,
                 is_enemy=False):
        super().__init__()
        self.sprites = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = grid_size
        self.move_left_to_right = move_left_to_right
        self.is_enemy = is_enemy

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

        self.load_sprites()

        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

    def animate(self, is_animating):
        self.is_animating = is_animating

    def update(self, speed):
        if self.is_animating:
            if self.move_left_to_right:
                self.pos_x += float(self.movement_speed)
                if self.pos_x >= self.screen_width:
                    self.pos_x = -self.grid_size
            else:
                self.pos_x -= float(self.movement_speed)
                if self.pos_x <= -self.grid_size:
                    self.pos_x = self.screen_width

            self.rect.topleft = [self.pos_x, self.pos_y]

            self.current_sprite += speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

    def load_sprites(self):
        sprite_width = self.sprite_width
        sprite_height = self.sprite_height
        sprite_columns = self.sprite_columns
        sprite_rows = self.sprite_rows

        target_width = self.grid_size
        target_height = self.grid_size

        for row in range(sprite_rows):
            for col in range(sprite_columns):
                x = col * sprite_width
                y = row * sprite_height
                sprite = self.sprite_sheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
                sprite = pygame.transform.scale(sprite, (target_width, target_height)).convert_alpha()

                if not self.move_left_to_right:
                    sprite = pygame.transform.flip(sprite, True, False)

                self.sprites.append(sprite)

    def get_x_position(self):
        return self.pos_x

    def get_is_enemy(self):
        return self.is_enemy

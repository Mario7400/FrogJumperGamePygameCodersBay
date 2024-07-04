import pygame, sys, os, copy
from creatingBackground import CreatingBackground
from movements import Movements
from frog import Frog
from movement_data import Data

PATH = os.path.abspath('.')+'/'
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
speed_factor = 0.0
level_counter = 1
delay_time = 4000
delay_time_level_up = 2000
delay_time_won = 8000
level_that_should_be_reached = 2
update_speed_frog = 0.08
font_path = pygame.font.match_font('comicsansms')

path_frog_jump = pygame.mixer.Sound(PATH + "soundEffects/jump.mp3")
sound_effect_water = pygame.mixer.Sound(PATH + 'soundEffects/water_fall.mp3')
sound_effect_electric = pygame.mixer.Sound(PATH + 'soundEffects/electrical-shock-zap-106412.mp3')
sound_effect_crash = pygame.mixer.Sound(PATH + 'soundEffects/shatter-93498.mp3')
sound_effect_jump = pygame.mixer.Sound(PATH + 'soundEffects/cartoon-jump-6462.mp3') # jump.mp3 # cartoon-jump-6462.mp3
sound_effect_frog_voice = pygame.mixer.Sound(PATH + 'soundEffects/frog_voice.mp3')
sound_effect_level_up = pygame.mixer.Sound(PATH + 'soundEffects/level-up-2-199574.mp3')
sound_effect_won = pygame.mixer.Sound(PATH + 'soundEffects/won.mp3')

speed_of_animation = 0.06*0.5

grid_size = 40
screen_width = grid_size*20
screen_height = grid_size*12

screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption("Frog Jumper Game")

creatingBackground = CreatingBackground(grid_size, screen_width, screen_height)

moving_sprites_frog = pygame.sprite.Group()  # Create a sprite group
movement_frog = Frog(PATH + "imageFrog/frog2_576x384px.png", 0.06,
                     screen_width, screen_height, grid_size, grid_size * 10, screen_height - grid_size - 15,
                     576 / 12, 384 / 8, 12, 8, "up", 3, 4)
moving_sprites_frog.add(movement_frog)  # Add the Frog sprite to the sprite group


def print_message(message, font_size, r=128, g=0, b=128): # A car crashed into the frog! :(
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render(message, True, (r, g, b))
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text_surface, text_rect)


def create_movements(sprites, data):
    for (sprite_sheet_path, movement_speed, init_x_position, y_position, sprite_width, sprite_height, sprite_columns,
         sprite_rows, move_left_to_right, is_enemy) in data:
        sprites.add(Movements(PATH + sprite_sheet_path, movement_speed, screen_width, screen_height, grid_size,
                              init_x_position, y_position, sprite_width, sprite_height, sprite_columns,
                              sprite_rows, move_left_to_right, is_enemy))


movement_data = Data(grid_size, speed_factor)
movements_data_constructor = movement_data.get_movement_data()

moving_sprites_line2 = pygame.sprite.Group()
moving_sprites_line3 = pygame.sprite.Group()
moving_sprites_line4 = pygame.sprite.Group()
moving_sprites_line5 = pygame.sprite.Group()
moving_sprites_line8 = pygame.sprite.Group()
moving_sprites_line9 = pygame.sprite.Group()
moving_sprites_line10 = pygame.sprite.Group()
moving_sprites_line11 = pygame.sprite.Group()

list_moving_sprites = [moving_sprites_line2, moving_sprites_line3, moving_sprites_line4, moving_sprites_line5,
                       moving_sprites_line8, moving_sprites_line9, moving_sprites_line10, moving_sprites_line11]

for i in range(len(list_moving_sprites)):
    create_movements(list_moving_sprites[i], movements_data_constructor[i])

image_line = []
for i in range(int(screen_height / grid_size + 1)):
    image_line.append(creatingBackground.load_image(i))

background_position = []
for i in range(int(screen_height / grid_size + 1)):
    background_position.append(creatingBackground.background_pos(i))


def handle_collision(message, fontsize):
    global is_animating, allow_change, dead, level_counter, collision_detected
    is_animating = False
    allow_change = True
    print_message(message, fontsize)
    dead = True
    level_counter = 1
    collision_detected = True


def reset_the_game(speed_factor_new):
    for sprite_group_new in list_moving_sprites:
        sprite_group_new.empty()
    movement_data_new = Data(grid_size, speed_factor_new)
    movements_data_constructor_new = movement_data_new.get_movement_data()
    for sprites in range(len(list_moving_sprites)):
        create_movements(list_moving_sprites[sprites], movements_data_constructor_new[sprites])


start_swipe_pos = None
end_swipe_pos = None

movement_direction = ""
is_animating = True
allow_change = True
counter_to_restart = 0
counter_to_allow_change = 0
dead = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_UP and allow_change:
                movement_frog.animate(is_animating)
                movement_frog.set_movement_direction("up")
                sound_effect_jump.play()
                allow_change = False
            elif event.key == pygame.K_DOWN and allow_change:
                movement_frog.animate(is_animating)
                movement_frog.set_movement_direction("down")
                sound_effect_jump.play()
                allow_change = False
            elif event.key == pygame.K_LEFT and allow_change:
                movement_frog.animate(is_animating)
                movement_frog.set_movement_direction("left")
                sound_effect_jump.play()
                allow_change = False
            elif event.key == pygame.K_RIGHT and allow_change:
                movement_frog.animate(is_animating)
                movement_frog.set_movement_direction("right")
                sound_effect_jump.play()
                allow_change = False
            elif event.type == pygame.FINGERDOWN:
                start_swipe_pos = pygame.Vector2(event.x, event.y)
            elif event.type == pygame.FINGERMOTION:
                if start_swipe_pos is not None:
                    end_swipe_pos = pygame.Vector2(event.x, event.y)
            elif event.type == pygame.FINGERUP:
                if start_swipe_pos is not None and end_swipe_pos is not None:
                    swipe_vector = end_swipe_pos - start_swipe_pos
                    swipe_direction = None

                    if swipe_vector.length_squared() > 100:
                        if abs(swipe_vector.x) > abs(swipe_vector.y):
                            if swipe_vector.x > 0:
                                swipe_direction = "right"
                            else:
                                swipe_direction = "left"
                        else:
                            if swipe_vector.y > 0:
                                swipe_direction = "down"
                            else:
                                swipe_direction = "up"

                    if swipe_direction == "left":
                        movement_frog.animate(is_animating)
                        movement_frog.set_movement_direction("left")
                        sound_effect_jump.play()
                    elif swipe_direction == "right":
                        movement_frog.animate(is_animating)
                        movement_frog.set_movement_direction("right")
                        sound_effect_jump.play()
                    elif swipe_direction == "up":
                        movement_frog.animate(is_animating)
                        movement_frog.set_movement_direction("up")
                        sound_effect_jump.play()
                    elif swipe_direction == "down":
                        movement_frog.animate(is_animating)
                        movement_frog.set_movement_direction("down")
                        sound_effect_jump.play()

                    start_swipe_pos = None
                    end_swipe_pos = None

    for i in range(int(screen_height / grid_size + 1)):
        screen.blit(image_line[i], background_position[i])

    if not dead and level_counter <= level_that_should_be_reached:
        print_message("Level " + str(level_counter),44, 154, 205, 50)

    for sprites_group in list_moving_sprites:
        for movement in sprites_group:
            movement.animate(is_animating)

    sprite_groups = [moving_sprites_line2, moving_sprites_line3, moving_sprites_line4, moving_sprites_line5,
                     moving_sprites_line8, moving_sprites_line9, moving_sprites_line10, moving_sprites_line11,
                     moving_sprites_frog]
    for sprite_group in sprite_groups:
        sprite_group.draw(screen)

    sprite_groups_and_speeds = [
        (moving_sprites_line2, speed_of_animation), (moving_sprites_line3, speed_of_animation),
        (moving_sprites_line4, speed_of_animation), (moving_sprites_line5, speed_of_animation),
        (moving_sprites_line8, speed_of_animation), (moving_sprites_line9, speed_of_animation),
        (moving_sprites_line10, speed_of_animation), (moving_sprites_line11, speed_of_animation)
    ]

    for sprite_group, speed in sprite_groups_and_speeds:
        sprite_group.update(speed)

    moving_sprites_frog.update(update_speed_frog)
    if not allow_change:
        counter_to_allow_change += 1

    if counter_to_allow_change == 2/update_speed_frog+1:
        allow_change = True
        counter_to_allow_change = 0

    for frog_sprite in moving_sprites_frog:
        scaled_frog = copy.copy(frog_sprite)
        scaled_frog.rect = frog_sprite.rect.inflate(-38, -38)
        moving_sprites = [moving_sprites_line11, moving_sprites_line10, moving_sprites_line9, moving_sprites_line8]
        for line_number in range(2, 6):
            if movement_frog.current_line() == line_number:
                collisions = pygame.sprite.spritecollide(scaled_frog, moving_sprites[line_number-2], False)
                if collisions:
                    handle_collision("Crashing into a car is like just using chat GPT...", 20)
                    sound_effect_jump.stop()
                    sound_effect_crash.play()
                    counter_to_restart += 1
                    if counter_to_restart == 10:
                        pygame.time.delay(delay_time)

                        reset_the_game(0.0)

                        movement_frog.reset_position()
                        sound_effect_frog_voice.play()

                        is_animating = True
                        counter_to_restart = 0
                        dead = False

        scaled_frog = copy.copy(frog_sprite)
        scaled_frog.rect = frog_sprite.rect.inflate(-15, -15)
        moving_sprites = [moving_sprites_line5, moving_sprites_line4, moving_sprites_line3, moving_sprites_line2]
        for line_number in range(8, 12):
            if movement_frog.current_line() == line_number and level_counter:
                collisions = pygame.sprite.spritecollide(scaled_frog, moving_sprites[line_number - 8], False)
                if not collisions:
                    handle_collision("Frameworks are like a swimming aid ;)", 20)
                    sound_effect_jump.stop()
                    sound_effect_water.play()

                    counter_to_restart += 1
                    if counter_to_restart == 10:
                        pygame.time.delay(delay_time)

                        reset_the_game(0.0)

                        movement_frog.reset_position()
                        sound_effect_frog_voice.play()

                        is_animating = True
                        counter_to_restart = 0
                        dead = False
                else:
                    for collided_sprite in collisions:
                        if collided_sprite.is_enemy:
                            handle_collision("Electric eels are like programming without polymorphism..", 20)
                            sound_effect_jump.stop()
                            sound_effect_electric.play()

                            counter_to_restart += 1
                            if counter_to_restart == 10:
                                pygame.time.delay(delay_time)

                                reset_the_game(0.0)

                                movement_frog.reset_position()
                                sound_effect_frog_voice.play()

                                is_animating = True
                                counter_to_restart = 0
                                dead = False
                        else:
                            movement_frog.set_new_x_position(collided_sprite.get_x_position())
                            movement_frog.update_water_movement()

    if movement_frog.won():
        if is_animating:
            level_counter += 1

        is_animating = False

        if level_counter > level_that_should_be_reached:
            counter_to_restart += 1
            print_message("Won - Codersbay is cool :)", 44, 255, 0, 0)
            if counter_to_restart == 10:
                sound_effect_won.play()
                pygame.time.delay(delay_time_won)
                pygame.quit()
                sys.exit()
        else:
            counter_to_restart += 1
            if counter_to_restart == 10:
                if path_frog_jump == PATH + "soundEffects/jump.mp3":
                    sound_effect_jump.stop()
                sound_effect_level_up.play()
                pygame.time.delay(delay_time_level_up)

                movement_frog.reset_position()
                sound_effect_frog_voice.play()

                speed_factor += 0.3

                reset_the_game(speed_factor)

                is_animating = True
                counter_to_restart = 0

    pygame.display.flip()
    clock.tick(60)

# Import the pygame module
import pygame
import random
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('mario.png')
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

            # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('goomba.png')
        image_size= self.image.get_rect().size # you can get size
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.image.get_rect(
            center=(
                random.randint(image_size[0]+30, SCREEN_WIDTH - image_size[0]),
                random.randint(image_size[1], SCREEN_HEIGHT-image_size[1]),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self, action):
        if action == 1:
            self.rect.move_ip(0, -5)
        if action == 2:
            self.rect.move_ip(0, 5)
        if action == 3:
            self.rect.move_ip(-5, 0)
        if action == 4:
            self.rect.move_ip(5, 0)

            # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    """def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()"""

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("fondo.png")

actions = list(range(1,5))
# Instantiate player. Right now, this is just a rectangle.
player = Player()
enemy = Enemy()
# Variable to keep the main loop running
running = True
pygame.mixer.music.load('mario.mp3')
pygame.mixer.music.play(-1)
# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
    print('in')
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    enemy.update(action=random.choice(actions))

    # Fill the screen with black
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # Draw the player on the screen
    screen.blit(enemy.image, enemy.rect)
    screen.blit(player.image, player.rect)
    """if pygame.sprite.spritecollideany(player, enemy):
        print('touch')"""
    if pygame.sprite.collide_rect(player, enemy):
        print('jm')
        running = False
    # Update the display
    pygame.display.flip()
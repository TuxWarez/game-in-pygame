import pygame
import math

COLOR = (0xAA, 0, 0)
color_gun = (0, 0xAA, 0)
SURFACE_COLOR = (0xAA, 0xAA, 0xAA)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()
    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x >= 620:
            self.rect.x -= pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x <= 0:
            self.rect.x += pixels

    def moveForward(self, speed):
        self.rect.y += speed
        if self.rect.y >= 460:
            self.rect.y -= speed

    def moveBack(self, speed):
        self.rect.y -= speed
        if self.rect.y <= 0:
            self.rect.y += speed

    def rotateRight(self, rotate):
        self.rect.x += (math.sin(rotate) * 25)
        self.rect.y += (math.cos(rotate) * 25)

    def rotateLeft(self, rotate):
        self.rect.x -= (math.sin(rotate) * 25)
        self.rect.y -= (math.cos(rotate) * 25)

background_colour = (0xAA, 0xAA, 0xAA)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("TuxWare's game")
screen.fill(background_colour)
pygame.display.flip()

all_sprites_list = pygame.sprite.Group()
object_ = Sprite((180, 0, 0), 20, 20)
object_.rect.x = 320
object_.rect.y = 240

all_sprites_list.add(object_)
clock = pygame.time.Clock()

running = True
rotate_sy = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        object_.moveRight(5)
    if keys[pygame.K_DOWN]:
        object_.moveForward(5)
    if keys[pygame.K_UP]:
        object_.moveBack(5)
    if keys[pygame.K_q]:
        rotate_sy += 0.25
        object_.rotateRight(rotate_sy)
    if keys[pygame.K_e]:
        rotate_sy -= 0.25
        object_.rotateLeft(rotate_sy)

    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 640, 480))
    pygame.draw.rect(screen, (170, 170, 170), pygame.Rect(5, 5, 630, 470))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

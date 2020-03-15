from math import sqrt
import pygame
from pygame import mixer
from random import randint
from typing import List


def show_big_text(text, x, y):
    label = pygame.font.Font("freesansbold.ttf", 64).render(text, True, (255, 255, 255))
    screen.blit(label, (x, y))


class Score:
    def __init__(self):
        self.score_value = 0
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.textX = 10
        self.textY = 10

    def __call__(self, screen, x, y):
        score = self.font.render("Score : " + str(self.score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))


class Entity:
    def __init__(
            self,
            image_name,
            init_x,
            init_y,
            speed,
            boost,
            dx=0,
            dy=0,
            icon_x_offset=0,
            icon_y_offset=0
    ):
        self.image =pygame.image.load(image_name)
        self.image_size = self.image.get_rect().size
        self.center_offset_x = self.image_size[0] // 2
        self.center_offset_y = self.image_size[1] // 2
        self.x = init_x
        self.y = init_y
        self.dx = dx
        self.dy = dy
        self.icon_x_offset = icon_x_offset
        self.icon_y_offset = icon_y_offset
        self.speed = speed
        self.boost = boost
        self.status = 1

    def __call__(self):
        screen.blit(self.image, (self.x, self.y))

    def move_x(self):
        self.x += self.dx
        if self.x < 0:
            self.x = 0
        elif self.x > windowWidth - self.icon_x_offset:
            self.x = windowWidth - self.icon_x_offset

    def move_y(self):
        self.y += self.dy
        if self.y < 0:
            self.y = 0
        elif self.y > windowHeight - self.icon_y_offset:
            self.y = windowHeight - self.icon_y_offset

    def update_dx(self, direction, boost=None):
        boost = boost if boost else self.boost
        self.dx = direction * self.speed * boost

    def update_dy(self, direction, boost=None):
        boost = boost if boost else self.boost
        self.dy = direction * self.speed * boost

    def stop_x(self):
        self.dx = 0

    def stop_y(self):
        self.dy = 0

    def stop(self):
        self.stop_x()
        self.stop_y()

    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Spaceship(Entity):
    def __init__(self, init_x, init_y, speed, boost=1, dx=0, dy=0):
        super(Spaceship, self).__init__(
            "player.png",
            init_x,
            init_y,
            speed,
            boost,
            dx,
            dy,
            icon_x_offset=60,
            icon_y_offset=65
        )


class Enemy(Entity):
    def __init__(self, init_x, init_y, speed, boost=1, dx=0, dy=0):
        super(Enemy, self).__init__(
            "virus.png",
            init_x,
            init_y,
            speed,
            boost,
            dx,
            dy,
            icon_x_offset=60,
            icon_y_offset=60,
        )

    def move(self):
        self.x += self.dx
        if self.x < 0:
            self.x = 0
            self.dx = self.dx * -1
            self.y += self.speed * self.boost
        elif self.x > windowWidth - self.icon_x_offset:
            self.x = windowWidth - self.icon_x_offset
            self.dx = self.dx * -1
            self.y += self.speed * self.boost

    def gets_killed(self):
        self.status = 0


class Bullet(Entity):
    def __init__(self, image, init_x, init_y, speed, boost=1, dx=0, dy=0, range=1):
        super(Bullet, self).__init__(
            image,
            init_x,
            init_y,
            speed,
            boost,
            dx,
            dy,
            icon_x_offset=12,
            icon_y_offset=12,
        )
        self.range = range

    def move(self):
        self.y += self.dy
        if self.y <= 0:
            self.status = 0

    def hit_enemy(self, enemies: List[Enemy]):
        for enemy in enemies:
            if self.distance(enemy) < sqrt(enemy.center_offset_x**2 + enemy.center_offset_y**2) * self.range:
                enemy.gets_killed()
                self.status = 0


class RegularBullet(Bullet):
    def __init__(self, init_x, init_y):
        super(RegularBullet, self).__init__(
            image="bullet1.png",
            init_x=init_x,
            init_y=init_y,
            speed=50,
            dy=-50
        )


class SuperBullet(Bullet):
    def __init__(self, init_x, init_y):
        super(SuperBullet, self).__init__(
            image="bullet2.png",
            init_x=init_x,
            init_y=init_y,
            speed=100,
            dy=-100,
            range=2,
        )


class UltraBullet(Bullet):
    def __init__(self, init_x, init_y):
        super(UltraBullet, self).__init__(
            image="bullet3.png",
            init_x=init_x,
            init_y=init_y,
            speed=150,
            dy=-150,
            range=3,
        )


# Initialize the pygame
pygame.init()

# Initialize a screen for our game
windowWidth, windowHeight = 1024, 1024
screen = pygame.display.set_mode((windowWidth, windowHeight))

# Set the title and caption
pygame.display.set_caption(" Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background.png")
mixer.music.load("background.wav")
mixer.music.play(-1)

player = Spaceship(init_x=windowWidth / 2, init_y=windowHeight - 100, speed=10, boost=2)
enemies = [
    Enemy(init_x=randint(0, windowWidth - 60), init_y=randint(0, windowHeight / 2), speed=20, dx=randint(20, 40))
    for _ in range(0, 100)
]
bullets = []
score = Score()

# Game Loop
running = True
while running:
    # Fill the screen with RGB - (Red, Green, Blue)
    # screen.fill((0, 0, 128))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.update_dx(direction=-1)
            elif event.key == pygame.K_RIGHT:
                player.update_dx(direction=1)
            elif event.key == pygame.K_UP:
                player.update_dy(direction=-1)
            elif event.key == pygame.K_DOWN:
                player.update_dy(direction=1)
            elif event.key == pygame.K_c:
                bullets.append(RegularBullet(player.x + player.center_offset_x - 10, player.y + player.center_offset_y))
            elif event.key == pygame.K_x:
                bullets.append(SuperBullet(player.x + player.center_offset_x - 10, player.y + player.center_offset_y))
            elif event.key == pygame.K_z:
                bullets.append(UltraBullet(player.x + player.center_offset_x - 10, player.y + player.center_offset_y))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop_x()
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.stop_y()

    player.move_x()
    player.move_y()
    print(player.x, player.y)
    player()
    for bullet in bullets:
        bullet.move()
        bullet.hit_enemy(enemies)
        if bullet.status == 1:
            bullet()
        elif bullet.status == 0:
            bullets.remove(bullet)
            del bullet
    for enemy in enemies:
        if enemy.status == 1:
            enemy.move()
            enemy()
        elif enemy.status == 0: 
            enemies.remove(enemy)
            del enemy
    score(screen=screen, x=100, y=20)
    if len(enemies) == 0:
        show_big_text("You Won!!!", x=windowWidth/2-200, y=windowHeight/2)
    pygame.display.update()

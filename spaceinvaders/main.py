import pygame
from pygame import mixer
from random import randint


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
        self.x = init_x
        self.y = init_y
        self.dx = dx
        self.dy = dy
        self.icon_x_offset = icon_x_offset
        self.icon_y_offset = icon_y_offset
        self.speed = speed
        self.boost = boost

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


class Bullet(Entity):
    def __init__(self, init_x, init_y, speed, boost=1, dx=0, dy=0):
        super(Bullet, self).__init__(
            "bullet1.png",
            init_x,
            init_y,
            speed,
            boost,
            dx,
            dy,
            icon_x_offset=60,
            icon_y_offset=60,
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

player = Spaceship(init_x=450, init_y=900, speed=10, boost=2)
enemies = [
    Enemy(init_x=randint(0, windowWidth - 60), init_y=randint(0, windowHeight / 2), speed=20, dx=randint(-30, 30))
    for _ in range(0, 10)
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
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop_x()
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.stop_y()

    player.move_x()
    player.move_y()
    print(player.x, player.y)
    player()
    for enemy in enemies:
        enemy.move()
        enemy()
    score(screen=screen, x=100, y=20)
    pygame.display.update()

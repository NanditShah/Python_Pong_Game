import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("PongGame")
x = 265
y = 580
radius = 5
width = 120
height = 10
vel = 10
gameOn = True
i = 8
j = 10
no = [random.randint(i, j), random.randint(i, j)]
upSide = False
sound = pygame.mixer.Sound("ping_pong.ogg")
wallCollideSound = pygame.mixer.Sound("Pop.ogg")
font = pygame.font.SysFont('comicsans', 30, True, True)
finalScoreFont = pygame.font.SysFont('comicsans', 50, True, False)
score = 0
increaseSpeed = 5


class Ball(object):
    def __init__(self, x, y):
        self.radius = j
        self.x = x
        self.y = y
        self.ballVel = [random.randint(i, j), random.randint(i, j)]

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)

    def move(self):
        collideWithWall()
        collide()
        text = font.render("Score = " + str(score), 1, (0, 0, 0))
        screen.blit(text, (450, 10))
        self.x += self.ballVel[0]
        self.y += self.ballVel[1]


def highScore():
    global score

    file = open("highScore.txt", 'r+')
    # file.write(highScore)
    # file.seek(0)
    high = font.render("High Score = " + str(file.read()), 1, (0, 0, 0))
    screen.blit(high, (20, 10))
    file.seek(0)
    if score > int(file.read()):
        file.seek(0)
        file.write(str(score))


def collide():
    global i
    global j
    global upSide
    global score
    global increaseSpeed
    # if ball.radius+ball.y >= board.y and (board.x<= and board.x+board.width:
    if ball.radius + ball.y >= board.y and ball.x >= board.x and board.x + board.width > ball.x:
        # ball.y=board.y-ball.radius
        # ball.x+=j
        # ball.y-=12
        sound.play()
        upSide = True
        score += 1
        if ball.x >= board.x and ball.x <= board.x + (board.width * 0.3):
            ball.ballVel[0] = -random.randint(i, j)
            ball.ballVel[1] = -random.randint(i, j)
        else:
            ball.ballVel[0] = +random.randint(i, j)
            ball.ballVel[1] = -random.randint(i, j)
        if score >= increaseSpeed:
            i += 2
            j += 2
            increaseSpeed += 5


def collideWithWall():
    global upSide

    if ball.y - ball.radius <= 0:
        wallCollideSound.play()
        upSide = False
        if 0 <= ball.x <= 100:
            ball.ballVel[0] = -random.randint(i, j)
            ball.ballVel[1] = +random.randint(i, j)
        elif 500 < ball.x < 600:
            ball.ballVel[0] = -random.randint(i, j)
            ball.ballVel[1] = +random.randint(i, j)
        else:
            ball.ballVel[0] = -random.randint(i, j)
            ball.ballVel[1] = +random.randint(i, j)
    if upSide:
        # no[0]=i
        # no[1]=j

        if ball.x + ball.radius >= 600:
            wallCollideSound.play()
            ball.ballVel[0] = -random.randint(i, j)
            ball.ballVel[1] = -random.randint(i, j)
        if ball.x - ball.radius <= 0:
            wallCollideSound.play()
            ball.ballVel[0] = +random.randint(i, j)
            ball.ballVel[1] = -random.randint(i, j)
    else:
        if ball.x + ball.radius >= 600:
            wallCollideSound.play()
            ball.ballVel[0] = -random.randint(i, j)
            ball.ballVel[1] = +random.randint(i, j)
        if ball.x - ball.radius <= 0:
            wallCollideSound.play()
            ball.ballVel[0] = +random.randint(i, j)
            ball.ballVel[1] = +random.randint(i, j)


class SkateBoard(object):
    def __init__(self):
        self.x = 265
        self.y = 580
        self.radius = 5
        self.width = 120
        self.height = j

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y + self.radius), self.radius)
        pygame.draw.circle(win, (0, 0, 0), (self.x + self.width, self.y + self.radius), self.radius)


ball = Ball(300, 300)
board = SkateBoard()
while gameOn:
    pygame.time.delay(30)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            gameOn = False
    screen.fill((255, 255, 255))
    if ball.y >= 600:
        text = font.render("Your Score = " + str(score), 1, (0, 0, 0))
        screen.blit(text, (240, 280))
        gameOn = False

    board.draw(screen)
    ball.draw(screen)

    ball.move()
    # board.collide()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        board.x += vel

    elif keys[pygame.K_LEFT]:
        board.x -= vel
    if board.x - board.radius <= 0:
        board.x = board.radius
    if board.x + board.width + board.radius >= 600:
        board.x = 600 - board.radius - board.width
    highScore()
    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()

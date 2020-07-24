import pygame, random

pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

# bird
birdIMG = pygame.image.load("bird2.png")
birdX = 70
birdY = 300
birdY_var = 3

# caption and icon
pygame.display.set_caption("udta panchi")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# statement
enter = pygame.font.Font("freesansbold.ttf", 20)
textX = 93
textY = 270

#green_pipe
green_pipe = pygame.image.load('pipe_green.png').convert()
green_pipet = pygame.transform.flip(green_pipe,False,True)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
# bg image
cx = 0
cy = 0
background = pygame.image.load("cloud_bg.jpg")

# ground
floor = pygame.image.load("Floor.png")
gx = 0
gy = 470
def create_rect():
    pipe_height = random.randint(220,420)
    pipe_heightchange = random.randint(520,600)
    pipe_rect_bottom = green_pipe.get_rect(midtop=(500, pipe_height))
    pipe_rect_top = green_pipe.get_rect(midtop=(500, pipe_height-pipe_heightchange))
    return pipe_rect_bottom, pipe_rect_top
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx-=3
    return pipes

def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom>=600:
            screen.blit(green_pipe,pipe)
        else:
            screen.blit(green_pipet,pipe)
def enter_text(x, y):
    Input = enter.render("PRESS SPACE TO START", True, (0, 0, 0))
    screen.blit(Input, (x, y))


def bird(x, y):
    screen.blit(birdIMG, (x, y))

def ground(x,y):
    screen.blit(floor,(x,y))

def cloud(x,y):
    screen.blit(background, (x, y))
running = True
starting = True
while starting:
    cloud(cx,cy)
    enter_text(textX, textY)
    ground(gx, gy)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starting = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                starting = False
                while running:
                    # bg image
                    cloud(cx,cy)
                    cloud(cx + 400,cy)
                    cx -= 1
                    if cx<=-400:
                        cx = 0
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                birdY_var = -3

                            if event.key == pygame.K_DOWN:
                                birdY_var = 5
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                birdY_var = 3
                        if event.type == SPAWNPIPE:
                            pipe_list.extend(create_rect())

                    clock.tick(120)

                    if birdY <= 0:
                        birdY = 0
                    elif birdY >= 550:
                        birdY = 550
                    #pipe
                    pipe_list = move_pipe(pipe_list)
                    draw_pipe(pipe_list)
                    #scrolling ground
                    ground(gx,gy)
                    ground(gx + 395,gy)
                    gx-=3
                    if gx <= -395:
                        gx=0

                    birdY += birdY_var
                    bird(birdX, birdY)
                    pygame.display.update()

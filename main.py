import pygame, sys, random, math
width = 640
height = 400

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

w = 160
h = 80
posx = 0
posy = 0
speed = 1
velx = speed
vely = speed
bounceRange = 1

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255, 0)

running = True
color = WHITE
colors = [(255,0,0),(0,255,255),(255,255,0),(0,255,0),(0,0,255)]

dvdLogo = pygame.image.load("/home/wittu/My Stuff/TCS/Python/#Sprites/Dvd.png").convert_alpha()
dvdLogoScaled = pygame.transform.scale(dvdLogo, (160, 80))

# Make a white version of the logo
whiteLogo = dvdLogoScaled.copy()
whiteLogo.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_ADD)

def randomColor():
    hue = float(random.randint(0,255))
    value = 100.0
    saturation = 100.0

    #return colorsys.hls_to_rgb(hue, value, saturation)
    global colors
    number = random.randint(0, len(colors)-1)
    return colors[number]

def checkBounce():
    global color
    if (posx + w >= width-bounceRange or posx <= bounceRange) and (posy + h >= height-bounceRange or posy <= bounceRange):
        color = randomColor()

angle = 45
speed = 1
velx = math.cos(math.radians(angle))*speed

vely = math.sin(math.radians(angle))*speed

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(120)
    screen.fill(BLACK)
    if posx+w>=640 or posx<0:
        velx*=-1
        color = randomColor()
    if posy+h>=400 or posy<0:
        vely*=-1
        color = randomColor()
    posx+=velx
    posy+=vely
    checkBounce()
    
    coloredLogo = whiteLogo.copy()
    coloredLogo.fill(color, special_flags=pygame.BLEND_RGB_MULT)
    screen.blit(coloredLogo, (posx, posy))
    
    pygame.display.update()
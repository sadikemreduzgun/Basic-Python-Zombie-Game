# import the pygame module
import random
import pygame

# import pygame.locals for easier
# access to key coordinates
from pygame.locals import *
from funcs import *


# Define our square object and call super to
# give it all the properties and methods of pygame.sprite.Sprite
# Define the class for our square objects
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()

        # Define the dimension of the surface
        # Here we are making squares of side 25px
        self.surf = pygame.Surface((25, 25))

        # Define the color of the surface using RGB color coding.
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()


# initialize pygame
pygame.init()
zomb_boy = 25
# Define the dimensions of screen object
screen_x = 1250.0
screen_y = 620.0
screen = pygame.display.set_mode((screen_x, screen_y))

# instantiate all square objects
square1 = Square()
#square1 =
agam = pygame.image.load("Adsız.png").convert_alpha()
agam = pygame.transform.scale(agam, (25, 25))

# Variable to keep our game loop running
gameOn = True

x = screen_x/2
y = screen_y/2
# Our game loop
speed = 10
screen.blit(square1.surf, (x, y))
degisken_hatirla = 1

w_basili = False
a_basili = False
s_basili = False
d_basili = False

ates=False
# mermi konumu belirleme
mermi_yatay_x = 10
mermi_yatay_y = 10
mermi_dikey_x = 30
mermi_dikey_y = 10

yerlestir = False

# mermi sağ sol veya yukarı aşagğı ateş etme belirleme
# en son w bastıysak mesela yukarı mermi atması için
w_mermi = False
a_mermi = False
s_mermi = False
d_mermi = False

zombi1_canli=False
zombi2_canli=False
zombi3_canli=False
zombi4_canli=False

# x i 800 y si 600
c = 0

zombi1_rast_x = 1
zombi2_rast_x = 1
zombi3_rast_x = 1
zombi4_rast_x = 1

zombi1_rast_y = 1
zombi2_rast_y = 1
zombi3_rast_y = 1
zombi4_rast_y = 1

karakter_hizi = 0.2
zombi_hizi = 0.1

zombi_yukari = pygame.image.load('zombi_up.png').convert_alpha()
zombi_yukari = pygame.transform.scale(zombi_yukari, (zomb_boy, zomb_boy))

zombi_sag = pygame.image.load('zombi_right.png').convert_alpha()
zombi_sag = pygame.transform.scale(zombi_sag, (zomb_boy, zomb_boy))

zombi_asagi = pygame.image.load('zombi_down.png').convert_alpha()
zombi_asagi = pygame.transform.scale(zombi_asagi, (zomb_boy, zomb_boy))

zombi_sol = pygame.image.load('zombi_left.png').convert_alpha()
zombi_sol = pygame.transform.scale(zombi_sol, (zomb_boy, zomb_boy))

x = zombi_oldur(1,2,3,4,5,5)
print(x)
zombi1_yon = 0
zombi2_yon = 0
zombi3_yon = 0
zombi4_yon = 0

while gameOn:
    print(c)
    # for loop through the event queue
    #screen.fill((ran1,ram2,ram3))
    # ekranı siyaha boya her while döngüsünde
    screen.fill((0, 0, 0))
    #screen.blit(zombi_yukari, (screen_x/2, screen_y/2))

    if ates and d_mermi:
        mermi_yatay_x=mermi_yatay_x+1
    elif ates and w_mermi:
        mermi_dikey_y=mermi_dikey_y-1
    elif ates and a_mermi:
        mermi_yatay_x = mermi_yatay_x-1
    elif ates and s_mermi :
        mermi_dikey_y= mermi_dikey_y+1
    else:
        mermi_yatay_x = x
        mermi_yatay_y = y

        mermi_dikey_y = y
        mermi_dikey_x = x

    if mermi_yatay_x > screen_x:

        ates = False
    elif mermi_yatay_x < 0.0:
        ates=False
    elif mermi_dikey_y <0.0:
        ates=False
    elif mermi_dikey_y >screen_y:
        ates=False

    mermi_yatay = pygame.Rect(mermi_yatay_x, mermi_yatay_y, 5, 1)
    mermi_dikey = pygame.Rect(mermi_dikey_x, mermi_dikey_y, 1, 5)

    # zombi ata
    if not zombi1_canli:
        zombi1_rast_x = random.randint(0,int(screen_x))
        zombi1_rast_y = 1
        zombi1_canli = True
    else:

        if (zombi1_rast_x-x) < 0:
            zombi1_rast_x += zombi_hizi
            #screen.blit(zombi_sag, (zombi1_rast_x, zombi1_rast_y))

        else:
            zombi1_rast_x -= zombi_hizi
            #screen.blit(zombi_sol, (zombi1_rast_x, zombi1_rast_y))
        if (zombi1_rast_y-y) < 0:
            zombi1_rast_y += zombi_hizi
            #screen.blit(zombi_asagi, (zombi1_rast_x, zombi1_rast_y))
        else:
            zombi1_rast_y -= zombi_hizi
            #screen.blit(zombi_yukari, (zombi1_rast_x, zombi1_rast_y))
        zombi1_yon = give_direc(x, y, zombi1_rast_x, zombi1_rast_y, zombi_hizi)

    if not zombi2_canli:
        zombi2_rast_x = random.randint(0, int(screen_x))
        zombi2_canli = True
        zombi2_rast_y = screen_y-1
    else:
        if (zombi2_rast_x - x) < 0:
            zombi2_rast_x += zombi_hizi
            #screen.blit(zombi_sag, (zombi2_rast_x, zombi2_rast_y))

        else:
            zombi2_rast_x -= zombi_hizi

            #screen.blit(zombi_sol, (zombi2_rast_x, zombi2_rast_y))
        if (zombi2_rast_y - y) < 0:
            zombi2_rast_y += zombi_hizi

            #screen.blit(zombi_asagi, (zombi2_rast_x, zombi2_rast_y))
        else:
            zombi2_rast_y -= zombi_hizi

        zombi2_yon = give_direc(x, y, zombi2_rast_x, zombi2_rast_y, zombi_hizi)
            #screen.blit(zombi_yukari, (zombi2_rast_x, zombi2_rast_y))

    if not zombi3_canli:
        zombi3_rast_x = 1
        zombi3_rast_y = random.randint(0,int(screen_y))
        zombi3_canli = True
    else:
        if (zombi3_rast_x-x) < 0:
            zombi3_rast_x += zombi_hizi
            #screen.blit(zombi_sag, (zombi3_rast_x, zombi1_rast_y))
        else:
            zombi3_rast_x -= zombi_hizi
            #screen.blit(zombi_sag, (zombi3_rast_x, zombi1_rast_y))
        if (zombi3_rast_y-y) < 0:
            zombi3_rast_y += zombi_hizi
        else:
            zombi3_rast_y -= zombi_hizi

        zombi3_yon = give_direc(x,y,zombi3_rast_x, zombi3_rast_y, zombi_hizi)

    if not zombi4_canli:
        zombi4_rast_x = screen_x-1
        zombi4_rast_y = random.randint(0,int(screen_y))
        zombi4_canli = True
    else:
        if (zombi4_rast_x-x) < 0:
            zombi4_rast_x += zombi_hizi
            #screen.blit(zombi_sag, (zombi4_rast_x, zombi1_rast_y))
        else:
            zombi4_rast_x -= zombi_hizi
            #screen.blit(zombi_sag, (zombi4_rast_x, zombi1_rast_y))

        if (zombi4_rast_y-y) < 0:
            zombi4_rast_y += zombi_hizi
        else:
            zombi4_rast_y -= zombi_hizi

        zombi4_yon = give_direc(x,y,zombi4_rast_x,zombi4_rast_y,zombi_hizi)

    # zombi_oldur(mermi_yx, mermi_yy, mermi_dy, mermi_dx, zombi_x, zombi_y)
    zombi1_canli = zombi_oldur(mermi_yatay_x, mermi_yatay_y, mermi_dikey_x, mermi_dikey_y, zombi1_rast_x, zombi1_rast_y)
    zombi2_canli = zombi_oldur(mermi_yatay_x, mermi_yatay_y, mermi_dikey_x, mermi_dikey_y, zombi2_rast_x, zombi2_rast_y)
    zombi3_canli = zombi_oldur(mermi_yatay_x, mermi_yatay_y, mermi_dikey_x, mermi_dikey_y, zombi3_rast_x, zombi3_rast_y)
    zombi4_canli = zombi_oldur(mermi_yatay_x, mermi_yatay_y, mermi_dikey_x, mermi_dikey_y, zombi4_rast_x, zombi4_rast_y)

    blit_iy(zombi1_yon, zombi_yukari, zombi_sol, zombi_sag, zombi_asagi, zombi1_rast_x, zombi1_rast_y, screen)
    blit_iy(zombi2_yon, zombi_yukari, zombi_sol, zombi_sag, zombi_asagi, zombi2_rast_x, zombi2_rast_y, screen)
    blit_iy(zombi3_yon, zombi_yukari, zombi_sol, zombi_sag, zombi_asagi, zombi3_rast_x, zombi3_rast_y, screen)
    blit_iy(zombi4_yon, zombi_yukari, zombi_sol, zombi_sag, zombi_asagi, zombi4_rast_x, zombi4_rast_y, screen)
    """zombi1 = pygame.Rect(zombi1_rast_x, zombi1_rast_y, 15, 15)
    zombi2 = pygame.Rect(zombi2_rast_x,zombi2_rast_y , 15, 15)
    zombi3 = pygame.Rect(zombi3_rast_x, zombi3_rast_y, 15, 15)
    zombi4 = pygame.Rect(zombi4_rast_x, zombi4_rast_y, 15, 15)
    
    pygame.draw.rect(screen, (0, 255, 0), zombi1)
    pygame.draw.rect(screen, (0, 255, 0), zombi2)
    pygame.draw.rect(screen, (0, 255, 0), zombi3)
    pygame.draw.rect(screen, (0, 255, 0), zombi4)"""

    #screen.blit(zombi_yukari, (zombi1_rast_x, zombi1_rast_y))

    #
    #pygame.draw.rect(screen, (255, 255, 0), mermi_dikey)
    pygame.draw.rect(screen, (255, 255, 0), mermi_yatay)
    pygame.draw.rect(screen, (255, 255, 0), mermi_dikey)

    screen.blit(agam, (x, y))
    if w_basili:
        y -= karakter_hizi
    elif a_basili:
        x -= karakter_hizi
    elif s_basili:
        y += karakter_hizi
    elif d_basili:
        x = x + karakter_hizi

    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == K_BACKSPACE:
                gameOn = False
            elif event.key == K_w:
                y = y-speed
                w_basili = True
                a_basili = False
                s_basili = False
                d_basili = False

                w_mermi =True
                a_mermi = False
                s_mermi = False
                d_mermi =False
            elif event.key == K_a:
                x -= speed

                w_basili = False
                a_basili = True
                s_basili = False
                d_basili = False


                w_mermi =False
                a_mermi = True
                s_mermi = False
                d_mermi =False
            elif event.key == K_d:
                x += speed

                w_basili = False
                a_basili = False
                s_basili = False
                d_basili = True

                w_mermi =False
                a_mermi = False
                s_mermi = False
                d_mermi =True
            elif event.key == K_s:
                y += speed

                w_basili = False
                a_basili = False
                s_basili = True
                d_basili = False


                w_mermi =False
                a_mermi = False
                s_mermi = True
                d_mermi =False
            elif event.key==K_SPACE:
                ates=True

            degisken_hatirla = event.key
        # Check for QUIT event
        elif event.type == KEYUP:

            w_basili = False
            a_basili = False
            s_basili = False
            d_basili = False

        elif event.type == QUIT:
            gameOn = False
    c += 1
    # Define where the squares will appear on the screen
    # Use blit to draw them on the screen surface
    #screen.blit(square1.surf, (40, 40))

    # Update the display using flip
    #pygame.display.flip()
    pygame.display.update()
    #clock.tick(20)

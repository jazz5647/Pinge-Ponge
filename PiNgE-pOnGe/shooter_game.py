#Создай собственный Шутер!
 
#создай игру "Лабиринт"!
from pygame import *
from random import *
from time import time as timer

rel_time_end = 0

speed_x = 3
speed_y = 3

init()

myfont = font.SysFont('Arial', 30)

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, speed, imag, height, width, dv2, dv3):
        super().__init__()
        self.image = transform.scale(image.load(imag), (height, width))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.dv2 = dv2
        self.dv3 = 0
        #self.direction = "left"
    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def morpeh(self):
        if self.dv2 == 1:
            keypressed = key.get_pressed()
            if keypressed[K_UP] and self.rect.y >= 0:
                self.rect.y -= self.speed
            if keypressed[K_DOWN] and self.rect.y <= 400:
                self.rect.y += self.speed
        if self.dv2 == 2:
            keypressed = key.get_pressed()
            if keypressed[K_w] and self.rect.y >= 0:
                self.rect.y -= self.speed
            if keypressed[K_s] and self.rect.y <= 400:
                self.rect.y += self.speed


w = 700
h = 500
cellsize = 24
wcells = w//cellsize
hcells = h//cellsize
x, y = 30, 10
kx, ky = 500, 300
speed = 15
ch = 6
background = transform.scale(image.load("piingepoonge.png"), (w, h))
#background = transform.scale(image.load("fon2.jpg"), (w, h))


clock = time.Clock()
FPS = 50
win = display.set_mode((w,h))
win.blit(background, (0,0))
fashik = []



#player = Player(30, 400,speed, "shlupka.jpg", 65, 65)
player = Player(10, 350,speed, "pingepoonge.png", 20, 100, 2, 0)
player2 = Player(670, 350,speed, "pingepoonge.png", 20, 100, 1, 0)

cyborg = GameSprite(300, 200,speed, "piingeponge.png", 50, 50, -3, -3)
#bullet = Bullet(player.rect.x+20, player.rect.y+20,speed, "shlupka.jpg", 25, 25)

'''for i in range(ch-1):
    win.blit(background, (0, 0))
    player.morpeh()
    player.draw()
    bulletg.draw(win)
    bulletg.update()
    fashisty.draw(win)
    fashisty.update()
    text = myfont.render("Приготовься! У тебя "+str(ch-1)+" секунд(ы)!", 1, (255,0,0))
    win.blit(text,(100,100))
    display.update()
    time.delay(1000)
    ch -= 1
ch = 6'''

display.set_caption("hl2")

game = True
finish = False
if game == True:
    while game:
        background.fill((0,255,255))

        player.morpeh()
        player.draw()
        player2.morpeh()
        player2.draw()
        cyborg.update()
        cyborg.draw()
        '''bullet.draw()
        bullet.update()'''
        
        

        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    game = False
        
        if finish != True:
            cyborg.rect.x += speed_x
            cyborg.rect.y += speed_y
            if sprite.collide_rect(cyborg, player):
                speed_x = speed_x * -1

            if sprite.collide_rect(cyborg, player2):
                speed_x = speed_x * -1

            if cyborg.rect.y <= 0:
                speed_y = speed_y * -1

            if cyborg.rect.y >= 450:
                speed_y = speed_y * -1

            if cyborg.rect.x <= 10:
                finish = True
                text = myfont.render("Player 1 lose!", True, (255,0,0))
                win.blit(text,((w-text.get_width())//2,(h-text.get_height())//2))
                display.update()
                time.delay(3000)
                game = False

            if cyborg.rect.x >= 690:
                finish = True
                text = myfont.render("Player 2 lose!", True, (255,0,0))
                win.blit(text,((w-text.get_width())//2,(h-text.get_height())//2))
                display.update()
                time.delay(3000)
                game = False


        display.update()
        win.blit(background, (0, 0))
        clock.tick(FPS)

        
            
#quit()

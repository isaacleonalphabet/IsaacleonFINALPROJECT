#File Created by Isaac Leon 


# This file was created by: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

# import libs
import pygame 
import os
# import settings 
from settings import *
from sprites import *
from os import path
from os import path 
from math import floor
pygame.init()
# from pg.sprite import Sprite

# set up assets folders

'''
goal: Fall down the screen and say "you loose" and try to make a new platorm that disappears. 
'''

# create game class in order to pass properties to the sprites file

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

#Thsi is to create a timer 
class Cooldown():
    def __init__(self):
        self.current_time = 0
        self.event_time = 0
        self.delta = 0
    def ticking(self):
        self.current_time = floor((pg.time.get_ticks())/1000)
        self.delta = self.current_time - self.event_time
        # print(self.delta)
    def reset(self):
        self.event_time = floor((pg.time.get_ticks())/1000)
    def timer(self):
        self.current_time = floor((pg.time.get_ticks())/1000)

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        


    def load_data(self):
        self.player_img = pg.image.load(path.join(img_folder, "Doodle jump.jpg")).convert()


    def new(self):
        # starting a new game
        # added to load data
        self.load_data()
        #This puts the 'class' in play 
        self.cd = Cooldown()
        # starting a new game
        self.win = False 
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self, WIDTH/2, HEIGHT/2)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        
        self.all_sprites.add(self.player)

        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()

    
    def run(self):
        self.playing = True
        while self.playing:

            # This runs the timer 
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()

        # The code of when it is counting 
        self.cd.ticking()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            self.cd.ticking()
            if hits:
                # These two platforms will not disappear, they are my safe zones. 
                if hits[0].variant == "normal":
                    hits[0].kill()
                    # No matter how may times I hit them, they will not kill me (lose)
                elif hits[0].variant == "normal":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
    def draw(self):
        print(self.cd.delta)

        # This says how long it would tick and the message will pop out 
        if self.cd.delta < 2:
            self.draw_text("BEGIN!", 100, BLACK, WIDTH/2, HEIGHT/2)
    
         # self.draw_text(str(self.player.rot), 24, WHITE, WIDTH/2, HEIGHT/2)
            #This says that as long as I am on a platform I am winning 
             # Winning = I am on a platform 

             
        if self.win == pg.sprite.spritecollide(self.player, self.platforms, False):
            self.draw_text("KEEP SURVIVING!", 24, BLACK, WIDTH/2, HEIGHT/2)

             # Winning = I am on a platform 
        if self.player.rect.y > HEIGHT:
            self.draw_text("YOU LOSE", 50, RED, WIDTH/2, HEIGHT/2,)
# This says as long as I am not on a platform, I am loosing or I just lost because the platforms on the bottom will dissappear
    
        # is this a method or a function?
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()
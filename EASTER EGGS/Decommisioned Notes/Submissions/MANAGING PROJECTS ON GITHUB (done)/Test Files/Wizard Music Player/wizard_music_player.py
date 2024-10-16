# Initialization
import os
import pygame
from pygame import mixer
pygame.init()

# Dimensions
screenX = 1000
screenY = 620
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption('Music Player')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Time Decal(s)
clock = pygame.time.Clock()
spriterun = 27

# Texts & Fonts
pygame.font.get_fonts()
font = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.Font('freesansbold.ttf', 40)

# Important Coordinates
originX = 0
originY = 0
heavenX = 5000
heavenY = 5000

# colour codes
sky_blue = (0,155,255)
black = (0,0,0)
gray = (127,127,127)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
pink = (255,0,255)

screen.fill(black)

# Menu Sounds
menu_move = pygame.mixer.Sound("move.wav")
off = "silence.wav"

def slide():
    pygame.mixer.Sound.play(menu_move)

# Data Accessing
files = os.listdir('.')
musics = []
sounds = []

for file in files:
    if '.mp3' in file:
        musics.append(file)
    elif 'wav' in file:
        sounds.append(file)
    else:
        None

music1 = musics[0]
music2 = musics[1]
music3 = musics[2]
music4 = musics[3]
music5 = musics[4]
music6 = musics[5]
music7 = musics[6]
music8 = musics[7]
music9 = musics[8]
music10 = musics[9]
music11 = musics[10]

# Music Playing Function(s)
partX = 525
partY = 200
pp = pygame.image.load('pp.png')
def part(x,y):
    screen.blit(pp, [x,y])
part(partX,partY)

ppX = 565
ppY = 260
def paused(x,y):
    paused_text = font2.render('PAUSED', True, pink)
    screen.blit(paused_text,[x,y])

def playing(x,y):
    playing_text = font2.render('PLAYING', True, blue)
    screen.blit(playing_text,[x,y])

def pp0():
    part(partX,partY)
    paused(ppX,ppY)
pp0()

def pp1():
    part(partX,partY)
    playing(ppX,ppY)

def play(music):
    mixer.music.load(music)
    mixer.music.play()

# Making Shortcut Functions
def name(music,colour,x,y,glob):
    name = music.replace('.mp3','') 
    txt = font.render(name, True, colour)
    screen.blit(txt,[x,y])
    if colour == green:
        glob = True
    elif colour == red:
        glob = False

def ext(music,x,y):
    if '.mp3' in music:
        ext = 'Format: MP3'
    elif '.wav' in music:
        ext = 'Format: WAV'
    else:
        None
    extention = font.render(ext, True, yellow)
    screen.blit(extention,[x,y]) 

def play(music):
    mixer.music.load(music)
    mixer.music.play()

# Applied Functions
def top(x,y):
    top = pygame.image.load('top.png')
    screen.blit(top,[x,y])
top(originX,originY)

nameX = 50
nameY = 80
extX = 800
extY = 80
Ygap = 40

m1 = True
name(music1,green,nameX,nameY+Ygap*0,m1)
ext(music1,extX,extY+Ygap*0)

m2 = False
name(music2,red,nameX,nameY+Ygap*1,m2)
ext(music2,extX,extY+Ygap*1)

m3 = False
name(music3,red,nameX,nameY+Ygap*2,m3)
ext(music3,extX,extY+Ygap*2)

m4 = False
name(music4,red,nameX,nameY+Ygap*3,m4)
ext(music4,extX,extY+Ygap*3)

m5 = False
name(music5,red,nameX,nameY+Ygap*4,m5)
ext(music5,extX,extY+Ygap*4)

m6 = False
name(music6,red,nameX,nameY+Ygap*5,m6)
ext(music6,extX,extY+Ygap*5)

m7 = False
name(music7,red,nameX,nameY+Ygap*6,m7)
ext(music7,extX,extY+Ygap*6)

m8 = False
name(music8,red,nameX,nameY+Ygap*7,m8)
ext(music8,extX,extY+Ygap*7)

m9 = False
name(music9,red,nameX,nameY+Ygap*8,m9)
ext(music9,extX,extY+Ygap*8)

m10 = False
name(music10,red,nameX,nameY+Ygap*9,m10)
ext(music10,extX,extY+Ygap*9)

m11 = False
name(music11,red,nameX,nameY+Ygap*10,m11)
ext(music11,extX,extY+Ygap*10)

# Functions To Copy (Never call it to avoid crash)
def copy_func():
    name(music1,green,nameX,nameY+Ygap*0,m1)
    name(music2,red,nameX,nameY+Ygap*1,m2)
    name(music3,red,nameX,nameY+Ygap*2,m3)
    name(music4,red,nameX,nameY+Ygap*3,m4)
    name(music5,red,nameX,nameY+Ygap*4,m5)
    name(music6,red,nameX,nameY+Ygap*5,m6)
    name(music7,red,nameX,nameY+Ygap*6,m7)
    name(music8,red,nameX,nameY+Ygap*7,m8)
    name(music9,red,nameX,nameY+Ygap*8,m9)
    name(music10,red,nameX,nameY+Ygap*9,m10)
    name(music11,red,nameX,nameY+Ygap*10,m11)
    name(music1,green,nameX,nameY+Ygap*0,m1)
    
# Show Display 1
pygame.display.update()

# Keyboard Inputs
running = True
while running:

    pygame.time.delay(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_DOWN:
                print('Down Arrow, Pressed')
                slide()
                if m1 == True:
                    name(music1,red,nameX,nameY+Ygap*0,m1)
                    m1 = False
                    name(music2,green,nameX,nameY+Ygap*1,m2)
                    m2 = True
                elif m2 == True:
                    name(music2,red,nameX,nameY+Ygap*1,m2)
                    m2 = False
                    name(music3,green,nameX,nameY+Ygap*2,m3)
                    m3 = True
                elif m3 == True:
                    name(music3,red,nameX,nameY+Ygap*2,m3)
                    m3 = False
                    name(music4,green,nameX,nameY+Ygap*3,m4)
                    m4 = True
                elif m4 == True:
                    name(music4,red,nameX,nameY+Ygap*3,m4)
                    m4 = False
                    name(music5,green,nameX,nameY+Ygap*4,m5)
                    m5 = True
                elif m5 == True:
                    name(music5,red,nameX,nameY+Ygap*4,m5)
                    m5 = False
                    name(music6,green,nameX,nameY+Ygap*5,m6)
                    m6 = True
                elif m6 == True:
                    name(music6,red,nameX,nameY+Ygap*5,m6)
                    m6 = False
                    name(music7,green,nameX,nameY+Ygap*6,m7)
                    m7 = True
                elif m7 == True:
                    name(music7,red,nameX,nameY+Ygap*6,m7)
                    m7 = False
                    name(music8,green,nameX,nameY+Ygap*7,m8)
                    m8 = True
                elif m8 == True:
                    name(music8,red,nameX,nameY+Ygap*7,m8)
                    m8 = False
                    name(music9,green,nameX,nameY+Ygap*8,m9)
                    m9 = True
                elif m9 == True:
                    name(music9,red,nameX,nameY+Ygap*8,m9)
                    m9 = False
                    name(music10,green,nameX,nameY+Ygap*9,m10)
                    m10 = True
                elif m10 == True:
                    name(music10,red,nameX,nameY+Ygap*9,m10)
                    m10 = False
                    name(music11,green,nameX,nameY+Ygap*10,m11)
                    m11 = True
                elif m11 == True:
                    name(music11,red,nameX,nameY+Ygap*10,m11)
                    m11 = False
                    name(music1,green,nameX,nameY+Ygap*0,m1)
                    m1 = True
                else:
                    None
                print('Down Arrow, Released')

                # Show Display 2
                pygame.display.update()
                
            if event.key == pygame.K_UP:
                print('Up Arrow, Pressed')
                slide()
                if m2 == True:
                    name(music1,green,nameX,nameY+Ygap*0,m1)
                    m1 = True
                    name(music2,red,nameX,nameY+Ygap*1,m2)
                    m2 = False
                elif m3 == True:
                    name(music2,green,nameX,nameY+Ygap*1,m2)
                    m2 = True
                    name(music3,red,nameX,nameY+Ygap*2,m3)
                    m3 = False
                elif m4 == True:
                    name(music3,green,nameX,nameY+Ygap*2,m3)
                    m3 = True
                    name(music4,red,nameX,nameY+Ygap*3,m4)
                    m4 = False
                elif m5 == True:
                    name(music4,green,nameX,nameY+Ygap*3,m4)
                    m4 = True
                    name(music5,red,nameX,nameY+Ygap*4,m5)
                    m5 = False
                elif m6 == True:
                    name(music5,green,nameX,nameY+Ygap*4,m5)
                    m5 = True
                    name(music6,red,nameX,nameY+Ygap*5,m6)
                    m6 = False
                elif m7 == True:
                    name(music6,green,nameX,nameY+Ygap*5,m6)
                    m6 = True
                    name(music7,red,nameX,nameY+Ygap*6,m7)
                    m7 = False
                elif m8 == True:
                    name(music7,green,nameX,nameY+Ygap*6,m7)
                    m7 = True
                    name(music8,red,nameX,nameY+Ygap*7,m8)
                    m8 = False
                elif m9 == True:
                    name(music8,green,nameX,nameY+Ygap*7,m8)
                    m8 = True
                    name(music9,red,nameX,nameY+Ygap*8,m9)
                    m9 = False
                elif m10 == True:
                    name(music9,green,nameX,nameY+Ygap*8,m9)
                    m9 = True
                    name(music10,red,nameX,nameY+Ygap*9,m10)
                    m10 = False
                elif m11 == True:
                    name(music10,green,nameX,nameY+Ygap*9,m10)
                    m10 = True
                    name(music11,red,nameX,nameY+Ygap*10,m11)
                    m11 = False
                elif m1 == True:
                    name(music11,green,nameX,nameY+Ygap*10,m11)
                    m11 = True
                    name(music1,red,nameX,nameY+Ygap*0,m1)
                    m1 = False
                else:
                    None
                print('Up Arrow, Released')

                # Show Display 4
                pygame.display.update()

            if event.key == pygame.K_RETURN:
                print('Return Button, Pressed')

                def run():
                    global run
                    run = False
                    if run == False:
                        run = True
                    elif run == True:
                        run = False
                        
                pp1()
                if m1 == True:
                    play(music1)
                elif m2 == True:
                    play(music2)
                elif m3 == True:
                    play(music3)
                elif m4 == True:
                    play(music4)
                elif m5 == True:
                    play(music5)
                elif m6 == True:
                    play(music6)
                elif m7 == True:
                    play(music7)
                elif m8 == True:
                    play(music8)
                elif m9 == True:
                    play(music9)
                elif m10 == True:
                    play(music10)
                elif m11 == True:
                    play(music11)
                else:
                    None
                print(m1)
                print(run)
                print('Return Button, Released')

                # Show Display 4
                pygame.display.update()
         
# Show Display 5
pygame.display.update()

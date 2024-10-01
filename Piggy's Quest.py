#!/usr/local/bin/python3

import pygame
import sys
import time
import os

pygame.init()
size=[1280,600]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("Piggy's Quest")

done=False

clock = pygame.time.Clock()
timer = 0

# -------- Settings ----------------------

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

pig_list    = [172,174,173,189,188,189]
pig_frame_int   = 1
pig_frame_str   = '1'

c      = 50
c_list = [[0,0],[1,2],[0,1]]
c_1    = -13

x = 40
x_speed = 20
y = 0
v   = 0
v_f = 0
v_fs = 45
g = 5

standing = True
jumping  = False
pressed_left = False
pressed_right= False

# -------- Images ----------------------

bg          = pygame.image.load("Assets/bg.png")
ground_l    = pygame.image.load("Assets/volcano_pack_03.png")
ground_r    = pygame.image.load("Assets/volcano_pack_07.png")
ground      = pygame.image.load("Assets/volcano_pack_05.png")
platform    = pygame.image.load("Assets/volcano_pack_13.png")
platform_l  = pygame.image.load("Assets/volcano_pack_38.png")
platform_r  = pygame.image.load("Assets/volcano_pack_15.png")
pig_l_1     = pygame.image.load("Assets/pig left 1.png")
pig_l_2     = pygame.image.load("Assets/pig left 2.png")
pig_l_3     = pygame.image.load("Assets/pig left 3.png")
pig_r_3     = pygame.image.load("Assets/pig right 1.png")
pig_r_2     = pygame.image.load("Assets/pig right 2.png")
pig_r_1     = pygame.image.load("Assets/pig right 3.png")
coin        = pygame.image.load("Assets/coinGold.png")
gem         = pygame.image.load("Assets/gemBlue.png")
keyRed      = pygame.image.load("Assets/keyRed.png")

pig_r = pig_r_1
pig_l = pig_l_1
pig   = pig_r
pig_dict        =   {"1": pig_r_1,"2": pig_r_2,"3": pig_r_3}

# -------- Functions -------------------

# -------- Locations -------------------

coin_locations = []

# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        elif event.type == pygame.KEYDOWN:         
            if event.key == pygame.K_LEFT:
                pressed_left = True
            elif event.key == pygame.K_RIGHT:
                pressed_right = True
            elif event.key == pygame.K_SPACE or pygame.K_UP:
                if standing:
                    v_f = v_fs
                    jumping = True
                    standing = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressed_left = False
            elif event.key == pygame.K_RIGHT:
                pressed_right = False

    screen.fill(white)
    screen.blit(bg,[0,0])
    screen.blit(ground_l,[0,600-128])
    for k in range(1,9):
        screen.blit(ground,[128*k,600-128])
    screen.blit(ground_r,[1280-128,600-128])

    screen.blit(platform_l,[128*2,320])
    screen.blit(platform_r,[128*3,320])
    screen.blit(platform_l,[128*5,160])
    screen.blit(platform,[128*6,160])
    screen.blit(platform_r,[128*7,160])
    
    #for k in range(1,3):
     #   screen.blit(ground, 

    #----- Add the Coin

    


    if pressed_left:
        x -= x_speed
        pig_dict        =   {"1": pig_l_1,"2": pig_l_2,"3": pig_l_3}
        c_list          = [[0,0+c_1],[-2,-1+c_1],[0,0+c_1]]
    
    if pressed_right:
        x += x_speed
        pig_dict        =   {"1": pig_r_1,"2": pig_r_2,"3": pig_r_3}
        c_list          = [[0,0],[1,2],[0,1]]

    if jumping:
        v_f -= g
        v = int(v_f)
        y -= v
        if y > c_list[pig_frame_int-1][1]:
            jumping  = False
            standing = True
            v_f = 0
            y = 0

    pig = pig_dict[pig_frame_str]
    #print([y,(600-172+c_list[pig_frame_int-1][1]),v,jumping,standing])
    
    screen.blit(pig,[x+c_list[pig_frame_int-1][0],y+600-172+c_list[pig_frame_int-1][1]])

    if pressed_left or pressed_right == True:
        pig_frame_int = (((pig_frame_int + 1)%3)+1)
        pig_frame_str = str(pig_frame_int)

    timer += 1
    clock.tick(30)
    pygame.display.flip()
pygame.quit ()

# -*- coding: utf-8 -*-

#### B. Atkinson & J. Bozzela
#### snake_1.py
#### MP3
#### Software Design FA'15

"""
First itereation of Snake for Mini Project 3
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((640,480)) # set window size
background = pygame.Surface(screen.get_size()) # generate empty pygame surface
background.fill((255,255,255)) # background color fill
background = background.convert() # improve blitting

screen.blit(background, (0, 0))

for event in pygame.event.get():
    if event.type == pygame.QUIT: 
        mainloop = False # window closed
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            mainloop = False # ESC pressed event

pygame.quit()
# -*- coding: utf-8 -*-

#### B. Atkinson & J. Bozzela
#### snake_1.py
#### MP3
#### Software Design FA'15

"""
First itereation of Snake for Mini Project 3
"""

import pygame
import random
import math
import time

pygame.init()

screen_size = (640,480)
screen = pygame.display.set_mode(screen_size) # set window size

background = pygame.Surface(screen.get_size()) # generate empty pygame surface
background.fill((255,255,255)) # background color fill
background = background.convert() # improve blitting

screen.blit(background, (0, 0))

running = True
while running:
	for event in pygame.event.get():
	    if event.type == pygame.QUIT: 
	        running = False # window closed
	    elif event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_ESCAPE:
	            running = False # ESC pressed event

pygame.quit()
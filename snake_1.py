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
import sys

pygame.init()

screen_size = (640,480)
screen = pygame.display.set_mode(screen_size) # set window size

background = pygame.Surface(screen.get_size()) # generate empty pygame surface
background.fill((255,255,255)) # background color fill
background = background.convert() # improve blitting

screen.blit(background, (0, 0))

running = True
FPS = 30 #set max frame rate
total_time = 0.0 #initialize total play time counter
clock = pygame.time.Clock()

while running:
	milliseconds = clock.tick(FPS) 
	total_time += milliseconds / 1000.0 

	for event in pygame.event.get():
	    if event.type == pygame.QUIT: 
	        running = False # window closed
	    elif event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_ESCAPE:
	            running = False # ESC pressed event

	text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), total_time)
	pygame.display.set_caption(text)
	pygame.display.flip()

pygame.quit()
sys.exit()
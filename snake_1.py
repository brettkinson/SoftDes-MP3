# -*- coding: utf-8 -*-

#### B. Atkinson & J. Bozzella
#### snake_1.py
#### MP3
#### Software Design FA'15

"""
First itereation of Snake Game for Mini Project 3
"""

import pygame
import time
import sys
import random



class SnakeWorld:
	screen_size = (640,480)
	screen = pygame.display.set_mode(screen_size) # set window size

	background = pygame.Surface(screen.get_size()) # generate empty pygame surface
	background.fill((255,255,255)) # background color fill
	background = background.convert() # improve blitting

	screen.blit(background, (0, 0))

	snake_head = pygame.Surface((20,20))

	screen.blit(snake_head, (0,0))



class SnakeHead:
	def __init__(self,color,size,x,y,vx,vy):
		self.color = color
		self.size = size
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy


class SnakeTail:
	def __init__(self,color,size,x,y):
		self.color = color
		self.size = size
		self.x = x
		self.y = y


class Food:
	def __init__(self,color,size,x,y):
		self.color = color
		self.size = size
		self.x = x
		self.y = y


class PyGameWindow:
	def __init__(self,screen,world):
		screen_size = (640,480)
		screen = pygame.display.set_mode(screen_size) # set window size
		self.screen = screen

	def generate(self):
		background = self.screen # generate empty pygame surface
		background.fill((255,255,255)) # background color fill
		background = background.convert() # improve blitting
		screen.blit(background, (0, 0))


class GameController:
	def __init__(self,world):
		self.world = world
		
	def collide(x1, x2, y1, y2, w1, w2, h1, h2):  #Collision Test using Bounded Box Testing
		if x1 + w1 > x2 and x2 + w2 > x1 and y1 + h1 > y2 and y2 + h2 > y1:  #test if the position of the snake head falls within the rect designating the food
			return True
		else:
			return False
	    
	def keyboard_event(self,event):
		if event.type == pygame.QUIT: 
		    running = False #window closed

		elif event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_ESCAPE:
		        running = False #ESC pressed event

		    elif event.key == pygame.K_UP:
		    	if self.world.head.vx == 0 and self.world.head.vy == 10:
		    		return
		    	else:
		    		self.world.head.vx = 0
		    		self.world.head.vy = 10

		    elif event.key == pygame.K_DOWN:
		    	if self.world.head.vx == 0 and self.world.head.vy == -10:
		    		return
		    	else:
		    		self.world.head.vx = 0
		    		self.world.head.vy = -10

		    elif event.key == pygame.K_RIGHT:
		    	if self.world.head.vx == 10 and self.world.head.vy == 0:
		    		return
		    	else:
		    		self.world.head.vx = 10
		    		self.world.head.vy = 0

		    elif event.key == pygame.K_LEFT:
		    	if self.world.head.vx == -10 and self.world.head.vy == 0:
		    		return
		    	else:
		    		self.world.head.vx = -10
		    		self.world.head.vy = 0
		        	


if __name__ == '__main__':
	pygame.init()

	screen_size = (640,480)
	screen = pygame.display.set_mode(screen_size) #set window size
	world = SnakeWorld()
	controller = GameController(world)
	game_view = PyGameWindow(screen,world)

	running = True #initialize game state
	FPS = 30 #set max frame rate
	total_time = 0.0 #initialize total play time counter
	clock = pygame.time.Clock()


	while running:
		milliseconds = clock.tick(FPS) 
		total_time += milliseconds / 1000.0 

		text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), total_time)
		pygame.display.set_caption(text)
		pygame.display.flip()


		pygame.draw.rect(background,(0,0,0),(300,200,40,40),0)
		pygame.draw.rect(snake_head,(133,192,122),(0,0,20,20),0)

		
	pygame.quit()
	sys.exit()
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



class SnakeWorld():
	def __init__(self):

		self.xlocal = [] #initialize lists to store head locations
		self.ylocal = []
		self.tails = [] #list to keep track of number of tails

		self.head = SnakeHead((0,255,0),320,240,10,10,0,10)
		self.food = Food((random.randint(0,255),random.randint(0,255),random.randint(0,255)),10,10,random.randint(10,630),random.randint(10,470))
		self.headRect = pygame.Rect(self.head.x,self.head.y,self.head.width,self.head.height)
		self.foodRect = pygame.Rect(self.food.x,self.food.y,self.food.width,self.food.height)

	def update(self):
		self.xlocal.append(self.head.x)
		self.ylocal.append(self.head.y)
		self.head.update()
		self.headRect = pygame.Rect(self.head.x,self.head.y,self.head.width,self.head.height)

		if self.headRect.colliderect(self.foodRect):
			self.food.update(random.randint(10,630),random.randint(10,470))
			tail = SnakeTail((0,255,0),10,10,self.head.x,self.head.y)
			self.tails.append(tail)
		else:
			pass
			
	def check_dead(self):
		for t in self.tail:
			if self.headRect.colliderect(self.tail[

class SnakeHead():
	def __init__(self,color,x,y,width,height,vx,vy):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vx = vx
		self.vy = vy

	def update(self):
		self.x += self.vx
		self.y += self.vy


class SnakeTail():
	def __init__(self,color,x,y,width,height):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def update(self,xlocal,ylocal):
		self.x = xlocal
		self.y = ylocal


class Food():
	def __init__(self,color,x,y,width,height):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def update(self,x_new,y_new):
		self.x = x_new
		self.y = y_new


class PyGameWindow():
	def __init__(self,world):
		screen_size = (640,480)
		self.screen = pygame.display.set_mode(screen_size) #set window size
		self.world = world

	def generate(self):
		self.screen.fill((255,255,255)) #background color fill
		#self.screen = self.screen.convert() #improve blitting
		self.screen.blit(self.screen, (0, 0))
		for item in self.world.tails:
			pygame.draw.rect(self.screen, pygame.Color(item.color[0],item.color[1],item.color[2]),pygame.Rect(item.x,item.y,item.width,item.height))
		pygame.draw.rect(self.screen, pygame.Color(self.world.food.color[0],self.world.food.color[1],self.world.food.color[2]),pygame.Rect(self.world.food.x,self.world.food.y,self.world.food.width,self.world.food.height))
		pygame.draw.rect(self.screen, pygame.Color(self.world.head.color[0],self.world.head.color[1],self.world.head.color[2]),pygame.Rect(self.world.head.x,self.world.head.y,self.world.head.width,self.world.head.height))
		for item in self.world.tails:
			pygame.draw.rect(self.screen, pygame.Color(item.color[0],item.color[1],item.color[2]),pygame.Rect(item.x,item.y,item.width,item.height))


class GameController():
	def __init__(self,world):
		self.world = world
	    
	def keyboard_event(self,event):
		if event.key == pygame.K_ESCAPE:
			running = False #ESC pressed event

		elif event.key == pygame.K_UP:
			if self.world.head.vx == 0 and self.world.head.vy == -10:
				return
			else:
				self.world.head.vx = 0
				self.world.head.vy = -10

		elif event.key == pygame.K_DOWN:
			if self.world.head.vx == 0 and self.world.head.vy == 10:
				return
			else:
				self.world.head.vx = 0
				self.world.head.vy = 10

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

	#screen_size = (640,480)
	#screen = pygame.display.set_mode(screen_size) #set window size
	world = SnakeWorld()
	controller = GameController(world)
	game_view = PyGameWindow(world)
	game_view.generate()

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

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				controller.keyboard_event(event)

		game_view.generate()
		world.update() 
		time.sleep(.1)
		pygame.display.flip()

			
	pygame.quit()
	sys.exit()
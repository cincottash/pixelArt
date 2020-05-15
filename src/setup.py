from globals import *
import pygame

def setup():
	pygame.init()
	canvas = pygame.display.set_mode((canvasWidth, canvasHeight))

	image = pygame.image.load("assets/earth.jpg")

	return canvas, image
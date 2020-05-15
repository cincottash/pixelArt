from globals import *
import pygame

def setup():
	canvas = pygame.display.set_mode((canvasWidth, canvasHeight))
	try:
		picDir = sys.argv[1]
		image = pygame.image.load("assets/{}".format(picDir))
	except IndexError:
		print("Please supply an image")
		exit(0)

	return canvas, image
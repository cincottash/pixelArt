from globals import *
from exceptions import *
import sys
import pygame

def setup():
	try:
		if(len(sys.argv) == 1 or len(sys.argv) > 3):
			raise generalError
		elif(len(sys.argv) == 2):
			raise missingBlockSizeError
		else:
			picDir = sys.argv[1]
			image = pygame.image.load("assets/{}".format(picDir))
			blockSize = int(sys.argv[2])
			canvas = pygame.display.set_mode((canvasWidth, canvasHeight))
	except missingBlockSizeError:
		print("Please supply a block size")
		exit(0)
	except generalError:
		print("Error incorrect arguments, usage is: python3 main.py image blockSize")
		exit(0)

	return canvas, image, blockSize

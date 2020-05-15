from setup import *

def main():
	canvas, picture = setup()
	ranOnce = 0
	while(True):
		#BLITS AT TOP LEFT COORDS (0,0)
		canvas.blit(picture, (0, 0))

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if(event.key == pygame.K_RETURN):
					exit(0)
		#Iterate over canvas by block
		if(ranOnce == 0):
			for i in range(canvasWidth//blockSize):
				for j in range(canvasHeight//blockSize):
					pixelStartX = i * blockSize
					pixelStartY = j * blockSize
					
					#COMPUTE AVG RGB PER BLOCK
					avgR = 0
					avgG = 0
					avgB = 0
					#iterate by pixel over block
					for pixelX in range(blockSize):
						for pixelY in range(blockSize):
							pixel = canvas.get_at((pixelStartX + pixelX, pixelStartY + pixelY))
							avgR += pixel[0]
							avgG += pixel[1]
							avgB += pixel[2]
					#Normalize
					avgR = avgR/(blockSize**2)
					avgG = avgG/(blockSize**2)
					avgB = avgB/(blockSize**2)
					#Again iterate over that block but this time set each pixel to the avg RGB
					for pixelX in range(blockSize):
						for pixelY in range(blockSize):
							canvas.set_at((pixelStartX + pixelX, pixelStartY + pixelY), (avgR, avgG, avgB))

					pygame.display.update()
		ranOnce = 1


if __name__ == '__main__':
	main()
import sys
canvasWidth = 1000
canvasHeight = 1000

try:
	blockSize = int(sys.argv[2])
except IndexError:
	print("Please supply a block size")
	exit(0)
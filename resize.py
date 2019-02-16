# os module used to access the image in the given location

import os

# openCV module used to resize the image and covert the image as black and white

import cv2

def imConvertor(path, newRatio):
	''' [ Resize and Convert to black & white ]

		Arguments:
			@ path -- Path to search the image
			@ newRatio -- New ratio for the image

		Vaiables:
			@ image -- To read image from given directory
			@ gray_image -- Used convert the image into black and white
			@ ratio -- New image ratio
			@ dimesion -- New image heigth and width
			@ resize -- Resizing image based on the given @dimension
			@ count -- used to give names to new image 
	'''
	count = 1
	for root, dirs, images in os.walk(path):
		for img in images:
			image = cv2.imread(path+ "/"+ img)
			gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			ratio = newRatio / gray_image.shape[1]
			dimension = (newRatio, int(gray_image.shape[0] * ratio))
			resize = cv2.resize(gray_image, dimension, interpolation = cv2.INTER_AREA)
			cv2.imwrite("plate"+str(count)+".jpg", resize)
			count += 1

	


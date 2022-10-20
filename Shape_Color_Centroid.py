import numpy as np
import cv2
 
#reading the image
img = cv2.imread('Shape_Color_Centroid.jpeg')
cv2.imshow(img)

detected_shapes = []

#converting rgb to hsv
hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow("xyz",hsvFrame)

#converting to grey scale to identify shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#setting threshold for grey scale
_, threshold = cv2.threshold(gray, 180, 30, cv2.THRESH_BINARY)

#set range for red colour and define mask
red_lower = np.array([0, 50, 50], np.uint8)
red_upper = np.array([10, 255, 255], np.uint8)
red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

#set range for green colour and define mask
green_lower = np.array([36, 25, 25], np.uint8)
green_upper = np.array([86, 255, 255], np.uint8)
green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

#set range for blue colour and define mask
blue_lower = np.array([110, 50, 50], np.uint8)
blue_upper = np.array([130, 255, 255], np.uint8)
blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

#set range for orange colour and define mask
orange_lower = np.array([1,190,200], np.uint8)
orange_upper = np.array([25,255,255], np.uint8)
orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)

#set range for yellow colour and define mask
yellow_lower = np.array([22,60,200], np.uint8)
yellow_upper = np.array([50,255,255], np.uint8)
yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)	

#morphological transform, dilation for each colour and bitwise and operator between img and mask determines to detect only that particular colour
kernal = np.ones((5, 5), "uint8")
	
#red mask
red_mask = cv2.dilate(red_mask, kernal)
res_red = cv2.bitwise_and(img, img,
							mask = red_mask)
	
#green mask
green_mask = cv2.dilate(green_mask, kernal)
res_green = cv2.bitwise_and(img, img,
								mask = green_mask)
	
#blue mask
blue_mask = cv2.dilate(blue_mask, kernal)
res_blue = cv2.bitwise_and(img, img,
							mask = blue_mask)

#orange mask
orange_mask = cv2.dilate(orange_mask, kernal)
res_orange = cv2.bitwise_and(img, img,
								mask = orange_mask)

#yellow mask
yellow_mask = cv2.dilate(yellow_mask, kernal)
res_yellow = cv2.bitwise_and(img, img,
								mask = yellow_mask)


#contour for red colour
contours, hierarchy = cv2.findContours(red_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)

	
for pic, contour in enumerate(contours):
	
	shape = []
	a = "Red"
	approx = cv2.approxPolyDP(
		contour, 0.03 * cv2.arcLength(contour, True), True)
	if len(approx) == 3:
		b = "Triangle"

	elif len(approx) == 4:
		x1,y1,w,h = cv2.boundingRect(contour)
		aspectratio = float(w)/h
		if (0.95<aspectratio<1.05):
			b = "Square"
		else:
			b = "Rectangle"
		
	elif len(approx) == 5:
		b = "Pentagon"

	elif len(approx) == 6:
		b = "Hexagon"

	else:
		b = "Circle"

	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])

	centroid = (x, y)
	shape.append(a)
	shape.append(b)
	shape.append(centroid)
	detected_shapes.append(shape)


#contour for green colour
contours, hierarchy = cv2.findContours(green_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
for pic, contour in enumerate(contours):
	
	shape = []
	a = "Green"
	approx = cv2.approxPolyDP(
		contour, 0.04 * cv2.arcLength(contour, True), True)
	if len(approx) == 3:
		b = "Triangle"

	elif len(approx) == 4:
		x1,y1,w,h = cv2.boundingRect(contour)
		aspectratio = float(w)/h
		if (0.95<aspectratio<1.05):
			b = "Square"
		else:
			b = "Rectangle"
		
	elif len(approx) == 5:
		b = "Pentagon"

	elif len(approx) == 6:
		b = "Hexagon"

	else:
		b = "Circle"

	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])

	centroid = (x, y)
	shape.append(a)
	shape.append(b)
	shape.append(centroid)
	detected_shapes.append(shape)

#contour for blue colour
contours, hierarchy = cv2.findContours(blue_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
	
	shape = []
	a = "Blue"
	approx = cv2.approxPolyDP(
		contour, 0.04 * cv2.arcLength(contour, True), True)
	if len(approx) == 3:
		b = "Triangle"

	elif len(approx) == 4:
		x1,y1,w,h = cv2.boundingRect(contour)
		aspectratio = float(w)/h
		if (0.95<aspectratio<1.05):
			b = "Square"
		else:
			b = "Rectangle"
		
	elif len(approx) == 5:
		b = "Pentagon"

	elif len(approx) == 6:
		b = "Hexagon"

	else:
		b = "Circle"

	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])

	centroid = (x, y)
	shape.append(a)
	shape.append(b)
	shape.append(centroid)
	detected_shapes.append(shape)

#contour for orange colour
contours, hierarchy = cv2.findContours(orange_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
	
	shape = []
	a = "Orange"
	approx = cv2.approxPolyDP(
		contour, 0.03 * cv2.arcLength(contour, True), True)
	if len(approx) == 3:
		b = "Triangle"

	elif len(approx) == 4:
		x1,y1,w,h = cv2.boundingRect(contour)
		aspectratio = float(w)/h
		if (0.95<aspectratio<1.05):
			b = "Square"
		else:
			b = "Rectangle"
		
	elif len(approx) == 5:
		b = "Pentagon"

	elif len(approx) == 6:
		b = "Hexagon"

	else:
		b = "Circle"

	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])

	centroid = (x, y)
	shape.append(a)
	shape.append(b)
	shape.append(centroid)
	detected_shapes.append(shape)
	
#contour for yellow colour
contours, hierarchy = cv2.findContours(yellow_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
	
	shape = []
	a = "Yellow"
	approx = cv2.approxPolyDP(
		contour, 0.01 * cv2.arcLength(contour, True), True)
	if len(approx) == 3:
		b = "Triangle"

	elif len(approx) == 4:
		x1,y1,w,h = cv2.boundingRect(contour)
		aspectratio = float(w)/h
		if (0.95<aspectratio<1.05):
			b = "Square"
		else:
			b = "Rectangle"
		
	elif len(approx) == 5:
		b = "Pentagon"

	elif len(approx) == 6:
		b = "Hexagon"

	else:
		b = "Circle"

	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])

	centroid = (x, y)
	shape.append(a)
	shape.append(b)
	shape.append(centroid)
	detected_shapes.append(shape)

print(detected_shapes)
#final window with required output
cv2.imshow("Rubic cube colour detection", img)

#escape sequence for closing the final window
cv2.waitKey() 
cv2.destroyAllWindows() 

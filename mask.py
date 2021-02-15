import cv2

import numpy as np

image = cv2.imread('images/pizza.jpg')
print('Image is :', image.shape)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


lower_array = np.array([0,0,230])
upper_array = np.array([60,60,255])
mask = cv2.inRange(image,lower_array, upper_array)
masked_image = np.copy(image)

masked_image [mask!=0] = [255,250,220]

background = cv2.imread('images/phone.jpg')
background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
crop_background = background[0:179, 0:281]
crop_background[mask == 0] = [0,0,0]

complete_image = crop_background + masked_image

print(complete_image.shape)


low_threshold = 50
high_threshold = 200
edges = cv2.Canny(complete_image, low_threshold, high_threshold)

rho = 1
theta = np.pi/180
threshold =60                       #min number of hough space intersection to detect a line
max_line_length=130
max_line_gap = 5

lines = cv2.HoughLinesP(edges,rho,theta, threshold, np.array([]), max_line_length,max_line_gap)
line_images = np.copy(complete_image)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_images,(x1,y1),(x2,y2),(210,100,140),5)



cv2.destroyAllWindows()
cv2.imshow('Pizza',line_images)
#cv2.imshow('OP22',complete_image)
cv2.waitKey(0)
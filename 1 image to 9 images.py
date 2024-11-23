import math

import cv2
import numpy


image = cv2.imread(r"E:\MY FILES\Wallpapers\20230530_233736.jpg")
reszed_img = cv2.resize(image,(900,900), interpolation=cv2.INTER_LINEAR)
grayed_img = cv2.cvtColor(reszed_img, cv2.COLOR_BGR2GRAY)
img1 = numpy.zeros((100,100,1),numpy.uint8)
img2 = numpy.zeros((100,100,1),numpy.uint8)
img3 = numpy.zeros((100,100,1),numpy.uint8)
img4 = numpy.zeros((100,100,1),numpy.uint8)
img5 = numpy.zeros((100,100,1),numpy.uint8)
img6 = numpy.zeros((100,100,1),numpy.uint8)
img7 = numpy.zeros((100,100,1),numpy.uint8)
img8 = numpy.zeros((100,100,1),numpy.uint8)
img9 = numpy.zeros((100,100,1),numpy.uint8)
def get_neighborhood(img , y, x):
    neighborhood = [[0,0,0],[0,0,0], [0,0,0] ]

    neighborhood[0][0] = img[y - 1, x - 1 ]
    neighborhood[0][1] = img[y - 1, x ]
    neighborhood[0][2] = img[y - 1, x + 1]
    neighborhood[1][0] = img[y , x - 1]
    neighborhood[1][1] = img[y , x ]
    neighborhood[1][2] = img[y , x + 1]
    neighborhood[2][0] = img[y + 1, x - 1]
    neighborhood[2][1] = img[y +1, x ]
    neighborhood[2][2] = img[y +1, x + 1]

    return neighborhood

for y in range(1, 900, 3):
    for x in range (1, 900, 3):
        Mask = get_neighborhood(grayed_img ,y,x)

        colomn = math.floor(x/3)
        row = math.floor(y/3)
        colomn = colomn % 100
        row = row % 100

        img1[row , colomn] = Mask[0][0]
        img2[row, colomn] = Mask[0][1]
        img3[row, colomn] = Mask[0][2]
        img4[row, colomn] = Mask[1][0]
        img5[row, colomn] = Mask[1][1]
        img6[row, colomn] = Mask[1][2]
        img7[row, colomn] = Mask[2][0]
        img8[row, colomn] = Mask[2][1]
        img9[row, colomn] = Mask[2][2]


cv2.imshow("First image",image)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)
cv2.imshow("img5", img5)
cv2.imshow("img6", img6)
cv2.imshow("img7", img7)
cv2.imshow("img8", img8)
cv2.imshow("img9", img9)
cv2.waitKey(0)
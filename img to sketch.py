import cv2
#.............................thankyou for breaking my heart darling!....................
image=cv2.imread("me1.jpg")

#....this code convert image to gray image........
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#.....this code convert negative image to positive image.......
inverted=255-gray_image

#......this code convert image to blurred from of image
blurred=cv2.GaussianBlur(inverted,(21,21),0)

#.......this code converted blurred image to invertedblur(negative from)
invertedblur=255-blurred

#.......this code converted image to pencilsketch........
pencilsketch=cv2.divide(gray_image,invertedblur,scale=256.0)



#.......save the file
cv2.imwrite("me-grayscale.jpg", gray_image)
print("............successfuly converted into grayscale.........")
cv2.imwrite("me-sketch.jpg", pencilsketch)
print("............successfuly converted into pencilsketch.........")
cv2.imwrite("me-inverted.jpg", inverted)
print("............successfuly converted into invertedimage.........")

cv2.imshow("grayscale",gray_image)
cv2.imshow("sketch",pencilsketch)
cv2.imshow("inverted",inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("............proccess finished enjoy your day.........")
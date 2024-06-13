import cv2

img = cv2.imread('solar-system.jpg')
cv2.putText(img , "SUN", (20,220),fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0,0,255))
cv2.imshow('Sun',img)
cv2.waitKey(0)

cv2.putText(img , "Earth", (300,220),fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=.5, color=(0,0,255))
cv2.imshow('Earth',img)
cv2.waitKey(0)

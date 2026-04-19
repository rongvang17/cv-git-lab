import cv2
from image_utils import resize_image, to_gray
from detector import detect_objects

img = cv2.imread("test.jpg")
img = resize_image(img)

detections = detect_objects(img)
gray = to_gray(img)

cv2.imwrite("output.jpg", gray)
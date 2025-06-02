import cv2 as cv
import sys

img = cv.imread('starry_night.jpg') # returns a numpy array
cv.imshow("Sample window",img) # displays the image loaded by imread. Needs a string, image array data
if img is None:
    sys.exit("Could not find the image")
key = cv.waitKey(0)
if key == ord("k"):
    cv.imwrite("starry_night.jpg",img) # writes the image(modified/same) back to computer storage

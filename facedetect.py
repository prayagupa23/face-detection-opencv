import cv2 as cv
import sys
import numpy as np

# cam = cv.VideoCapture(0)
# frame_wid = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
# frame_height= int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

# fourcc = cv.VideoWriter_fourcc(*'mp4v')
# out= cv.VideoWriter('output.mp4',fourcc,20.0,(frame_wid,frame_height))

# while True:
#     ret, frame = cam.read()
#     out.write(frame)
#     cv.imshow("Camera",frame)
#     if cv.waitKey(0) == ord("q"):
#         break

# cam.release()
# out.release()
# cv.destroyAllWindows()

img = cv.imread('starry_night.jpg') # returns a numpy array

# after reading, the image data will be stored in 'cv::Mat' or 'Mat' object.

if img is None:
    sys.exit("Could not find the image")

cv.imshow("Sample window",img) # displays the image loaded by imread. Needs a string, image array data

# In Python, the image data is stored as a NumPy array (np.ndarray).

key = cv.waitKey(0)
if key == ord("k"):
    cv.imwrite("starry_night_copy.png",img) # writes the image(modified/same) back to computer storage
cv.destroyAllWindows()
print("All open cv windows closed")
print("Script executed successfully")


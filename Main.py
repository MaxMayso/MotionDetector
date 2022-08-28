import cv2 #import cv2 for file processing
import time

#method that triggers video capture object, can provide path of video file in 
#tuple, or a single integer. Single integer calls from camera because each camera is
#assigned and index number. Only one webcam is usually "0".. 
#UPDATE : can also generate and pull video from mobile devices that have a camera that can generate
#an IP adress, such as DSLR's, cellphones, GoPros, and 

video = cv2.VideoCapture(0) 

while True:    
    
    #This code is the framework for the motion sensor program, please adjust accordingly to course
    #on Udemy. Python Mastery Course Section 19 - Lecture 2

    check, frame = video.read() #boolean data type and numpy array
            
    img = cv2.cvtColor(frame, cv2.COLOR_RGBA2YUV_IYUV)

    cv2.imshow("Capturing", img)

    key = cv2.waitKey(1) #in while loop, continously takes video capture every 1 Millisecond consecutively 
                    #to create the video
    print(img)

    if (key == ord('x')):
        break
    

video.release() #releasing the camera, Python is starting the camera and then releasing the camera
cv2.destroyAllWindows()

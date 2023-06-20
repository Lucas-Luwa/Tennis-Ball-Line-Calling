import cv2
import imutils
import pygame
import time

pygame.init()

#Use the two commented out lines for IPWebcam
# camera1 = cv2.VideoCapture('https://128.61.77.18:8080/video')
# camera2 = cv2.VideoCapture('http://128.61.71.19:8080/video')

#VideoCapture ports may be different.
camera1 = cv2.VideoCapture(2)
camera2 = cv2.VideoCapture(3)

#Change out the audio file for a different sound
my_sound = pygame.mixer.Sound('buzzer.wav')

#Original Testing Values Indoors:
# ballColorLower = (25, 130, 50)
# ballColorUpper = (40, 255, 255)

#Final Ball Colors
ballColorLower = (25, 130, 50)
ballColorUpper = (100, 255, 255)

#Old Values
# ballColorLower = (0, 150, 150)
# ballColorUpper = (255,255,255)

triggeredSound = False
init = time.time()
while True:
    coreX = None
    coreY = None
    core2X = None
    core2Y = None

    #Grab values from cameras
    rv1, image = camera1.read()
    rv2, image2 = camera2.read()

    #Get dimensions of images and black out certain pixels
    width = image.shape[0]
    height = image.shape[1]
    for i in range(width):
        for j in range(height):
            if i < 60:
                image[i][j] = (0,0,0)

    #Resize Image
    image = imutils.resize(image, width=550)
    image2 = imutils.resize(image2, width=550)

    #Blur and convert to hsv C1
    gaussBlurImg = cv2.GaussianBlur(image, (9, 9), cv2.BORDER_DEFAULT)
    HSVResult = cv2.cvtColor(gaussBlurImg, cv2.COLOR_BGR2HSV)

    #Blur and convert to HSV C2
    gaussBlurImg2 = cv2.GaussianBlur(image2, (9, 9), cv2.BORDER_DEFAULT)
    HSVResult2 = cv2.cvtColor(gaussBlurImg2, cv2.COLOR_BGR2HSV)

    #Process data to reduce noise
    #Camera 1
    filter = cv2.inRange(HSVResult, ballColorLower, ballColorUpper)
    filterErode = cv2.erode(filter, None, iterations=3)
    filterDilate = cv2.dilate(filterErode, None, iterations=2)
    #Second Camera
    filter2 = cv2.inRange(HSVResult2, ballColorLower, ballColorUpper)
    filterErode2 = cv2.erode(filter2, None, iterations=3)
    filterDilate2 = cv2.dilate(filterErode2, None, iterations=2)

    # processing = cv2.vconcat([image, mask])
    extractedContours = cv2.findContours(filterDilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    extractedContours = imutils.grab_contours(extractedContours)

    # processing = cv2.vconcat([image, mask])
    extractedContours2 = cv2.findContours(filterDilate2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    extractedContours2 = imutils.grab_contours(extractedContours2)

    if len(extractedContours) > 0 and len(extractedContours2) > 0:
        proposedBall1 = max(extractedContours, key=cv2.contourArea)
        proposedBall2 = max(extractedContours2, key = cv2.contourArea)
        ((x1, y1), r) = cv2.minEnclosingCircle(proposedBall1)
        cam1Moments = cv2.moments(proposedBall1)
        ((x2, y2), r2) = cv2.minEnclosingCircle(proposedBall2)
        cam2Moments = cv2.moments(proposedBall2)
        coreX = int(cam1Moments["m10"] / cam1Moments["m00"])
        coreY = int(cam1Moments["m01"] / cam1Moments["m00"])
        core2X = int(cam2Moments["m10"] / cam2Moments["m00"])
        core2Y = int(cam2Moments["m01"] / cam2Moments["m00"])
        
        #perhaps modify this if its picking up too much trash
        if r > 3 and r2 > 3:
            # print(time.time())
            # print("hi")
            # print(time.time() - init > 10)

            #Depending on orientation of phone, you may need to adjust this.
            if (core2Y > 104 or core2X > 130) and not triggeredSound and time.time() - init > 2:
                triggeredSound = True
                my_sound.play()
                init = time.time()

            cv2.circle(image, (int(x1), int(y1)), int(r), (50, 205, 50), 1)
            cv2.circle(image, (coreX, coreY), 5, (255, 165, 0), -1)
            cv2.circle(image2, (int(x2), int(y2)), int(r2), (50, 205, 50), 1)
            cv2.circle(image2, (core2X, core2Y), 5, (255, 165, 0), -1)
        triggeredSound = False

    processing = cv2.hconcat([image, image2])
    cv2.imshow('Video Stream', processing)

    #If you hit escape, the program will halt
    if cv2.waitKey(1) == 27:
    	break

#Close program and release cameras  
camera1.release()
camera2.release()
cv2.destroyAllWindows()

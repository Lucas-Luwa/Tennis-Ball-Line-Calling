import cv2
camera1 = set_Camera(0)
camera2 = set_Camera(1)
while True:
    rv1, image1 = camera1.read()
    rv2, image2 = camera2.read()
    cv2.imshow('Port View Left', image1)
    cv2.imshow('Port View Front', image2)
    if cv2.waitKey(1) == 27:
        break
camera1.release()
camera2.release()
cv2.destroyAllWindows()
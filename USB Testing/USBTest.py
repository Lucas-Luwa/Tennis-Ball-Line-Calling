import cv2
videoCapture1 = cv2.VideoCapture(2)
videoCapture3 = cv2.VideoCapture(0)
videoCapture2 = cv2.VideoCapture(3)
while True:
    rv1, image1 = videoCapture1.read()
    rv2, image2 = videoCapture2.read()
    rv3, image3 = videoCapture3.read()
    proc = cv2.hconcat([image1, image2, image3])
    cv2.imshow('Port View',proc)
    if cv2.waitKey(1) == 27:
        break
videoCapture1.release()
videoCapture2.release()
videoCapture3.release()
cv2.destroyAllWindows()
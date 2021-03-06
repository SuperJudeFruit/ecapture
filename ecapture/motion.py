def motion_detect(camera_index, key_for_exit,threshold,window_name):
    import cv2
    import time
    import os
    import numpy as np
    import sys
    from skimage.measure import compare_ssim
    from skimage.transform import resize
    from scipy.ndimage import imread

    #Capture video from webcam
    cam = cv2.VideoCapture(camera_index)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        cv2.imwrite("1.jpg",img) #save image
    vid_capture = cv2.VideoCapture(camera_index)

    vid_cod = cv2.VideoWriter_fourcc(*'XVID')

    output = cv2.VideoWriter("test.avi", vid_cod, 20.0, (640,480))
    while(True):
    
        # Capture each frame of webcam video
        ret,frame = vid_capture.read()
        cv2.imwrite("2.jpg", frame)


    # get two images - resize both to 1024 x 1024
        img_a = cv2.imread("1.jpg")
        img_b = cv2.imread("2.jpg")

    # score: {-1:1} measure of the structural similarity between the images
        score, diff = compare_ssim(img_a, img_b, full=True, multichannel=True)
        if score < threshold:
            print("Detected")
            break
        else:
            print("Not Detected")
        if window_name != False:
            cv2.imshow(window_name, frame) 
             # Close and break the loop after pressing "x" key
        if cv2.waitKey(1) &0XFF == ord(key_for_exit):
            break
# close the already opened camera
    vid_capture.release()
# close the already opened file
    
    output.release()
# close the window and de-allocate any associated memory usage
    os.remove("1.jpg")
    os.remove("2.jpg")
    os.remove("test.avi")
    cv2.destroyAllWindows()

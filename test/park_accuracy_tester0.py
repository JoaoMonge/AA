#Works by giving images with cars manually counted and then measures the accuracy of the classifier
import cv2
import numpy as np
import imutils as im
from imutils.object_detection import non_max_suppression
import argparse

def get_acc(cascade_src):
    print
    # video_src = 'dataset/video2.avi'
    Total = [157,156,156,154,156] #manually determined by counting cars in test images
    
    # car_cascade = cv2.CascadeClassifier(cascade_src)
    car_cascade = cv2.CascadeClassifier('/home/js/Desktop/comp/emel/parkingLotCounter/classifiers/test/ankit_class/Khare_classifier_02.xml')
    counter = 1
    index =0
    list_of_indexes = []

    while True:

        if counter<6:
            print 'Reading img',counter
            img_init = cv2.imread('/home/js/Desktop/comp/emel/parkingLotCounter/classifiers/test/imgs/ankit/Khare_testFrame_0'+str(counter)+'.jpg') #test images
            print type(img_init)
            img = cv2.resize(img_init, None, fx=0.6, fy=0.6)
        else:
            break
        print '\nGray array'
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #convert to gray
        print (gray)

        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
            
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in cars])

        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        # draw the final bounding boxes
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)
            for (x, y, w, h) in cars:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0 , 0, 255), 2) #bgr
            index+=1
        cv2.imshow('image', img)
        cv2.waitKey(0)
        
        counter+=1
        saved = index
        print("%d vehicles found" %saved)
        list_of_indexes.append(saved/float(Total[counter-2]))
        index = 0
        print

    sum = 0
    for i in list_of_indexes:
        sum = sum + i
    percentage = (sum/len(list_of_indexes))*100
    print("Accuracy after evaluating 5 frames and assuming correct identification: ", percentage)
    cv2.destroyAllWindows()
    return percentage


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-cl", "--classifier", required=True, help="Path to the classifier")
args = vars(ap.parse_args())
# load the class, start the acc tester
get_acc(args["classifier"])

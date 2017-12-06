#Works by giving images with cars manually counted and then measures the accuracy of the classifier
import cv2
import numpy as np
import imutils as im
from imutils.object_detection import non_max_suppression
import argparse
import os

import sys
sys.path.append('/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/src')
import fileops

def get_acc(classifier):
    print

    # classifier=''

    car_cascade = cv2.CascadeClassifier(classifier)
    index = 0

    # images_path='/home/js/Desktop/comp/emel/parkingLotCounter/classifiers/datasets/ankit_dataset/negative'
    # Accuracy after evaluating 1570 frames and assuming correct identification:  25 %

    images_path='/home/js/Desktop/comp/emel/parkingLotCounter/classifiers/datasets/ankit_dataset/positive'

    direc = os.listdir(images_path)
    
    total=len(direc)
    
    for file in direc:

        # print 'Img: ',file
        img_init = cv2.imread(images_path+'/'+file) #  test images
        # print type(img_init)

        # img = cv2.resize(img_init, None, fx=0.60, fy=0.60)
        img = img_init

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #  convert to gray

        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in cars])
        
        # pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        # draw the final bounding boxes
        if len(cars):
            index+=1

        # cv2.imshow('image', img)
        cv2.waitKey(0)
        
        # print index,'\n'

    print index
    percentage = index*100/total


    accuraccy="Accuracy after evaluating",total," frames and assuming correct identification: ",percentage,"%"
    print s
    
    dataset=('_').join(images_path.split("/")[-2:])

    cl=('_').join(classifier.split("/")[-2:])


    wfile(s,fp.paths['ACCURACY_TEST_DIR']+cl+dataset+'.txt')

    cv2.destroyAllWindows()
    return percentage


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-cl", "--classifier", required=True, help="Path to the classifier")
args = vars(ap.parse_args())
# load the class, start the acc tester
get_acc(args["classifier"])
# get_acc(args["classifier"])

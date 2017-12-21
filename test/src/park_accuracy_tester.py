#Works by giving images with cars manually counted and then measures the accuracy of the classifier
import cv2

import numpy as np
import imutils as im
from imutils.object_detection import non_max_suppression
import argparse
import os

import sys
sys.path.append('/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/src')
import fileops as fp



def get_acc(classifier,images_path):
    idebug=0

    car_cascade = cv2.CascadeClassifier(classifier)
    index = 0

    direc = os.listdir(images_path)
    total=len(direc)

    for file in direc:
        if idebug>10:    
            print '\nImg: ',file,'\n'
        img_init = cv2.imread(images_path+'/'+file) #  test images
        
        # img = cv2.resize(img_init, None, fx=0.60, fy=0.60)
        img = img_init

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #  convert to gray


        # cars = car_cascade.detectMultiScale(gray, 1.1, 1)  #  detect the cars 
        cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)  #  detect the cars 
        '''
        Parameters of cascade.detectmultiscale():
    
        cascade – Haar classifier cascade (OpenCV 1.x API only). It can be loaded from XML or YAML file using Load().   
            When the cascade is not needed anymore, release it using cvReleaseHaarClassifierCascade(&cascade).
        image – Matrix of the type CV_8U containing an image where objects are detected.
        objects – Vector of rectangles where each rectangle contains the detected object.
        scaleFactor – Parameter specifying how much the image size is reduced at each image scale.
        minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.   
            Higher value results in less detections but with higher quality.
        flags – Parameter with the same meaning for an old cascade as in the function cvHaarDetectObjects. 
            It is not used for a new cascade.
        minSize – Minimum possible object size. Objects smaller than that are ignored.
        maxSize – Maximum possible object size. Objects larger than that are ignored.
        '''





        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in cars])
        
        # pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        # draw the final bounding boxes
        if len(cars):
            index+=1

        # cv2.imshow('image', img)
        cv2.waitKey(0)
        
        # print index,'\n'

    # print index
    percentage = index*100/total
    
    imgs=('_').join(images_path.split("/")[-3:])
    cl=('_').join(classifier.split("/")[-2:])

    test = 'positive' if 'positive' in imgs else 'negative'

    print "Accuracy after evaluating the classifer  ("+cl+")  with the dataset ("+imgs+") with "+str(total)+" imgs and assuming correct identification: "+str(percentage)+"%"

    # out_path=fp.paths['ACCURACY_TEST_DIR']+cl+'_'+imgs+'.txt'
    out_path=fp.DIRS['OPENCV-ACCURACY_TEST']+'accuracy-results-'+test+'.txt'

    result={
        'dataset':imgs,
        'classifer':cl,
        'accuracy':percentage
    }
    fp.aafile(result,out_path)

    cv2.destroyAllWindows()
    # return percentage


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
# ap.add_argument("-cls", "--classifiers", required=True, help="Path to the classifiers dir")
ap.add_argument("-ims", "--images", required=True, help="Path to the images dir")
args = vars(ap.parse_args())


## Test all classifiers
# for classifier in os.listdir(args["classifiers"]):
for classifier in fp.classifiers.values():
    print '\n\nTesting accury on', classifier,'\n'
    get_acc(classifier,args["images"][:-1])

# load the class, start the acc tester
# get_acc(args["classifier"])




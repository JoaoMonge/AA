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


classifiers={
'our-lbt':          '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/LBP_ankit_imgs.xml',
'our-harr' :        '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/HAAR_ankit_imgs.xml',
'our-harr-small' :  '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/HAAR_small_ankit_imgs.xml',
'ankit-haar' :      '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/ankit_class/ankit-haar.xml',
'ankit-haar2' :     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/ankit_class/ankit-haar2.xml'
}



def get_acc(classifier=None,images_path):
    print

    # classifier=''

    car_cascade = cv2.CascadeClassifier(classifier)
    index = 0

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




    # print index
    percentage = index*100/total
    
    imgs=('_').join(images_path.split("/")[-2:])

    cl=('_').join(classifier.split("/")[-2:])

    print "Accuracy after evaluating the classifer"+cl+" with the dataset "+imgs+" with "+str(total)+" imgs and assuming correct identification: "+str(percentage)+"%"

    # out_path=fp.paths['ACCURACY_TEST_DIR']+cl+'_'+imgs+'.txt'
    out_path=fp.paths['ACCURACY_TEST_DIR']+'accuracy-results.txt'

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
ap.add_argument("-cl", "--classifier", required=False, help="Path to the classifier")
ap.add_argument("-imgs", "--images", required=True, help="Path to the images")

args = vars(ap.parse_args())

if len(args=2):
    
# load the class, start the acc tester
get_acc(args["classifier"],args["images"])
# get_acc(args["classifier"])




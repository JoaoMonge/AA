# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV 
import cv2
# import time as Time

import sys
sys.path.append('/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/src')
import fileops as fp

from utils import *




'''
Generate images with rectangles over the detected cars,
only works for classifiers that are built with OPENCV or follow its structure (xml of the classf)

saves the results in the /results_class_full_img dir with the name class+video+'.jpg'

classifer-> all calssfiers to test in each video
videos->  1st frame of each video is used to apply the classififers above

'''


# classifier={

# 'our-lbt':          '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/LBP_ankit_imgs.xml',
# 'our-harr' :        '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/HAAR_ankit_imgs.xml',
# 'our-harr-small' :  '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/HAAR_small_ankit_imgs.xml',
# 'ankit-haar' :      '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/ankit_class/ankit-haar.xml',
# 'ankit-haar2' :     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/ankit_class/ankit-haar2.xml'

# }


videos={
'ankit':    '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/ankit.mp4',
'abhi':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/abhi.mp4',
'highway' : '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/highway.avi',
'garage' :  '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/garage.mp4',
'trig':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/trigg.mp4'
}


defs={
'save': True
}


for cl in classifiers.keys():
    for vid in videos.keys():
        print '\n\nNext Combination:'

        defs['classifier_path'] = classifiers[cl]
        defs['video_path'] = videos[vid]

        print 'iteration parameters: \n-',cl,'\n-',vid,'\n'

        print 'iteration paths: \n-',defs['classifier_path'],'\n-',defs['video_path'],'\n'

        save_path=fp.DIRS['OPENCV-FULLPARK-RESULT']+cl+'_'+vid+'.png'

        # start video iteration
        cap = cv2.VideoCapture(defs['video_path'])
        if cap.isOpened():
            print 'Video opened\n'
        else:
            
            print 'Error in opening video, bye!\n'
            exit()
        print

        # Trained XML classifiers describes some features of some object we want to detect
        car_cascade = cv2.CascadeClassifier(defs['classifier_path'])
        
        # loop runs if capturing has been initialized.
        try:
            while True:
                # reads frames from a video
                ret, frames = cap.read()

                # convert to gray scale of each frames
                gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
                
                # Detects cars of different sizes in the input image
                cars = car_cascade.detectMultiScale(gray, 1.1, 1)
                
                # To draw a rectangle in each cars
                for (x,y,w,h) in cars:
                    cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
                    
                # save img when more then 4 cars are detected
                if defs['save'] and len(cars)>4:

                    print 'Saving img with name',save_path
                    cv2.imwrite(save_path,frames)

                    # De-allocate any associated memory usage
                    cv2.destroyAllWindows()
                    break

                ## Display frames in a window 
                # cv2.imshow(save_path, frames)
                # Time.sleep(0.01)

                # Wait for Esc key to stop
                if cv2.waitKey(33) == 27:
                    break
            
                # De-allocate any associated memory usage
                cv2.destroyAllWindows()
        except:
            print 'Error in ', cl,' , ',vid
            raise


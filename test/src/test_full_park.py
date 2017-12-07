# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV 
import cv2
# import time as Time

import sys
sys.path.append('/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/src')
import fileops as fp

print

'''
This script generates images with rectangles over the detected cars,
only works for classifiers that are built with OPENCV or follow its structure (of the classf)

save the results in the /results_class_full_img dir with the name class+video+'.jpg'

classifer-> all calssfiers to test in each video
videos->  1st frame of each video is used to apply the classififers above

'''


classifier={
'our-lbt':          '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/LBP_ankit_imgs.xml',
'our-harr' :        '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/HAAR_ankit_imgs.xml',
'our-harr-small' :  '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/HAAR_small_ankit_imgs.xml',
'ankit-haar' :      '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/ankit_class/ankit-haar.xml',
'ankit-haar2' :     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/ankit_class/ankit-haar2.xml'
}


videos={
'ankit':    '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/ankit.mp4',
'abhi':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/abhi.mp4',
'highway' : '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/highway.avi',
'garage' :  '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/garage.mp4',
'trig':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/trigg.mp4'
}


params={
'save': True
}


for cl in classifier.keys():
    for vid in videos.keys():
        print '\n\nNext:'

        params['classifier_path'] = classifier[cl]
        params['video_path'] = videos[vid]

        print 'iteration parameters: \n-',cl,'\n-',vid
        print

        print 'iteration paths: \n-',params['classifier_path'],'\n-',params['video_path']
        print

        save_path=fp.DIRS['OPENCV-FULLPARK-RESULT']+cl+'_'+vid+'.png'

        # start video iteration
        cap = cv2.VideoCapture(params['video_path'])
        if cap.isOpened():
            print 'Video opened'
        else:
            print 'Video error in open'
            raise
        print

        # Trained XML classifiers describes some features of some object we want to detect
        car_cascade = cv2.CascadeClassifier(params['classifier_path'])
        
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
                    
                # save imge
                if params['save'] and len(cars)!=0:

                    print 'Saving img with name',save_path

                    cv2.imwrite(save_path,frames)
                    # cv2.imwrite('./ahha.png',frames)
                    # De-allocate any associated memory usage
                    cv2.destroyAllWindows()
                    break

                # Display frames in a window 
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


'''
detect cars in video frame with opencv
saves image of detected cars with rectangle
'''
# import libraries of python OpenCV 
import cv2
# import time as Time


classifier={
'our-lbt':      '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/banana_classifier_LBP_ankit_imgs.xml',
'our-harr' :    '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/our_class/banana_classifier_HAAR_ankit_imgs_output.txt',
'ankit-haar' :  '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/ankit_class/ankit-haar.xml',
'ankit-lbt' :   '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/classifiers_opencv/ankit_class/ankit-lbt.xml'
}

videos={
'ankit':    '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/ankit.mp4',
'abhi':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/abhi.mp4',
'highway' : '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/highway.avi',
'garage' :  '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/garage.mp4',
'trig':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/videos/trigg.mp4'
}

cl=classifier['ankit-haar']
vid=videos['highway']
save_path='/home/js/Documents/comp/emel/parkingLotCounter/classifiers/test/results/'+cl+'_'+vid+'.png'

params={
    'classifier_path' : cl,
    'video_path' : vid,
    'save':True
}

print '\nChosen parameters:',cl,vid


# capture frames from a video
cap = cv2.VideoCapture(params['video_path'])

print cap.isOpened()

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
            
        # Display frames in a window 
        cv2.imshow(cl+'_'+vid, frames)
        # Time.sleep(0.01)

        # Wait for Esc key to stop
        if cv2.waitKey(33) == 27:
            break
    
        # De-allocate any associated memory usage
except:
    print 'Error in', cl,vid
    cv2.destroyAllWindows()

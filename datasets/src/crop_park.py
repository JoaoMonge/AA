# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:21:17 2015

@author: elad
"""

import yaml
import numpy as np
import cv2
print '\n',cv2.__version__,'\n'

# paths of the imgs
imgs={
'ankit':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/ankit.jpg',
'eladj':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/eladj.png',
'highway' :  '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/highway.png',
'garage' :   '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/garage.png',
'trig':      '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/trig/trigg.png',
'trig2':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/trig/trigg2.png',
'trig3':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/trig/trigg3.png',
'trig4':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/trig/trigg4.png',
'trig5':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/trig/trigg5.png',
'trig6':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/trig/trigg6.png',
'trig7':     '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/normal/trig/trigg7.png',
}
img='highway'

# paths of the imgs
typpes={
    'pos' : 'positive',  
    'neg' : 'negative'
}
typpe=typpes['neg']  # pos->car imgs ; neg->empty spot imgs (floor : )
fn = imgs[img]


# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
count =0
print_parking_data =[]



def click_crop_save(event, x, y, flags, param):
    idebug=0
    # grab references to the global variables
    global refPt, count, print_parking_data, fn

    if event == cv2.EVENT_LBUTTONDOWN:
        if idebug>10:
            print 'clicked down'

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:

        # record the ending (x, y) coordinates
        if idebug>10:
            print 'clicked up', x, y
        refPt.append([x, y])
        count = count + 1

        # draw the line of interest
        try:
            #draw a line between the two last elements
            cv2.line(frame, (refPt[-2][0],refPt[-2][1]), (refPt[-1][0],refPt[-1][1]), (0, 255, 0), 1)
            # cv2.imshow("ankit", frame)
        except:
            if idebug>10:
                print 'Could access points to draw line'
            pass

        # cv2.imshow("frame", frame)
        if idebug>10:
            print 'Current rectangle', refPt

        id = count%4
        if id==0 :
            cv2.line(frame, (refPt[-1][0],refPt[-1][1]), (refPt[0][0],refPt[0][1]), (0, 255, 0), 1)

            #copy the cropped img and save
            full_img_out_path=img_out+str(count/4)+'.png'
            if idebug>10:
                print 'Image saved to path:', full_img_out_path
            
            # crop and save rectangle/img wirh ROI inside
            # save_img(fn,out_path,refPt)
            # save_img1(fn,out_path,refPt)
            draw_rect_over_poly(refPt,full_img_out_path)

            #append to park slots datapoints = np.array(park['points'])points = np.array(park['points'])
            print_parking_data.append( {'points':refPt,'id':count/4} )
            if idebug>10:
                print 'End of rect: ', refPt,'\n'
            refPt=[]




def draw_rect_over_poly(points,path):
    idebug=11

    if idebug>10:
        print '\ndraw_rect_over_poly()\n'
        print 'Polygon:', points,'\n'

    #get a rectangle that has the whole polygon
    [x,y,w,h] = cv2.boundingRect(np.asarray(points))   # rect = [x, y, w, h]
    if idebug>10:
        print 'Rectangle from polygon', x,y,w,h,'\n'
    
    #load the original img to avoid cropping the drawed car spot line
    img = cv2.imread(fn)

    # crop rectangle
    crop_img = img[y:y+h, x:x+w] # Crop from x, y, w, h -> 100, 200, 300, 400
    # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
    cv2.imshow("cropped", crop_img)

    # save img
    cv2.imwrite(path,crop_img)
    
    if idebug>10:
        print '\nSaved image to path: ', path,'\n'

    return crop_img







print "============================="
print "Running detectpark from file "
print "============================="
print



# continue img out path on save with number.jpg
if 'trig' in img:
    img_out = '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/cropped/trigg/'+typpe+'/'+typpe+'_'+img+'_' 
else:
    img_out = '/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/imgs/imgs-full-parks/cropped/'+img+'/'+typpe+'/'+typpe+'_'+img+'_' 


# Set capture device or file
cap = cv2.VideoCapture(fn)
video_info = {'fps':    cap.get(cv2.CAP_PROP_FPS),
              'width':  int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
              'fourcc': cap.get(cv2.CAP_PROP_FOURCC),
              'num_of_frames': int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}
print '\nVideo info:', video_info

cv2.namedWindow(img)
cv2.setMouseCallback(img, click_crop_save)
frame = cv2.imread(imgs[img])



while True:
    # Display imgs

    cv2.imshow(img, frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
        cv2.destroyAllWindows()


print '\nFinal rectangles(park spots)', print_parking_data,'\n'

print
print "============================="
print '           THE END           '
print "============================="
print
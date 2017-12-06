#https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html
#https://github.com/mrnugget/opencv-haar-classifier-training
#https://docs.opencv.org/3.3.0/dc/d88/tutorial_traincascade.html

#Put your positive images in the ./positive_images folder and create a list of them:
 find ./positive_images -iname "*.bmp" > positives.txt


#Put the negative images in the ./negative_images folder and create a list of them:
 find ./negative_images -iname "*.jpg" > negatives.txt


#Create positive samples with the bin/createsamples.pl script and save them to the ./samples folder: 
 perl bin/createsamples.pl positives.txt negatives.txt samples 1500\
   "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
   -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 80 -h 40"


#Use tools/mergevec.py to merge the samples in ./samples into one file:
 python ./tools/mergevec.py -v samples/ -o samples.vec

#Note: If you get the error struct.error: unpack requires a string argument of length 12 then go into your samples directory and delete all files of length 0.


#Start training the classifier with opencv_traincascade, which comes with OpenCV, and save the results to ./classifier:
#   default->(-featureType HAAR)

 opencv_traincascade\
   -data classifier\
   -vec samples.vec \
   -bg negatives.txt\
   -numStages 20\
   -minHitRate 0.999\
   -maxFalseAlarmRate 0.5\
   -numPos 1000\
   -numNeg 600\
   -w 80\
   -h 40\
   -mode ALL\
   -precalcValBufSize 1024\
   -precalcIdxBufSize 1024

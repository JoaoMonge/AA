import os
from PIL import Image                                                                                
import sys
os.system

#number/name of the photos
i=0

# dir to look for invalid
dirr="/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/new-mixed/negative/"


for filename in os.listdir(dirr):
    # print(filename)
    try:
        img = Image.open(dirr+'Khare_trainimage_negative_534.jpg')
        img.show() 
        img.close()

    except BaseException :
        tb = sys.exc_info()[2]
        os.remove(dirr+filename)
        print('removed')

    exit()
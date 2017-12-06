import os

i=2204

dirr="/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/new-mixed/floor/MiddleClose/"


for filename in os.listdir(dirr):
    print(filename)
    if '.bmp' != filename[-4:]:
     os.rename(dirr+filename, dirr+'imag_'+str(i)+filename[-4:])
     i+=1
    else:
     os.rename('/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/new-mixed/'+filename, dirr+'_'+filename)

print(i)

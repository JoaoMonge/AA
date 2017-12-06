import os


def change_name():
    i=0
    dirr_in='home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/new-mixed/floor/MiddleClose/'
    dirr_out='/home/js/Documents/comp/emel/parkingLotCounter/classifiers/datasets/new-mixed/'

    for filename in os.listdir(dirr_in):
        print(filename)
        if '.bmp' != filename[-4:]:
            os.rename(dirr_in+filename, dirr_in+'imag_'+str(i)+filename[-4:])
            i+=1
        else:
            os.rename(dirr_out+filename, dirr_in+'_'+filename)

    print(i)

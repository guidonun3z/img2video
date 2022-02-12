#create video from images
#version: 0.2
# autor: GENA

from fileinput import filename
import cv2
import os
from os.path import isfile, join
from numpy import *
import random
nrad=random.randint(0,999)


# Video especifications 

hhini=000
hhfin=2400
dia="0211"
camara="TSOQ22"
ext=".avi"


def convert_pictures_to_video(pathIn, pathOut, fps, time):
    '''this function converts pictures to video'''
    frame_array = []
    files=[f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]    
    files2=[j for j in files if hhini<=int(j[-10:-6])<=hhfin ]
 
    for i in range (len(files2)):
        filename=pathIn+files2[i]
        ''''readin images'''
        img=cv2.imread(filename)
        #change size
        #img=cv2.resize(img,(1400,1600))
        
        height, width, layers = img.shape
        size=(width, height)
        
        for k in range (time):
            frame_array.append(img)

    out=cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps,size)

    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
    print("se creó el video exitosamente\n","se compilaron " + str(len(files2))+ " archivos" )
    
#out file configuration: 
directory='c:/carpeta/carpeta'
pathIn=directory+'/'
pathOut=pathIn+camara+'-'+str(hhini)+'-'+str(hhfin)+'-'+dia+'-'+str(nrad)+ext
fps=25
time=5 #time duration of each pictures

#calling function
convert_pictures_to_video(pathIn, pathOut, fps, time)


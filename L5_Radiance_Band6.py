#MD SHAH NAIM HREDOY
#hridhowlader@gmail.com

# Import system modules

import arcpy
from arcpy import env

# set environment
# Here you have to set your own directory

env.workspace="H:/STUDY/Document/Papers/RS02/LT05_L1TP_138043_20010112_20161212_01_T1"
env.overwriteOutput=True
from arcpy.sa import *

# Checking out spatial extension 

arcpy.CheckOutExtension("Spatial")

# Setting up variables

image = arcpy.Raster("H:/STUDY/Document/Papers/RS02/LT05_L1TP_138043_20010112_20161212_01_T1/LT05_L1TP_138043_20010112_20161212_01_T1_B6.TIF")
numerator = 14.065
denominator = 254
cons1=1
cons2=1.234

# performing main operation step by step

qcal=image-cons1
division=numerator/denominator
multiply=qcal*division
radiance=multiply+cons2

# Save the output

radiance.save("H:/STUDY/Document/Papers/RS02/LT05_L1TP_138043_20010112_20161212_01_T1/rad6.tif")

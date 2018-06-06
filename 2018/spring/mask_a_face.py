# (c) Giovambattista Vieri
# 2018 
# license Mit

import os
import re
from PIL import Image, ImageFont, ImageDraw, ImageEnhance 

X_WIDTH=229
Y_HEIGHT=256

mask="FACE_CROP_.*\.jpg"
mydir="."

def mask_a_face(file):
    """mask a face"""
    face=Image.open(file) 
    face.show()
    width, height = face.size
    print "larghezza e altezza %s,%s" % (width, height) 
    x_coeff=float(width)/X_WIDTH
    y_coeff=float(height)/Y_HEIGHT
    print "xcoeef %s ycoeff %s" % (x_coeff,y_coeff) 
    draw = ImageDraw.Draw(face)
    x1=50 * x_coeff
    y1=50 * y_coeff
    x2=130* x_coeff
    y2=80 * y_coeff
    draw=draw.rectangle(((x1,y1),(x2,y2)), fill="black") 
    draw = ImageDraw.Draw(face)
    x1=100* x_coeff
    y1=80 * y_coeff
    x2=115* x_coeff
    y2=170* y_coeff
#    draw=draw.rectangle(((100,80),(115,170)), fill="black") 
    draw=draw.rectangle(((x1,y1),(x2,y2)), fill="black") 
    draw = ImageDraw.Draw(face)
    x1=115* x_coeff
    y1=120* y_coeff
    x2=170* x_coeff
    y2=135* y_coeff
#    draw=draw.rectangle(((115,120),(170,135)), fill="black") 
    draw=draw.rectangle(((x1,y1),(x2,y2)), fill="black") 

    face.show()
    face.save("MASKED_"+file)


for file in os.listdir(mydir):
    if re.match(mask, file):
        print "found:"+file
        mask_a_face(file)


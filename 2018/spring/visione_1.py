# simple demo for a pool of images to "qualify" using google services




# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

import io
import os
from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw 


extension = ".jpg"
mydir     = "." 
img_size= 512, 512
font = ImageFont.truetype("FreeSans.ttf", 16)


for file in os.listdir(mydir):
    if file.endswith(extension):
	filepath=os.path.join(mydir, file)
	print filepath
        
# The name of the image file to annotate
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    filepath)

# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)
# Instantiates a client
	client = vision.ImageAnnotatorClient()

# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations

	print('Labels:')
	for label in labels:
	    print(label.description)
        print "***********************************************"
	img = Image.open(file_name)
        img.thumbnail(img_size, Image.ANTIALIAS) 
# get real size 
        width,height = img.size
	heightdraw=height
	height+=200
	realSize=(width, height)
	print realSize
# add large + 200 pixel area 
	newimg= Image.new(img.mode,realSize)
        

# move the image in the new area 
        newimg.paste(img,(0,0)) 

# write in the new area 
        draw = ImageDraw.Draw(newimg)
        for label in labels:
            draw.text((0, heightdraw),label.description,(255,0,0),font=font)
            heightdraw += 20 


	newimg.show() 

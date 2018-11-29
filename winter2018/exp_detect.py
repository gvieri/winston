import io
import os
import re
import time
from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

mask=".*\.jpg" 
mydir     = "." 
img_size= 512, 512
font = ImageFont.truetype("FreeSans.ttf", 16)

def detect_faces(path):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('**********************************************')
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('sorrow: {}'.format(likelihood_name[face.sorrow_likelihood]))
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        print('blurred: {}'.format(likelihood_name[face.blurred_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

#        print('face bounds: {}'.format(','.join(vertices)))

for file in os.listdir(mydir):
    if re.match(mask, file):
        print('**********************************************')
        print "found:"+file
        img = Image.open(file)
        img.show() 	 
        img.thumbnail(img_size, Image.ANTIALIAS) 
        time.sleep(2)
        detect_faces(file)
	time.sleep(10) 


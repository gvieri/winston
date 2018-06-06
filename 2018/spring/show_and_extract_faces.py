import io
import os
import re

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image

face_file_size=256, 256
mask="face.*\.jpg"
mydir="."

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
    print('File name {} Faces:'.format(path))
###
    img= Image.open(path)
    

###
    faceCounter=0

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
	print face.bounding_poly.vertices
	dummy0=face.bounding_poly.vertices
	# I need a box to crop the face	
	box=[dummy0[0].x,dummy0[0].y,dummy0[2].x,dummy0[2].y]

        	
        print box	

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])
        print('face bounds: {}'.format(','.join(vertices)))
###      now extract face from bound, create a new image 512x512 
	imgDest=img.crop(box)
	imgDest.thumbnail(face_file_size,Image.ANTIALIAS)
#	imgDest.show() 
	savename="FACE_CROP_"+str(faceCounter)+path
	imgDest.save(savename)
        faceCounter+=1
        


for file in os.listdir(mydir):
    if re.match(mask, file):
        print "found:"+file
        detect_faces(file)


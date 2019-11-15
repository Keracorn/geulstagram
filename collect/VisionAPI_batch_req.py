# -*- coding: UTF-8 -*-
import os, io
from google.cloud import vision
from google.cloud.vision import enums
from google.cloud.vision import types
import pandas as pd


#you should change 1) credentials and 2) system environment variable in order to change into other account
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'credentials.json' #specifying the location of credentials.
client = vision.ImageAnnotatorClient() #fetching google vision api client

# You can add other Google Vision's features, like face detection, over here.
features = [
    types.Feature(type=enums.Feature.Type.TEXT_DETECTION) # Here, we are only going to use text detection feature.
]



requests = []

# inputting files here, as in forms of filename
for filename in ['1.jpg','2.png','3.jpg']:
    with io.open(filename, 'rb') as image_file:
        content = image_file.read() # reading the image content
    image = vision.types.Image(content=content)
    request = types.AnnotateImageRequest(image=image, features=features) #request is a single dictionary
    requests.append(request) #making list of requests for batch request
print("numbers of files submitted to API: "+ str(len(requests)))

response = client.batch_annotate_images(requests) #response from submitting batch request to Google Cloud API Client

# print(response)
for annotation_response in response.responses:
    texts = annotation_response.text_annotations
    # text annotations is
    # annotation response is

    df = pd.DataFrame(columns=['locale','description'])
    # texts is a list. texts is consisted of 1) entire text paragraph, 2) individual lines following afterwards.
    text = texts[0]
    df = df.append(
        dict(
            locale = text.locale,
            description=text.description
        ),
        ignore_index=True
    )
    print(df['description'][0])




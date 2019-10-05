# -*- coding: UTF-8 -*-
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# 1. Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# choose a local (colab) directory to store the data.
local_download_path = os.path.expanduser('~/data')
try:
  os.makedirs(local_download_path)
except: pass

# 2. Auto-iterate using the query syntax
#    https://developers.google.com/drive/v2/web/search-parameters
file_list = drive.ListFile(
    {'q': "'185t0Gf_n7s0-whl2CtaTWzTV0CdqUJcv' in parents"}).GetList()

for f in file_list:
    print(f)

credential_location = ""

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

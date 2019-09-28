import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'credentials2.json'

client = vision.ImageAnnotatorClient()

# print(dir(client))

client = vision.ImageAnnotatorClient()

def detectText(img):

    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # print(response)

    df = pd.DataFrame(columns=['locale','description'])
    for text in texts:
        df = df.append(
            dict(
                locale = text.locale,
                description=text.description
            ),
            ignore_index=True
        )

    print(df['description'][0])
    return df

FILE_NAME = 'hand4.jpg'
FOLDER_PATH =r'C:/Users/pc/Desktop/1909XX Coding/_Python venv/VisionAPIDemo/IMAGE'
# print(detectText(os.path.join(FOLDER_PATH,FILE_NAME)))
detectText(os.path.join(FOLDER_PATH,FILE_NAME))

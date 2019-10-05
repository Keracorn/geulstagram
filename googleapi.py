import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd
import json
from collections import OrderedDict

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'credentials.json'

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
    return df['description'][0]

FOLDER_PATH =r'C:/Users/khak1/OneDrive/바탕 화면/임시 컨트리/woojin_940205'
file_list=os.listdir(FOLDER_PATH)

ID = dict()

#for i in range(len(file_list)): 실제 데이터 생성용
#for i in range(0,5): test용
    try :
        content=detectText(os.path.join(FOLDER_PATH,file_list[i]))
        ID[i]=file_list[i], content
    except IndexError:
        continue

with open("woojin_940205.json",'w',encoding="utf-8") as make_file:
          json.dump(ID, make_file, ensure_ascii=False, indent="\t")

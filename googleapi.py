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

tmp_content=list()
content=list()
file_data=OrderedDict()

#for i in range(len(file_list)):
for i in range(0, 5):
    try :
        temp=detectText(os.path.join(FOLDER_PATH,file_list[i]))
        tmp_content.append(temp)
    except IndexError:
        continue

#for i in range(len(tmp_content)):
#    content.append(tmp_content[i].split())

#for i in range(len(content)):
#    tmp_hash=list()
#    for j in range(len(content[i])):
#        if j<len(content[i]):
#            if "#" in content[i][j]:
#                tmp_hash.append(content[i][j])
#                del content[i][j]
#        file_data[str(i+1)+" hash"]=tmp_hash
#    file_data[i+1]=content[i]
for i in range(len(tmp_content)):
    tmp_hash=list()
    for j in range(len(tmp_content[i])):
        if j<len(tmp_content[i]):
            if "#" in tmp_content[i][j]:
                tmp_hash.append(tmp_content[i][j])
                del tmp_content[i][j]
            file_data[str(i+1)+" hash"]=tmp_hash
        file_data[i+1]=tmp_content[i]

with open("woojin_940205.json",'w',encoding="utf-8") as make_file:
          json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

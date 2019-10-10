import os
import io
from google.cloud import vision
import pandas as pd
import json
import csv

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'snoop2head@gmail.com.json'

client = vision.ImageAnnotatorClient()

# OCR 작동 부분
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

# 이미지 들어있는 폴더 넣기
def textToJsonToCsv(FOLDER_PATH):
    file_list = os.listdir(FOLDER_PATH)
    User_name = os.path.basename(FOLDER_PATH)

    ID = dict()

    for i in range(len(file_list)): #실제 데이터 생성용
#    for i in range(0,2): #test용
        try :
            content = detectText(os.path.join(FOLDER_PATH,file_list[i]))
            ID[i]=file_list[i], content
        except IndexError:
            continue

    # save as json
    with open(User_name + ".json",'w',encoding="utf-8") as make_file:
              json.dump(ID, make_file, ensure_ascii=False, indent="\t")

    # Json to CSV
    Input = open(User_name + ".json",'rt', encoding='utf-8')
    json_data = json.load(Input)

    Output=open(User_name + ".csv", 'w',newline='', encoding='utf-8-sig')

    csvwriter = csv.writer(Output)

    content = list(json_data.values())

    header = ["게시글 id", "이미지 본문"]
    csvwriter.writerow(header)

    for i in range(len(content)):
        for j in range(len(content[i])):
            content[i][j] = content[i][j].replace("\n", " ")

    for i in range(len(content)):
        csvwriter.writerow(content[i])

    Output.close()

# 유저 폴더 묶인 상위 폴더
user_list = os.listdir(r'C:\Users\Ajou\Downloads\User_Images_2/')
print(user_list)
cnt = 0
for i in user_list:
    cnt += 1
    textToJsonToCsv(r'C:\Users\Ajou\Downloads\User_Images_2/' + i )
    print(cnt)
    print(i,"완료")
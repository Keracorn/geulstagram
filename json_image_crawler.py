import json
import re
import sys
import urllib.request
import ig_query_parser

import os
from collections import OrderedDict
from urllib.error import HTTPError

def get_image_tag(userName):
    # print("username : " + userName)
    currentpath = os.getcwd()
    path = os.path.join(currentpath, userName)
    try:
         if not(os.path.isdir(path)):
           os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    # print(path)
    file_name = userName+".json"
    with open(file_name,'r',encoding="UTF8") as data_file:
        data = json.load(data_file)
        # print(data)
        # print(len(data))
        # image URL은 해당 글스타그램 사진에 해당하는 url입니다.

        #이미지 파일 정보에 대한 json 파일을 생성하는 부분입니다.
        out_json = os.path.join(path, userName + "_" + "image.json")
        with open(out_json, 'w+', encoding="utf-8") as make_file:
            list = []
            
            image_cnt = 0
            for i in range(0, len(data)-1):
                file_data = OrderedDict()
                #key 값을 json data로 부터 받아서 오는 작업
                key = ig_query_parser.get_ig_key(data[i]["key"])
                # print("key : " + key)
                if "img_urls" in data[i]:
                    image_num = 0
                    image_list = data[i]["img_urls"]
                    file_list = []
                    for imageUrl in image_list:
                        #image 이름을 만드는 부분입니다. key_0.jpg 형태로 image 파일이 생성됩니다
                        image_name = key + "_" + str(image_num) + ".jpg"
                        #URL이 이미지 형태가 아닐경우 예외처리를 하는 구간입니다.
                        try:
                            download_image(imageUrl, path, image_name)
                        except HTTPError as e:
                            print("CANNOT DOWNLOAD FILE")
                            continue
                        file_list.append(image_name)
                        image_num += 1
                        image_cnt += 1
                    if not file_list:
                        continue
                    file_data["file_names"] = file_list
                    tag_list = []
                    #게시글의 해쉬태그를 가져오는 부분입니다. 해쉬태그는 본문에서 찾을 수 없는 경우 댓글에서 찾도록 손을 봤습니다.

                    # if data[i].has_key("caption"):
                    if "caption" in data[i]:
                        tag_containing_txt = data[i]["caption"]
                        tag_list = re.findall(r"#(\w+)", tag_containing_txt)
                        #caption 에 해쉬태그를 달지 않는경우 comments에서 해쉬태그를 찾음
                        if not tag_list:
                            #댓글이 있는지 확인
                            if "comments" in data[i]:
                                #댓글이 있는 경우 리스트로 받아옴
                                comment_list = data[i]["comments"]
                                for i in comment_list:
                                    comment_writer = i["author"]
                                    if comment_writer == userName:
                                        author_written_comment = i["comment"]
                                        tag_list = re.findall(r"#(\w+)", author_written_comment)
                                        #태그가 저장이 되었다면 for 문 종료
                                        if len(tag_list) != 0:
                                            break

                    file_data["tags"] = tag_list
                    list.append(file_data)

            #생성된 json list를 저장
            json.dump(list, make_file, ensure_ascii=False)
        
        print("#USER : " + userName + "  " + str(image_cnt)+ " images downloaded!")
                
def download_image(url,path, name):
    print("download : " + url)
    if not os.path.isdir(path):
        os.makedirs(path)

    
    urllib.request.urlretrieve(url, path +"/" +name)
    



if(len(sys.argv) == 1):
    print("missing argument!")
    sys.exit()
get_image_tag(sys.argv[1])

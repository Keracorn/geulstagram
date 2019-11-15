import json
import re

# sky_blue_writing07.json
# 해시태그가 본문에 달린 경우

def get_tag_body(userName):
    file_name = "_2_IG_HASHTAG/"+ userName+".json"
    with open(file_name,'r',encoding="UTF8") as data_file:
        data = json.load(data_file)
        # print(data)
        print(len(data))
        # image URL은 해당 글스타그램 사진에 해당하는 url입니다.
        print(data[0]["img_urls"])

        # caption이 인플루언서가 사진과 더불어서 입력하는 본문입니다.
        # print(data[0]["caption"])
        tag_containing_txt = data[0]["caption"]
        tag_list = re.findall(r"#(\w+)", tag_containing_txt)
        print(tag_list)
    return tag_list

# get_tag_body("1day1poem")

def get_tag_comment(userName):
    file_name = "_2_IG_HASHTAG/" + userName+".json"
    with open(file_name,'r',encoding="UTF8") as data_file:
        data = json.load(data_file)
        # print(data)
        print(len(data))

        # print(data[0])
        # image urls은 해당 글스타그램 사진들에 해당하는 url들의 리스트입니다.
        image_urls_list = data[0]["img_urls"]
        print(image_urls_list)

        # tag_body_list는 본문 내용에 들어있는 해시태그 키워드들을 리스트로 반환해줍니다.
        # caption이 인플루언서가 사진과 더불어서 입력하는 본문 내용입니다.
        tag_body_list = data[0]["caption"]
        print(tag_body_list)

        # tag_containing_comment는 덧글 내용에 들어있는 해시태그 키워드들을 리스트로 반환해줍니다.
        comment_list = data[0]["comments"]
        for i in comment_list:
            comment_writer = i["author"]
            if comment_writer == userName:
                author_written_comment = i["comment"]
                tag_list = re.findall(r"#(\w+)", author_written_comment)
                if len(tag_list) == 0:
                    pass
                else:
                    break
        print(tag_list)
        return tag_list


# get_tag_comment("insum_")

# get_tag_comment("ajaegeul")

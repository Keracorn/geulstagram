import csv, json

Input = open("kim_hanwoong.json",'rt', encoding='utf-8')
data=json.load(Input)

Output=open("kim_hanwoong.csv", 'w',newline='', encoding='utf-8-sig')

csvwriter=csv.writer(Output)

content=list(data.values())

header=["게시글 id", "이미지 본문"]
csvwriter.writerow(header)

for i in range(len(content)):
    for j in range(len(content[i])):
        content[i][j]=content[i][j].replace("\n"," ")

for i in range(len(content)):
    csvwriter.writerow(content[i])


Output.close()



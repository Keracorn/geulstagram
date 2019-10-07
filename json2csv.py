from pandas.io.json import json_normalize
import csv, json
import numpy as np

Input = open("woojin_940205.json",'r',encoding="UTF-8")
data=json.load(Input)

Output=open("woojin_940205.csv", 'w',encoding="euc_kr", newline='')

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



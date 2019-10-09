from ig_query_parser import get_ig_key
import numpy as np
import pandas as pd
import csv

def index_csv(username):
    csv_file_name = "_1_OCR_CSV/" + username + ".csv"
    print(csv_file_name)
    with open(csv_file_name,'r',encoding="UTF8") as data_file:
        df = pd.DataFrame(data_file)
        print(df)

index_csv("iamkimbunny")

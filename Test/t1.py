import pandas as pd

df = pd.read_csv('order.csv')
print(df.loc[0])


import csv

with open('order.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

split_list = [row.split(';') for sublist in your_list for row in sublist]

your_dict = {row[0]: row[1:] for row in split_list[1:]}

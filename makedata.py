import csv
import random
import json


data_out = {}

with open('data.csv', 'r') as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        namestr = f"<b>{row['name']}</b><br>{row['occupation']}"
        cat = row['picture_category']

        if not data_out.get(cat):
            data_out[cat] = set()

        data_out[cat].add(namestr)

for key in data_out:
    rec = data_out[key]
    random.shuffle(list(rec))
    if len(rec) == 1:
        html = f'<div class="mug"><img src="pictures/{key}.jpg" title="{key}" /><p class="caption">{list(rec)[0]}</p></div>'
        print(html)

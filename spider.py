import requests
from bs4 import BeautifulSoup
import csv
# web crawler
url ='https://pleagueofficial.com/stat-player'
html = requests.get(url)
html.encoding = 'UTF-8'
bs = BeautifulSoup(html.text, 'html.parser')
table=bs.tbody
row=table.find_all('tr')

# data processing
data=[]
for i in row:
    for j in i:
        if j.text != '\n':
            data.append(j.text)

# write into csv
with open('player.csv', 'w', newline='',encoding="UTF-8") as file:
    writer = csv.writer(file)
    
    field = ["name", "number","team", "Games played","time(min)",
             "2pt","2pt shot","2pt percentage","3pt","3pt shot",
             "3pt percentage","free throw","free throw shot",
             "free throw percentage","pt","offReb","defReb",
             "tReb","assist","steal","block","turn over","foul"]
    writer.writerow(field)
    for i in range(len(data)//23):
        row=[]
        for j in range(23):
            row.append(data[0])
            data.pop(0)
        # print(row)
        writer.writerow(row)

    
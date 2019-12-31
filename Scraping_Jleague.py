# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys

url = "https://data.j-league.or.jp/SFIX02/search?displayId=SFIX02&selectValue=1&displayId=SFIX02&selectValueTeam=54"
#url = "https://www.google.com/"

html = requests.get(url)

soup = BeautifulSoup(html.content,"html.parser")

view_str = soup.prettify

ps = soup.find_all("p",class_="name")

name_list = []
for p in ps:
    name_list.append(p.span.string)
    replaced_name_list = [s.replace('\u3000',' ') for s in name_list]
print(replaced_name_list)

#print sys.stdout.encodeing

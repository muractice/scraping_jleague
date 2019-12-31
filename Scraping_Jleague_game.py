# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys

def get_member_list(area):

    title_name = area.find_all("h4",class_="two-column-table-st-base")[0].string
    print (title_name)

    positions_tag = area.find_all("td",class_="position")
    positions = []
    for position_tag in positions_tag:
        positions.append(position_tag.span.string)

    numbers_tag = area.find_all("td",class_="number")
    numbers = []
    for number_tag in numbers_tag:
        numbers.append(number_tag.string)


    player_names_tag = area.find_all("td",class_="name")
    player_names = []
    relaced_player_names = []
    for player_name_tag in player_names_tag:
        relaced_player_names.append(player_name_tag.string.strip())
#        player_names.append(player_name_tag.get_text)

    '''
    relaced_player_names = []
    for name in player_names:
        relaced_player_names.append(
            str(name).replace(' ','')
            .replace('<boundmethodTag.get_textof<tdclass="name">\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t','')
            .replace('</td>','')
            .replace('\u3000',' ')
            .replace('>','')
            )
    '''

    i=0
    for player in relaced_player_names:
        view_str = positions[i] + " " + numbers[i] + " " + relaced_player_names[i]
#        view_str = relaced_player_names[i]
        print (view_str)
        i = i+1
    print ("\n")

def get_team_info(soup,area):
    team_left_area_list = soup.find_all("div",class_= area)
    team_name = team_left_area_list[0].find_all("h3",class_="two-column-table-t-base")[0].string
    print (team_name)
    get_member_list(team_left_area_list[0])
    get_member_list(team_left_area_list[1])


def main():
    url = "https://data.j-league.or.jp/SFMS02/?match_card_id=21776"
    html = requests.get(url)

    parsed_html = BeautifulSoup(html.content,"html.parser")

    get_team_info(parsed_html,"two-column-table-box-l")
    get_team_info(parsed_html,"two-column-table-box-r")

main()

# coding=utf-8
import requests, json
import os.path as path
from bs4 import BeautifulSoup
import re


def get_enents():
	url = "https://api.matsurihi.me/mltd/v1/events"

	r = requests.get(url)
	data = r.json()
	# my_data = []
	e_tour = []
	e_theater = []
	for e in data:
	    if e['type'] == 3:
	        e_name = e['name'][12:-1]
	        e_theater.append({"id": e['id'], "name": e_name})
	    if e['type'] == 4:
	        e_name = e['name'][11:-1]
	        e_tour.append({"id": e['id'], "name": e_name})

	e_data = [e_theater, e_tour]
	with open('events_list.json', 'w') as f:
	    json.dump(e_data ,f)

if __name__ == '__main__':
	get_enents()
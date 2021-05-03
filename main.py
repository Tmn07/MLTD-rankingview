# coding=utf-8
import requests, json
from bs4 import BeautifulSoup
from os import path
from getEventData import get_eventdata

from log import *


def get_events(upload=False):
    url = "https://api.matsurihi.me/mltd/v1/events"
    try: 
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            # my_data = []
            e_tour = []
            e_theater = []
            e_tune = []
            e_twin = []
            
            last = -1
            ddir = "data/"
            pst_event_type = [3,4,10,11,12]

            for e in data:
                if e['type'] == 3:
                    e_name = e['name'][12:-1]
                    e_theater.append({"id": e['id'], "name": e_name})
                if e['type'] == 4:
                    e_name = e['name'][11:-1]
                    e_tour.append({"id": e['id'], "name": e_name})
                if e['type'] == 11:
                    e_name = e['name'][12:-1]
                    e_tune.append({"id": e['id'], "name": e_name})
                if e['type'] == 10 or e['type'] == 12:
                    e_name = e['name'][20:-1]
                    e_twin.append({"id": e['id'], "name": e_name})
                if e['type'] in pst_event_type:
                    last = e['id']
            
            # pst活动已经结束 且 还没有保存过上一个pst活动的数据
            if (e['type'] not in pst_event_type) and (not path.exists(ddir+str(last)+'.json')):
                get_eventdata(str(last))

            e_data = [e_theater, e_tour, e_tune, e_twin]
            with open('events.json', 'w') as f:
                json.dump(e_data ,f)
                logging.info("events.json update")
            
            # if upload:
            #     from qnlib.test import *
            #     q = Auth(access_key, secret_key)
            #     print (delete_data(q, "rank_v1912/events_list.json"))
            #     print (upload_data(q, "rank_v1912/events_list.json", 'events_list.json'))
            #     print (refresh_data(q, 'https://tmn07.com/rank_v1912/events_list.json'))
        else:
            logging.error(f'status_code:{r.status_code}')
    except Exception as e:
        logging.error(f'Exception:{e}')




if __name__ == '__main__':
    get_events(False)
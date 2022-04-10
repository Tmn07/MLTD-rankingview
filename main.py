# coding=utf-8
import requests, json
from os import path
import datetime

from getEventData import get_eventdata
from log import *

def getDuration(e):
    str_p0 = e['schedule']['beginDate'][:10]
    date_p0 = datetime.datetime.strptime(str_p0,'%Y-%m-%d').date()
    str_p = e['schedule']['endDate'][:10]
    date_p = datetime.datetime.strptime(str_p,'%Y-%m-%d').date()
    days = (date_p-date_p0).days
    return days

def get_events(getLast=False,upload=False):
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
            e_tail = []
            
            last = -1
            ddir = "data/"
            pst_event_type = [3,4,10,11,12,13]

            for e in data:
                # todo: 今后可以考虑改成正则表达式匹配
                if e['type'] == 3:
                    e_name = e['name'].split("～")[-2]
                    e_theater.append({"id": e['id'], "name": e_name, "duration": getDuration(e)})
                if e['type'] == 4:
                    e_name = e['name'].split("～")[-2]
                    e_tour.append({"id": e['id'], "name": e_name, "duration": getDuration(e)})
                if e['type'] == 11:
                    e_name = e['name'].split("～")[-2]
                    e_tune.append({"id": e['id'], "name": e_name, "duration": getDuration(e)})
                if e['type'] == 10 or e['type'] == 12:
                    e_name = e['name'].split("～")[-2]
                    e_twin.append({"id": e['id'], "name": e_name, "duration": getDuration(e)})
                if e['type'] ==13:
                    e_name = e['name'].split("～")[-2]
                    e_tail.append({"id": e['id'], "name": e_name, "duration": getDuration(e)})

                if e['type'] in pst_event_type:
                    last = e['id']
            
            # pst活动已经结束 且 还没有保存过上一个pst活动的数据
            if getLast:
                # 当前活动非pst活动（即pst活动结束）
                if (e['type'] not in pst_event_type) and (not path.exists(ddir+str(last)+'.json')):
                    get_eventdata(str(last))

            e_data = [e_theater, e_tour, e_tune, e_twin, e_tail]
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
    # 只更新events.json
    get_events(False,False)
    # 线上部署，检查上一个活动数据是否保存
    # get_events(True,False)

# coding=utf-8
#####  统计活动参数与人数的
import requests, json
from bs4 import BeautifulSoup
from os import path
from getEventData import get_eventdata

from log import *


url = "https://api.matsurihi.me/mltd/v1/events"

# try: 
r = requests.get(url)
if r.status_code == 200:
    data = r.json()
    # my_data = []
    enames = []
    enums = []
    etimes = []
    
    pst_event_type = [3,4,5,10,11,12]
    for e in data:
        if e['type'] in pst_event_type:
            eid = e['id']
            ename = e['name']
            etime = e['schedule']['endDate'][:-15]
            count_url = f"https://api.matsurihi.me/mltd/v1/events/{eid}/rankings/summaries/eventPoint"
            r2 = requests.get(count_url)
            data_c = r2.json()
            if len(data_c) == 0:
                print(eid,etime,'lost')
            else:
                enames.append(ename)
                etimes.append(etime)
                enums.append(data_c[-1]['count'])
                print(eid,etime,data_c[-1]['count'])

with open('nums.csv','w') as f:
    for et in etimes:
        f.write(et+",")
    f.write('\n')
    # for en in enames:
    #     f.write(en+",")
    # f.write('\n')
    for en in enums:
        f.write(str(en)+",")
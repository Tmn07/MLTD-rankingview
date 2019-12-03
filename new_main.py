# coding=utf-8
import requests, json
import os.path as path
from bs4 import BeautifulSoup
import re
from event_list import get_events

def get_loglenth(eid = "108"):
    url = "https://api.matsurihi.me/mltd/v1/events/"+eid+"/rankings/logs/eventPoint/100,2500,5000,10000"
    r = requests.get(url)
    data = r.json()
    nums = len(data)
    for i in range(nums):
        print(len(data[i]['data']))

def get_eventdata_old(eid="32"):
    url = "https://otomestorm.anzu.work/events/"+eid+"/rankings/event_point"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Origin": "https://si.ster.li",
        "Referer": "https://si.ster.li/events/"+eid,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

    r = requests.get(url, headers=headers)
    jsondata = json.loads(r.text)
    if jsondata['status'] == 1:
        result = {"id": eid, 'borders': jsondata['data']['borders'][:-3]}
        log_point = []
        lenth = len(jsondata['data']['logs'])
        for t in range(lenth):
            data_point = []
            if int(eid)>10:
                data_point.append(jsondata['data']['logs'][t]['borders']['100'])
            data_point.append(jsondata['data']['logs'][t]['borders']['2000'])
            data_point.append(jsondata['data']['logs'][t]['borders']['5000'])
            data_point.append(jsondata['data']['logs'][t]['borders']['20000'])
            data_time = jsondata['data']['logs'][t]['datetime']
            if eid=="32":
                data_time = data_time[:-6]
            data_dict = {"t": data_time[11:-3], "d": data_point}
            log_point.append(data_dict)

        result['log'] = log_point
        with open('new_data/'+eid+'.json', 'w') as f:
            json.dump(result, f)
            print(eid+'.json save')
    else:
        print(eid+" error")    

def get_eventdata(eid = "108", upload=False):
    # 25000&50000 data loss...
    url = "https://api.matsurihi.me/mltd/v1/events/"+eid+"/rankings/logs/eventPoint/100,2500,5000,10000"
    r = requests.get(url)
    data = r.json()
    lenth = len(data[0]['data'])
    result = {"id": eid, 'borders':[100,2500,5000,10000]}
    log_point = []

    # 验证长度是否一致
    # nums = len(data)
    # pre = len(data[0]['data'])
    # print(pre)
    # for i in range(1, nums):
    #     tmp = len(data[i]['data'])
    #     print(tmp)
    #     if tmp == pre:
    #         pre = tmp
    #         continue
    #     else:
    #         print('wrong:' + eid)
    #         return 0

    for t in range(lenth):
        data_point = []
        data_point.append(int(data[0]["data"][t]["score"]))
        data_point.append(int(data[1]["data"][t]["score"]))
        data_point.append(int(data[2]["data"][t]["score"]))
        data_point.append(int(data[3]["data"][t]["score"]))
        data_time = data[0]['data'][t]["summaryTime"]
        data_dict = {"t": data_time[11:-9], "d": data_point}
        log_point.append(data_dict)

    result['log'] = log_point
    with open('new_data/'+eid+'.json', 'w') as f:
        json.dump(result ,f)
        print(eid + " save ok")
    if upload:
        from qnlib.test import *
        q = Auth(access_key, secret_key)
        upload_info = upload_data(q, "rank_v1911/"+eid+".json", 'new_data/'+eid+'.json')
        if upload_info.status_code==200:
            print(eid + ".json upload ok")
        else:
            print(upload_info)


# all_data
# url = "https://api.matsurihi.me/mltd/v1/events"
# r = requests.get(url)
# data = r.json()

# for e in data:
#     if (e['type'] == 3 or e['type'] == 4) and e['id']>32:
#         get_eventdata(str(e['id']))
#     if (e['type'] == 3 or e['type'] == 4) and e['id']<=32:
#         print(str(e['id']))
#         get_eventdata_old(str(e['id']))


get_eventdata('102', upload=True)
get_events(upload=True)
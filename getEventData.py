# coding=utf-8
import requests, json
from bs4 import BeautifulSoup
# from event_list import get_events
import json
from os import path
from os import mkdir

from log import *

def get_loglength(eid = "108"):
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
        length = len(jsondata['data']['logs'])
        for t in range(length):
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
        with open(ddir+eid+'.json', 'w') as f:
            json.dump(result, f)
            print(eid+'.json saved')
    else:
        print(eid+" error")    


def get_eventdata(eid = "108", borders=[100,2500,5000,10000], ddir='data/', upload=False):
    # 25000&50000 data loss...
    borders_url = ','.join(map(str,borders))
    url = "https://api.matsurihi.me/mltd/v1/events/"+eid+"/rankings/logs/eventPoint/"+borders_url
    r = requests.get(url)
    data = r.json()
    length = len(data[0]['data'])
    # old borders=[100,2000,5000,10000]
    result = {"id": eid, 'borders':borders}
    log_point = []

    lengths = [len(data[i]['data']) for i in range(len(borders))]

    d1 = lengths[1] - length
    d2 = lengths[2] - length
    d3 = lengths[3] - length

    # 验证长度是否一致
    # nums = len(data)
    # pre = len(data[0]['data'])
    # # print(pre)
    # for i in range(1, nums):
    #     tmp = len(data[i]['data'])
    #     print(tmp)
    #     if tmp == pre:
    #         pre = tmp
    #         continue
    #     else:
    #         print('wrong:' + eid)
    #         return 0

    for t in range(length):
        data_point = []
        data_point.append(int(data[0]["data"][t]["score"]))
        if t <-d1:
            data_point.append(0)
        else:
            data_point.append(int(data[1]["data"][t+d1]["score"]))

        if t <-d2:
            data_point.append(0)
        else:
            data_point.append(int(data[2]["data"][t+d2]["score"]))

        if t <-d3:
            data_point.append(0)
        else:
            data_point.append(int(data[3]["data"][t+d3]["score"]))

        data_time = data[0]['data'][t]["summaryTime"]
        data_dict = {"t": data_time[11:-9], "d": data_point}
        log_point.append(data_dict)

    result['log'] = log_point
    with open(ddir+eid+'.json', 'w') as f:
        json.dump(result ,f)
        # print(eid + " saved")
        logging.info(eid + " saved")

    # if upload:
    #     from qnlib.test import *
    #     q = Auth(access_key, secret_key)
    #     upload_info = upload_data(q, "rank_v1912/"+eid+".json", 'new_data/'+eid+'.json')
    #     if upload_info.status_code==200:
    #         print(eid + ".json upload ok")
    #     else:
    #         print(upload_info)





if __name__ == '__main__':

    # single data
    get_eventdata(eid = "196")

    # all_data
    # pst_event_type = [3,4,10,11,12]
    # pst_newid = 32
    # ddir = "data/"
    # if not path.exists(ddir):
    #     mkdir(ddir)
    # 
    # url = "https://api.matsurihi.me/mltd/v1/events"
    # r = requests.get(url)
    # data = r.json()
    # for e in data:
    #     if e['type'] in pst_event_type and e['id']>pst_newid:
    #         get_eventdata(str(e['id']))

    #     old pst data lost
    #     if e['type'] in pst_event_type and e['id']<=pst_newid:
    #         get_eventdata(str(e['id']), [100,2000,5000,10000])

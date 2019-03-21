# coding=utf-8
import requests, json
import os.path as path
from bs4 import BeautifulSoup
import re
# 44 1周年活动

newest = '78'
# 想要比对的
# 72,68,52,56,64
nums = ['78','72', '68', '52', '56', '64']
ranking = '100'
data_dir = './data/'

def get_data(num):
    if path.exists(data_dir+num+'.json') and num != newest:
        print(num+'.json pass')
    else:
        url = "https://otomestorm.anzu.work/events/"+num+"/rankings/event_point"
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Origin": "https://si.ster.li",
            "Referer": "https://si.ster.li/events/"+num,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }

        r = requests.get(url, headers=headers)
        jsondata = json.loads(r.text)
        if jsondata['status'] == 1:
            with open(data_dir+num+'.json', 'w') as f:
                json.dump(jsondata, f)
                print(num+'.json save')
        else:
            print(num+" pass")

# map(get_data, nums)
def write_csv(nums, rank, mode):
    with open('data.csv', mode) as f:
        for num in nums:
            jsondata = json.load(open(data_dir+num+'.json'))
            f.write(num+',')
            f.write(','.join(map(str,[data['borders'][rank] for data in jsondata['data']['logs']])))
            f.write('\n')
        print('compare data in data.csv')

def get_eventname():
    url = "https://si.ster.li/events/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    eves = soup.find_all(href=re.compile("event"))
    data = {'tour': {}, 'theater': {}}
    for e in eves:
        # theater
        event_num = e.attrs['href'].split('/')[-1]
        if e.text[:11] == u'プラチナスターシアター':
            data['theater'][event_num] = e.text[12:-1]
        # tour 
        if e.text[:10] == u'プラチナスターツアー':
            data['tour'][event_num] = e.text[11:-1]
    with open('events.json', 'w') as f:
        json.dump(data ,f)

# 下载数据
# map(get_data, nums)
# map(get_data, map(str,range(4,78)))

# 比对数据
# write_csv(nums, '2500', 'w')

# write_csv(['72', '68', '56'],'2500', 'w')
# write_csv(['27'],'2000', 'a')

get_eventname()
# ミリシア PST ranking view

偶像大师百万现场剧场时光 pst活动 排名数据表（好别扭的名字

![](./resource/show.png)

## 代码结构

new_main.py 相关数据爬虫 (requests, BeautifulSoup, [qiniu])

index.html 主页

new_data 手动建目录 存储数据

events_list.json 活动信息列表

qnlib 目录下编辑config-bak.py 另存为config.py

## TODO

- [ ] 优化界面
- [x] 爬取数据后自动上传cdn
- [ ] 时间对齐（因为有部分漏的数据）

## TIP

```bash
# 临时测试用server
# python2
python -m SimpleHTTPServer 8080
# python3
python -m http.server 8080
```
# coding=utf-8
import json
# 4条需要填充.. 手动填？
# 35 各漏一条，手动处理...  , {"t": "16:30", "d": [16342, 2622, 1904, 1044]}
# 62
eid = "68"
with open("modif_data/"+eid+".json") as f:
	data = json.load(f)

result = {"id": eid, 'borders': [
    100,
    2500,
    5000,
    10000
]}
result["log"] = []
for i in data["data"]["logs"]:
	tmp = {}
	d = [i["borders"]["100"],
		i["borders"]["2500"],
		i["borders"]["5000"],
		i["borders"]["10000"]]
	
	tmp["d"] = d
	tmp["t"] = i['datetime'][11:16]
	result["log"].append(tmp)

with open('new_data/'+eid+'_modif.json', 'w') as f:
	json.dump(result, f)
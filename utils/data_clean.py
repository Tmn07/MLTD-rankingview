# coding=utf-8
import json
from os import listdir
from math import floor

def read_data(eid):
	# +str(eid)+".json"
	with open("new_data/"+eid) as f:
		data = json.load(f)
	return data

# data = read_data(100)
# 假设没有超过连续2条的缺失

# new_data
allfile = listdir("new_data/")

lengths = []
for f in allfile:
	data = read_data(f)
	eid = int(f.split('.')[0])
	# 64之前 无20:30数据
	# if eid < 62:
	# 	length = len(data['log'])
		# print (eid, length)
	# 	data_2 = data['log'][-2]['d']
	# 	data_1 = data['log'][-1]['d']
	# 	data_fill = []
	# 	for i in range(4):
	# 		tmp = int(floor((data_1[i]+data_2[i])/2))
	# 		data_fill.append(tmp)
	# 	new = {"t": "20:30", "d": data_fill}
	# 	data['log'].insert(-1, new)
	# 	with open("modif_data/"+str(eid)+'.json', 'w') as fp:
	# 		json.dump(data ,fp)

	length = len(data['log'])
	
	# fp = open('tmp.csv' ,'a')
# 	fp = open('348_modif1.csv' ,'a')
# 	# fp = open("300_modif1.csv", 'a')
# 	# fp = open("396_modif1.csv", 'a')
# 	# if length < 310:
# 	# if length>340 and length < 350:
# 	if length>390 and length < 400:
# 		print (eid, length)
# 		log_data = data['log']
# 		logs = []
# 		for d in log_data:
# 			fp.write(d['t']+",")
# 			logs.append(d['d'][1]) 

# 		fp.write('\n')
# 		for i in logs:
# 			fp.write(str(i)+",")
# 		fp.write('\n')	

# fp.close()


	# if length in [300,348,396]:
	# 	continue
	# else:
	# 	log_data = data['log']
	# 	tmp = log_data[0]['t']
	# 	for d in log_data[1:]:
	# 		if isNext(d['t'], tmp):
	# 			pass
	# 		else:

	lengths.append(length)
	print(f ,length)
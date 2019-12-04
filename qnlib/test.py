# -*- coding: utf-8 -*-

from qiniu import Auth, put_file, etag, BucketManager, CdnManager
from config import *


def delete_data(q, path):
	#初始化BucketManager
	bucket = BucketManager(q)
	#你要测试的空间， 并且这个key在你空间中存在
	key = path
	#删除bucket_name 中的文件 key
	ret, info = bucket.delete(bucket_name, key)
	# assert ret == {}
	return info

def upload_data(q, path_file, localfile):
	#上传后保存的文件名
	# key = 'my-test.png'
	key = path_file
	#生成上传 Token，可以指定过期时间等
	token = q.upload_token(bucket_name, key, 3600)
	#要上传文件的本地路径
	# localfile = r'C:\Users\Tmn07\Desktop\project\ranking\test\merry.png'
	ret, info = put_file(token, key, localfile)
	# print info.status_code
	assert ret['key'] == key
	assert ret['hash'] == etag(localfile)
	return info


def refresh_data(q, url):
	cdn_manager = CdnManager(q)
	# 需要刷新的文件链接
	urls = [
		url,
	    # 'https://tmn07.com/rank_v1911/events_list.json',
	]
	# 刷新链接
	refresh_url_result = cdn_manager.refresh_urls(urls)
	return refresh_url_result



if __name__ == '__main__':
	q = Auth(access_key, secret_key)
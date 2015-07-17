#!/usr/bin/env python
# coding:utf-8
import sys
import urllib2
import time
import json
import redis
reload(sys)
sys.setdefaultencoding('utf-8')
#userid = sys.argv[1]
#title = sys.argv[2]   # 位置参数获取title 适用于zabbix
#content = sys.argv[3] # 位置参数获取content 适用于zabbix

class Token(object):
    # 获取token
    def __init__(self, corpid, corpsecret):
        self.baseurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}'.format(
        corpid,corpsecret)
        self.r = redis.Redis(host='10.16.48.81',port=6379)
        self.expire_time = eval(self.r['token'])['expires_in']
    def get_token(self):
        if self.expire_time < int(time.time()): #如果超时时间小于当前时间 重新获取token
            request = urllib2.Request(self.baseurl)
            response = urllib2.urlopen(request)
            ret = response.read().strip()
            ret = json.loads(ret)
            ret['expires_in'] += int(time.time())
            access_token = ret['access_token']
            self.r['token'] = ret
            return access_token
        else:
            return eval(self.r['token'])['access_token']

def send_msg(title,userid,content):
    # 发送消息
    corpid = "xxxxxxxx"  # 填写企业号的id 
    corpsecret = "xxxxxxxxx" # 填写应用的id 这个id可以重置
    qs_token = Token(corpid=corpid, corpsecret=corpsecret).get_token()
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}".format(
        qs_token)
    payload = {
        "touser": userid,
        "msgtype": "text",
        "agentid": "0",
        "text": {
                   "content": "标题:{0}\n 内容:{1}".format(title, content)
        },
        "safe": "0"
    }
    ret = urllib2.urlopen(url, data=json.dumps(payload, ensure_ascii=False))
    return ret.read()

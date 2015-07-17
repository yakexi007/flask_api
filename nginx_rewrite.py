#!/usr/bin/env 	python
#__author__:zhangjun

from flask import Flask,jsonify,request,redirect
from mysqldb import *
import hashlib,random
app = Flask(__name__)

li = [x for x in range(100)]
@app.route('/distribute_platform/')
@app.route('/distribute_platform/<a>/<b>/')
@app.route('/distribute_platform/<a>/<b>/<c>/')
@app.route('/distribute_platform/<a>/<b>/<c>/<d>/')
@app.route('/distribute_platform/<a>/<b>/<c>/<d>/<e>/')
@app.route('/distribute_platform/<a>/<b>/<c>/<d>/<e>/<f>/')
@app.route('/distribute_platform/<a>/<b>/<c>/<d>/<e>/<f>/<h>/')
def down(a=None,b=None,c=None,d=None,e=None,f=None,h=None):
    x = request.base_url.split('/')
    id = str(random.choice(li))
    data = mysql()
    nginx_ip = data.exec_redis()
    hostHash = hashlib.md5()
    hostHash.update(id)
    hostIndex = nginx_ip[ord(hostHash.digest()[-1:]) % len(nginx_ip)][0]
    print hostIndex
    x[2] = hostIndex
    url = '/'.join(x[:-1])
    return redirect(url,code=301)

@app.route('/silent_download/')
@app.route('/silent_download/<a>/<b>/')
@app.route('/silent_download/<a>/<b>/<c>/')
@app.route('/silent_download/<a>/<b>/<c>/<d>/')
@app.route('/silent_download/<a>/<b>/<c>/<d>/<e>/')
@app.route('/silent_download/<a>/<b>/<c>/<d>/<e>/<f>/')
@app.route('/silent_download/<a>/<b>/<c>/<d>/<e>/<f>/<h>/')
def down1(a=None,b=None,c=None,d=None,e=None,f=None,h=None):
    x = request.base_url.split('/')
    id = str(random.choice(li))
    data = mysql()
    nginx_ip = data.exec_redis()
    hostHash = hashlib.md5()
    hostHash.update(id)
    hostIndex = nginx_ip[ord(hostHash.digest()[-1:]) % len(nginx_ip)][0]
    print hostIndex
    x[2] = hostIndex
    url = '/'.join(x[:-1])
    return redirect(url,code=301)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9191)

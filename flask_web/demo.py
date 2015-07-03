#!/usr/bin/env  python
#coding:utf-8

from flask import Flask,jsonify,request,render_template
from mysqld import *
app = Flask(__name__)
app.debug = True

@app.route("/data/",methods=['GET','POST'])
def hello():
    #name = request.args.get("name")
    name = request.form['name']
    return jsonify({"name":name})

@app.route("/")
def index():
    data = getData()
    num = 1
    return render_template("index.html",data = data, num = num)

@app.route("/page",methods=['GET'])
def page():
    act = request.args.get('act')
    num = int(request.args.get('num'))
    data = getData()
    if act == 'a':num-=1
    if act == 'b':num+=1
    print act,num
    return render_template("index.html",data = data, num = num)

@app.route("/search_ip",methods=['GET'])
def search():
    ip = request.args.get("ip")
    data = serData(ip)
    print ip
    return render_template("index.html",data = data, num = 1)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=2324)

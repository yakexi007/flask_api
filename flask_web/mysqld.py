#!/usr/bin/env	python
#coding:utf-8
__author__ = "zhangjun"

import MySQLdb

conn = MySQLdb.connect(host='10.16.48.81',user='root',passwd='123',db='weblog',charset='utf8')
cur = conn.cursor()

def getData():
    sql = "select ip,status from download_nginx_copy"
    cur.execute(sql)
    data = cur.fetchall()
    return data

def serData(ip):
    sql = "select ip,status from download_nginx where ip LIKE '%%%s%%'" %ip
    print sql
    cur.execute(sql)
    data = cur.fetchall()
    return data

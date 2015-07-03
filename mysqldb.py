#!/usr/bin/env	python
import MySQLdb
import redis

class mysql:
    def __init__(self):
        self.conn = MySQLdb.connect(host="10.16.48.81",db="weblog",user="root",passwd="123",charset="utf8")
        self.cur = self.conn.cursor()
        self.r = redis.Redis(host='10.16.48.81',port=6379)

    def exec_sql(self):
        sql = "select ip from download_nginx where status = 'active'"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        self.r.set('download',data)
        return data

    def exec_redis(self):
        data = eval(self.r['download'])
        return data

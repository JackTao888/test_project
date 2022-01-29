#!/usr/bin/env python3
#!coding: utf-8
import random
import sys, os, time
import math
import pymysql
import math
import operator
from flask import Flask, make_response, request

app = Flask(__name__)




@app.route("/",methods = ["GET","POST"])
def my_root():
    f = open(r"d:\2.html","r")

    lines = f.readlines()
    res = ""
    for line in lines:
        res += line
    a = res.encode("utf8").decode("utf8")

    return make_response(a)

@app.route("/register", methods = ["GET","POST"])
def register():
    parameters = request.form.to_dict()
    username = parameters["username2"]
    password = parameters["password2"]

    insert(username, password)
    a = count()

    return "You have login successfully, there are now {} person".format(a[0])

@app.route("/login", methods=["GET", "POST"])
def login():
    db = pymysql.connect(host="localhost", user="root", password="", database="taorj", charset="utf8")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select username, password from userinfo")
    data = cursor.fetchall()
    a = count()

    parameters = request.form.to_dict()
    username1 = parameters["username1"]
    password1 = parameters["password1"]
    i = 0
    j = 0
    for i in range(a[0]):
        if username1 == data[i]:
            for j in range(a[0]):
                if password1 == data[j]:
                    return "You have login successfully, there are now {} person".format(a[0])
                j+= 1
        else:
            i+= 1
    return "wrong password or username."


def query():
    db = pymysql.connect(host= "localhost",user= "root", password="", database= "taorj", charset="utf8")
    cursor = db.cursor()
    query01 = "select * ,DATE_FORMAT('%Y-%m-%d') from userinfo limit 3;"
    cursor.execute(query01)
    row01 = cursor.fetchone()
    while row01 is not None:
        print(row01)
        row01 = cursor.fetchone()
    print("############################")


 return

def insert(username,password):
    db = pymysql.connect(host= "localhost",user= "root", password="", database= "taorj", charset="utf8")
    cursor = db.cursor()
    #cursor.execute("insert into userinfo(username, password) values('{}', '{}')".format(username, password) )
    sql = "insert into userinfo(username, password) values(%s, %s)"

    res = cursor.execute(sql,("{}".format(username), "{}".format(password)))
    #res = cursor.executemany(sql, [("{}".format(username), "{}".format(password)),("{}".format(password), "{}".format(username))])
    print("res ={}".format(res))
    print("res =%d" % (res))
    print("res =", res)

    db.commit()
    print("last row id = ", cursor.lastrowid)
    cursor.close()
    db.close()
    print("====================================")


def count():
    db = pymysql.connect(host="localhost", user="root", password="", database="taorj", charset='utf8')
    cursor = db.cursor()
    cursor.execute("SELECT count(*) from userinfo")
    data = cursor.fetchall()

    for i in range(len(data)):
        print(data[i])
    cursor.close()
    db.close()

    return data[0]

    print("====================================")


def delete(column1, line1):
    db = pymysql.connect(host= "localhost",user= "root", password="", database= "taorj", charset="utf8")
    cursor = db.cursor()
    cursor.execute("delete from userinfo where column_name = column1 or raw_name = line1 ")
    db.commit()
    cursor.close()
    db.close()

    print("====================================")

def select():
    # 连接数据库
    db = pymysql.connect(host="localhost", user="root", password="", database="taorj", charset='utf8')
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM userinfo")

    data = cursor.fetchall()
    print("1.fetchall=")
    for i in range(len(data)):
        print(data[i])
    #print(cursor.description)

    data = cursor.fetchall()
    print("2.fetchall=")
    for i in range(len(data)):
        print(data[i])

    cursor.scroll(10, mode='absolute')  # 相对首行移动了0，就是把行指针移动到了首行
    data = cursor.fetchall()
    print("3.fetchall=")
    for i in range(len(data)):
        print(data[i])

    print("====================================")
    # 打印获取到的数据
    #print(data)

    # 关闭游标和数据库的连接
    cursor.close()
    db.close()



if __name__ == "__main__":
    app.run(port = 80, host = "0.0.0.0",debug = True)

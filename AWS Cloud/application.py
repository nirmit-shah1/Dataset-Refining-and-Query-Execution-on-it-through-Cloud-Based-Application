from flask import Flask, request, render_template
import pymysql
import sys
import csv
import pandas as pd
import requests


application=Flask(__name__)

@application.route("/")
def index():    
    return render_template('index.html')

@application.route("/taskone",methods=['GET','POST'])
def taskone():
    info='none'
    value=request.form['data']
    filename = 'EnglishWordsMostFreq.csv'
    data = pd.read_csv(filename, header=None)
    stocklist = list(data.values.flatten())
    for word in stocklist:
        demo=str(word)
        if demo==value:
            info="hello"
    return render_template('taskone.html',demo=value,info=info)
@application.route("/tasktwo",methods=['GET','POST'])
def tasktwo():
    info='none'
    value=request.form['data']
    d1=value.split(" ")
    filename = 'EnglishWordsMostFreq.csv'
    data = pd.read_csv(filename, header=None)
    stocklist = list(data.values.flatten())
    final=""
    notfinal=" "
    for dd in d1:
        for word in stocklist:
            demo=str(word)
            if demo==dd:
                final=final+","+dd
                break
            else:
                notfinal=notfinal+","+dd
                break
    return render_template('tasktwo.html',val=value,info=info,final=final, notfinal=notfinal)
@application.route("/taskthree",methods=['GET','POST'])
def taskthree():
    value=request.form['data']
    return render_template('taskthree.html',val=value)
@application.route("/taskfour",methods=['GET','POST'])
def taskfour():
    info='none'
    value=str(request.form['data'])
    data1=value.replace(',', ' ')
    data = pd.read_csv("SpanishEnglishFreq.csv", index_col = 0, header=None, encoding='cp1252' )
    stocklist = list(data.values.flatten())
    for word in stocklist:
        demo=str(word)
        if demo==data1:
            info="hello"
    return render_template('taskfour.html',demo=data1,info=info)
if __name__=='__main__':
    application.run()
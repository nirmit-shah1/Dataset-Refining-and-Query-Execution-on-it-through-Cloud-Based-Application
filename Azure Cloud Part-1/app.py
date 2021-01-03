import json
from flask import Flask,render_template, url_for, flash, redirect, request
import random
from datetime import date, timedelta, datetime
import os
import redis
import pyodbc


app = Flask(__name__)

@app.route("/")
def index():
        return render_template('index.html')
@app.route('/taskone',methods= ['POST','GET'])
def taskone():
    cname = str(request.form.get('cname'))
    syear=str(request.form.get('syear'))
    eyear=str(request.form.get('eyear'))
    server = 'nirmit.database.windows.net'
    database = 'earthquake'
    username = 'nirmitshah'
    password = 'nirmit@123'
    driver= '{ODBC Driver 17 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT COUNT(*) AS TOTAL,Year FROM dbo.s WHERE (Entity=? )AND Year Between ? and ? GROUP BY YEAR",cname,syear,eyear)
    rows = cursor.fetchall()
    sums=0
    for i in range(0,len(rows)):
            sums=sums+int(rows[i][0])
    tabledata1 = []
    for i in range(0,len(rows)):
        tabledata1.append({
                'range': rows[i][1],
                'count': float((rows[i][0])/sums)})    
    return render_template('taskone.html',data=tabledata1)
@app.route('/tasktwo',methods= ['POST','GET'])
def tasktwo():
    cname = str(request.form.get('cname'))
    syear=str(request.form.get('syear'))
    eyear=str(request.form.get('eyear'))
    server = 'nirmit.database.windows.net'
    database = 'earthquake'
    username = 'nirmitshah'
    password = 'nirmit@123'
    driver= '{ODBC Driver 17 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT Year FROM dbo.s ORDER BY YEAR DESC")
    abc= cursor.fetchall()
    maxyear=abc[0][0]
    cursor.execute("SELECT Year FROM dbo.s ORDER BY YEAR ASC")
    xyz= cursor.fetchall()
    minyear=xyz[0][0]
    cursor.execute("SELECT Year,Smokers FROM dbo.s WHERE (Entity=? )AND Year Between ? and ? GROUP BY YEAR,Smokers",cname,syear,eyear)
    rows = cursor.fetchall()
    tabledata1=[]
    for i in range(0,len(rows)):
            if int(rows[i][0])>int(maxyear) or int(rows[i][0])<int(minyear):
                
                    tabledata1.append({
                'xaxis':str( rows[i][0]),
                'yaxis':'0'})            
            tabledata1.append({
                'xaxis': str(rows[i][0]),
                'yaxis':str( rows[i][1])})    
    
    return render_template('tasktwo.html',data=tabledata1)





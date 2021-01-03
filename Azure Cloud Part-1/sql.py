from flask import Flask,render_template, url_for, flash, redirect, request
from datetime import date, timedelta, datetime
import os
import redis
import pyodbc
import json

l1="12"
l2="13"
myHostname = "nirmit.redis.cache.windows.net"
myPassword = "DH63WTOukcA2CRPCkS2rR+odtCeAl6GsshvLFzAFKmg="
r = redis.StrictRedis(host=myHostname, port=6380,password=myPassword, ssl=True) 
server = 'nirmit.database.windows.net'
database = 'earthquake'
username = 'nirmitshah'
password = 'nirmit@123'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT time,mag,place from dbo.EARTHQUAKE_TABLE where latitude between ? and ?",l1,l2)
rows = cursor.fetchall()
tableData = []
for i in range(0,len(rows)):
    tableData += [{
            'time': rows[i][0],
            'lat': rows[i][1],
            'long': rows[i][2],
        }]
print(tableData)

rows=tableData
print(rows)

    

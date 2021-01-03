import os,fnmatch
import shutil
import pandas as pd
import ibm_db
import csv
from datetime import date, timedelta
import sys
from flask import Flask,render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField, validators
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Configurations
app.config['SECRET_KEY'] = 'blah blah blah blah'


# ROUTES!
@app.route('/', methods=['GET','POST'])
def index():
        return render_template('index.html')

@app.route('/help')
def help():
	text_list = []
	# Python Version
	text_list.append({
		'label':'Python Version',
		'value':str(sys.version)})
	# os.path.abspath(os.path.dirname(__file__))
	text_list.append({
		'label':'os.path.abspath(os.path.dirname(__file__))',
		'value':str(os.path.abspath(os.path.dirname(__file__)))
		})
	# OS Current Working Directory
	text_list.append({
		'label':'OS CWD',
		'value':str(os.getcwd())})
	# OS CWD Contents
	label = 'OS CWD Contents'
	value = ''
	text_list.append({
		'label':label,
		'value':value})
	return render_template('help.html',text_list=text_list,title='help')

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')
#================================ Task one========================================================


@app.route('/taskone')
def taskone():
    nir_dsn_hostname ="dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net"
    nir_dsn_uid = "mfm86030"        
    nir_dsn_pwd = "s17-fnd9c6p060xm"      
    nir_dsn_driver = "{IBM DB2 ODBC DRIVER}"
    nir_dsn_database = "BLUDB"            
    nir_dsn_protocol = "TCPIP" 
    nir_dsn_port ="50000"
    dsn_nir = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(nir_dsn_driver, nir_dsn_database, nir_dsn_hostname, nir_dsn_port, nir_dsn_protocol, nir_dsn_uid, nir_dsn_pwd)
    try:
        conn = ibm_db.connect(dsn_nir, "", "")
    except:
        print ("Unable to connect: ", ibm_db.conn_errormsg() )
    server = ibm_db.server_info(conn)
    sql = "SELECT * FROM EARTHQUAKE_TABLEQ ORDER BY DEPTH DESC LIMIT 1"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    col1_time=[]
    col2_latitude=[]
    while dictionary != False: 
        col1_time.append(dictionary[6])
        col2_latitude.append(dictionary[7])
        dictionary = ibm_db.fetch_both(stmt)
    sql1 = "SELECT COUNT(*) AS FINAL_data FROM EARTHQUAKE_TABLEQ"
    stmt1 = ibm_db.exec_immediate(conn, sql1)
    dictionary1 = ibm_db.fetch_both(stmt1)
    final_value=[] 
    while dictionary1 != False:
        final_value.append(dictionary1[0])
        dictionary1 = ibm_db.fetch_both(stmt1)
    
    return render_template('taskone.html',col1_time=col1_time,col2_latitude=col2_latitude,final_value=final_value)
############################################################################################################
@app.route('/tasktwo',methods=['POST'])
def tasktwo():
    lati1=str(request.form['number1'])
    longi1=str(request.form['number2'])
    lati2=str(request.form['number3'])
    longi2=str(request.form['number4'])
    value=str(request.form['number5'])
    nir_dsn_hostname ="dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net"
    nir_dsn_uid = "mfm86030"        
    nir_dsn_pwd = "s17-fnd9c6p060xm"      
    nir_dsn_driver = "{IBM DB2 ODBC DRIVER}"
    nir_dsn_database = "BLUDB"            
    nir_dsn_protocol = "TCPIP" 
    nir_dsn_port ="50000"
    dsn_nir = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(nir_dsn_driver, nir_dsn_database, nir_dsn_hostname, nir_dsn_port, nir_dsn_protocol, nir_dsn_uid, nir_dsn_pwd)
    try:
        conn = ibm_db.connect(dsn_nir, "", "")
    except:
        print ("Unable to connect: ", ibm_db.conn_errormsg() )
    server = ibm_db.server_info(conn)
    sql = "SELECT  COUNT(*) AS ct FROM EARTHQUAKE_TABLEQ WHERE (LATITUDE>="+lati1+" AND LATITUDE<="+lati2+") AND (LONGITUDE>="+longi1+" AND LONGITUDE<= "+longi2+")"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    demo2=[]
    while dictionary != False:
        demo2.append(dictionary[0])
        dictionary = ibm_db.fetch_both(stmt)
    return render_template('tasktwo.html',demo2=demo2,value=value)
@app.route('/taskthree',methods=['POST'])
def taskthree():
    n1=str(request.form['n1'])
    n2=str(request.form['n2'])
    nir_dsn_hostname ="dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net"
    nir_dsn_uid = "mfm86030"        
    nir_dsn_pwd = "s17-fnd9c6p060xm"      
    nir_dsn_driver = "{IBM DB2 ODBC DRIVER}"
    nir_dsn_database = "BLUDB"            
    nir_dsn_protocol = "TCPIP" 
    nir_dsn_port ="50000"
    dsn_nir = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(nir_dsn_driver, nir_dsn_database, nir_dsn_hostname, nir_dsn_port, nir_dsn_protocol, nir_dsn_uid, nir_dsn_pwd)
    try:
        conn = ibm_db.connect(dsn_nir, "", "")
    except:
        print ("Unable to connect: ", ibm_db.conn_errormsg() )
    server = ibm_db.server_info(conn)
    sql = "SELECT  * FROM EARTHQUAKE_TABLEQ WHERE (PLACE  LIKE '%"+n1+"%') AND (MAG >"+n2+") ORDER BY QUAKETIME ASC LIMIT 10)"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    demo1=[]
    demo2=[]
    demo3=[]
    demo4=[]
    while dictionary != False:
        demo1.append(dictionary[1])
        demo2.append(dictionary[2])
        demo3.append(dictionary[6])
        demo4.append(dictionary[7])
        dictionary = ibm_db.fetch_both(stmt)
    
    
    return render_template('taskthree.html',demo1=demo1,demo2=demo2,demo3=demo3,demo4=demo4)
port_data = int(os.getenv('PORT', '3000'))
app.run(host='0.0.0.0', port=port_data)
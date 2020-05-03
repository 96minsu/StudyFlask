
## config 설정
# app.config.from_object 메소드를 이용해서 splite config 설정
from flask import *
import sqlite3

#sqlite config
DATABASE='../db/my.db'
SECRET_KEY='my developement key'
USERNAME='root'
PASSWORD='1234'

# create the application instance :)
app=Flask(__name__)

# sqlite config read
# load config from this file , flaskr.py
app.config.from_object(__name__)




## Request hook을 이용
# request 처리 전 db connect를 만들고 table 생성하고 request 처리 후에 connect close
@app.before_request
def before_request():
    g.db = connect_db()
    createTalbe(g)
    print('before request')
    
@app.teardown_request
def teardown_request( exception ):
    g.db.close()
    print('end request')
    
@app.route('/')
def myTest():
    return "hello flask...:"

if __name__ == '__main__':
    app.run(use_reloader=True)
    
    
    
    
## 데이터베이스 connect
# 데이터베이스가 쉽게 접속할 수 있는 방법을 추가
def connect_db():
    return sqlite3.connect(ap.config['DATABASE'])




## 테이블 생성
# createTable 함수 정의
def createTable(g):
    try:
        sql = "create table class( name text, count int )"
        g.db.execute( sql )
        g.db.commit()
        print('create success')
    except Exception as err:
        print('error:', err)
        
        
        
    
## 테이블 생성 : if not exists
# createTable 함수 내에 if not exists를 정의하고 테이블을 생성하면 존재하지 않을 경우만 생성됨
def createTable(g):
    try:
        sql = "create table if not exists student( name text, age int )"
        g.db.execute( sql )
        g.db.commit()
        print('create success')
    except Exception as err:
        print('error:', err)
        
        
        
        
## Request context / 서버 실행
# before_request에 db 연결 및  테이블 생성을 넣어 request 처리전에 테이블 생성하고 request 처리가 끈타면 db 처리를 close함
@app.before_request
def before_request():
    g.db = connect_db()
    createTalbe(g)
    print('before request')
    
@app.teardown_request
def teardown_request( exception ):
    g.db.close()
    print('end request')
    
@app.route('/')
def myTest():
    return "hello flask...:"

if __name__ == '__main__':
    app.run(use_reloader=True)

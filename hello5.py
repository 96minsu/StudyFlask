# writefile flaskr/hello5.py
# app.route : 중복 라우팅
# 여러 개의 라우팅을 하나의 함수에 연결해서 동일한 처리
import datetime
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def index():
    """Route Handler (View Function) for '/' and '/hello"""
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
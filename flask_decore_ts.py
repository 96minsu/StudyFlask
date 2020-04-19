# writefile flask_decore_ts.py
# add_rul_rule로 등록하기
# 데코레이터 대신 add_url_rule로 등록해서 사용하기
from flask import Flask

app = Flask(__name__)

def index():
    return "Hello, World!!!!!!!"

app.add_url_rule('/', 'index', index)

if __name__ =='__main__':
    app.run(debug=True)
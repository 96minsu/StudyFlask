
## redirect 함수로 라우팅 하기
# redirect(주소)를 정의해서 request 결과를 다른 웹페이지로 전달
from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return redirect('http://www.google.com')

if __name__ == '__main__':
    app.run()

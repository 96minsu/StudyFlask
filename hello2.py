# flask를 구동시키기 위한 어플리케이션 인스턴스를 생성
from flask import Flask, redirect
app = Flask(__name__)

# 31p redirect 함수로 라우팅 하기
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return redirect('http://www.google.com')

# flask를 구동시키기 위한 어플리케이션 인스턴스를 run()을 구동해서 시작
if __name__ == '__main__':
    app.run()

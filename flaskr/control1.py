
## 템플릿 : 제어 실행 로직
# name 변수에 값을 주지 않으면 if문에서 else로 처리
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    name = ""
    return render_template('control1.html', name=name)

if __name__ == '__main__' :
    app.run()

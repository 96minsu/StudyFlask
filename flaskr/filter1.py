
## 템플릿 : 필터 실행 로직
# 템플릿 렌더링을 필터링 하는 html 문서를 만들고 처리
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('filter1.html', name=name)

if __name__ == '__main__':
    app.run()

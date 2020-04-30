
## 템플릿 : 순환 실행 로직
# name, comments 변수에 값을 주고 템플릿에서 for문을 실행
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    comments = ['apple', 'orange']
    return render_template('forloop1.html', name=name, comments=comments)

if __name__ == '__main__':
    app.run()

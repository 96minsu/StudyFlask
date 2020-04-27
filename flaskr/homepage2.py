
## 변수에 값 세팅 : 실행 결과
# 변수에 세팅된 결과에 따라 실행
import datetime
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    htmltxt = render_template('homepage2.html')
    return htmltxt

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)

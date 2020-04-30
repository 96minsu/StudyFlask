
## 메인 프로그램
# 내부 리스트로 제공받은 변수에 대해 처리
import datetime
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    htmltxt = render_template('homepage1.html', the_date = datetime.date.today())
    return htmltxt

if __name__ == '__main__' :
    app.run(use_reloader=True, debug=True)

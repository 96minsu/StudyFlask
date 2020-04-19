
## app.run
# app.run 함수 파라미터에 use_reloader=True로 넣으면 수정 즉시 적용, debug=True 표시하면 debug처리
import datetime
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    htmltxt = render_template('homepage.html', the_date = datetime.date.today())
    return htmltxt

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)

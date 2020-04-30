
## 템플릿 : include 실행 로직
# 렌더링 실행
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    status = 1
    return render_template('include_body.html', status=status)

if __name__ == '__main__':
    app.run()


## 템플릿 : 상속 실행 로직
# 렌더링 실행
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('show.html')

if __name__ == '__main__':
    app.run()

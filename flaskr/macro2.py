
## 템플릿 : 매크로 실행 로직
# 매크로 지정 템플릿에 맞춰 x, y의 값을 전달
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('macro1.html', x=10, y=10)

if __name__ == '__main__':
    app.run()

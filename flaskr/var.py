
## 템플릿 문법 : 문장 처리 예시2
# 템플릿과 파이썬 함수를 실행결과
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
@app.route('/<name>')
def get_task(name=None):
    
    return render_template('var.html', name=name)

if __name__ == '__main__' :
    app.run(debug=True)

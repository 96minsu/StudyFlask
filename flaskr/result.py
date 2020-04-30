
## 템플릿 : 순환 실행 로직
# dict으로 데이터를 받아 템플릿에서 for문을 실행
from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
@app.route('/result')
def result():
    
    dict = {'phy':50, 'che':60, 'maths':70}
    
    return render_template('result.html', result = dict)

if __name__ == '__main__' :
    app.run(debug = True)

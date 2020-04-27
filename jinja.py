
## Render_template으로 변환
# 함수의 결과를 문자열로 직접 전달
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    if user:
        user = user
    else :
        user = request.args.get('user', 'Shalabh')
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)

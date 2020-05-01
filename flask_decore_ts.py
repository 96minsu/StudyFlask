
## Login 처리 예시
# Login 함수에서 get(send data 요청)과 post(요청 데이터를 받음) 메소드를 처리
from flask import Flask, session, request, redirect, url_for

app = Flask(__name__)

# set the secret key. keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/, ?RT'

def index():
    return "Hello, World!!!!!!"

app.add_url_rule('/', 'index', index)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

if __ name__ == '__main__':
    app.run(debug=True)

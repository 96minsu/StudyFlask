# writefile flask_decore_ts.py
# add_rul_rule로 등록하기
# 데코레이터 대신 add_url_rule로 등록해서 사용하기
from flask import Flask, url_for

app = Flask(__name__)

def index():
    return "Hello, World!!!!!!!"

app.add_url_rule('/', 'index', index)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        session['username'] = request.form['username']
        return redirect(rul_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
print(app.url_map)

if __name__ =='__main__':
    app.run(debug=True)
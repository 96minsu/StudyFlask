
## Request hook
# Request를 처리하기 전후에 코드를 작성하고 g객체를 가지고 정보를 공유함
from flask import Flask, render_template, request, g, session

app = Flask('__name__')

@app.route('/')
def hello():
    return " Hello Flask Jupyter Notebook"

@app.route('/hi')
def hello1():
    return "hello1 hi !!!!!" + g.my

@app.before_request
def before_request():
    g.my = "before_request"
    print('before request')
    
@app.teardown_request
def teardown_request(exception):
    print('end request')
    
if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)

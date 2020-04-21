
## HTML 문자열로 전달
# 함수의 결과를 문자열로 직접 전달
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    user = user or 'Shalabh'
    return '''
<html>
Templating with Jinja2
    <head>
    <title>Flask Framework Cookbook</title>
    </head>
    <body>
    <h1>Hello %s!</h1>
    <p>Welcome to the world of Flask! </p>
    </body>
</html>''' % user

if __name__ == '__main__':
    app.run()

# app.route:HTTP 메소드 지정
# 기본은 GET이지만 POST등이 메소드로 처리 가능
from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Post method"
    else:
        return "Get method"

if __name__ == '__main__':
    app.run()
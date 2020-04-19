# writefile flaskr/hello_ts.py
# flask를 구동시키기 위한 어플리케이션 인스턴스를 생성
from flask import Flask
app = Flask(__name__)
print(app)

# hello world 출력하기
@app.route( '/' )
def hello():
    return 'Hello World !'

# flask를 구동시키기 위한 어플리케이션 인스턴스를 run()을 구동해서 시작
if __name__ == '__main__':
    app.run(debug=True)

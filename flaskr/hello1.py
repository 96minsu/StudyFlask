from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # Render_template에 변수명은 키워드 인자로 처리
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run()

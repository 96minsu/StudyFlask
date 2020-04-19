
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template("aaa.html")

@app.route('/about')
def about():
    
    return render_template("bbb.html")

if __name__ == '__main__':
    app.run()
